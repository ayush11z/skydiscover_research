"""Optional LangFuse observability for LLM calls.

Activate by setting environment variables before running:

    LANGFUSE_PUBLIC_KEY  — Langfuse project public key
    LANGFUSE_SECRET_KEY  — Langfuse project secret key
    LANGFUSE_HOST        — server URL (default: https://cloud.langfuse.com)
                           self-hosted example: http://localhost:3000

Install the SDK if not present:
    pip install langfuse
    # or: conda install -c conda-forge langfuse
"""

import atexit
import logging
import os
from contextvars import ContextVar
from typing import Any, Dict, List, Optional

logger = logging.getLogger("skydiscover.llm")

# ---------------------------------------------------------------------------
# Async-safe context variable.
# Controllers set this before making LLM calls so the tracer records
# loop_type and iteration without changing the generate() signature.
# ---------------------------------------------------------------------------

_llm_ctx: ContextVar[Dict[str, Any]] = ContextVar("_llm_ctx", default={})


def set_llm_context(loop_type: str, iteration: int) -> Any:
    """Stamp the current async context with loop metadata.

    Returns a reset token; pass it to reset_llm_context() when done
    to restore the previous context (important inside retry loops).

    Example::

        token = set_llm_context("inner", iteration)
        try:
            result = await self._call_llm(...)
        finally:
            reset_llm_context(token)
    """
    return _llm_ctx.set({"loop_type": loop_type, "iteration": iteration})


def reset_llm_context(token: Any) -> None:
    """Restore context to the state before the matching set_llm_context call."""
    _llm_ctx.reset(token)


def get_llm_context() -> Dict[str, Any]:
    """Return the current loop metadata dict (may be empty)."""
    return _llm_ctx.get()


# ---------------------------------------------------------------------------
# Fallback: infer loop type from model name when no context var is set.
# Inner loop → gemma3:12b (Ollama).  Outer loop → qwen2.5-coder:14b.
# ---------------------------------------------------------------------------

def _infer_loop_type(model_name: str) -> str:
    name = model_name.lower()
    if any(s in name for s in ("qwen", "coder")):
        return "outer"
    if "gemma" in name:
        return "inner"
    return "unknown"


# ---------------------------------------------------------------------------
# Singleton tracer
# ---------------------------------------------------------------------------

class LangFuseTracer:
    """LangFuse tracing singleton.

    Safe to call even when LangFuse is not configured — all methods
    become no-ops in that case.
    """

    _instance: Optional["LangFuseTracer"] = None
    _client: Any = None

    def __init__(self) -> None:
        public_key = os.getenv("LANGFUSE_PUBLIC_KEY")
        secret_key = os.getenv("LANGFUSE_SECRET_KEY")
        host = os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com")

        if not public_key or not secret_key:
            logger.info(
                "LangFuse tracing disabled — "
                "set LANGFUSE_PUBLIC_KEY + LANGFUSE_SECRET_KEY to enable"
            )
            return

        try:
            from langfuse import Langfuse  # type: ignore[import-untyped]

            self._client = Langfuse(
                public_key=public_key,
                secret_key=secret_key,
                host=host,
            )
            atexit.register(self._flush_on_exit)
            logger.info(f"LangFuse tracing enabled → {host}")
        except ImportError:
            logger.warning(
                "langfuse package not found — tracing disabled. "
                "Install with: pip install langfuse"
            )

    def _flush_on_exit(self) -> None:
        if self._client:
            try:
                self._client.flush()
            except Exception:
                pass

    @classmethod
    def get(cls) -> "LangFuseTracer":
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @property
    def enabled(self) -> bool:
        return self._client is not None

    def log_generation(
        self,
        *,
        model: str,
        messages: List[Dict[str, Any]],
        output: str,
        latency_s: float,
        usage: Optional[Dict[str, int]] = None,
        loop_type: str = "unknown",
        iteration: int = -1,
    ) -> None:
        """Log one LLM generation to LangFuse.

        Args:
            model: model name string (e.g. "gemma3:12b").
            messages: full formatted message list sent to the API.
            output: raw text returned by the model.
            latency_s: wall-clock seconds for the API call.
            usage: dict with prompt_tokens / completion_tokens / total_tokens.
            loop_type: "inner" | "outer" | "outer_variation" | "unknown".
            iteration: solution or search iteration number (-1 if not known).
        """
        if not self._client:
            return
        try:
            _usage = usage or {}
            self._client.generation(
                name=f"{loop_type}_loop",
                model=model,
                input=messages,
                output=output,
                usage={
                    "input": _usage.get("prompt_tokens", 0),
                    "output": _usage.get("completion_tokens", 0),
                    "total": _usage.get("total_tokens", 0),
                    "unit": "TOKENS",
                },
                metadata={
                    "loop_type": loop_type,
                    "iteration": iteration,
                    "latency_s": round(latency_s, 3),
                },
            )
        except Exception as exc:
            logger.debug("LangFuse log error (non-fatal): %s", exc)
