---
name: IN-LangFuseTracer.__init__
description: method in skydiscover/llm/langfuse_tracer.py (observability)
metadata:
  type: project
---

# LangFuseTracer.__init__

**File:** `skydiscover/llm/langfuse_tracer.py:87`  
**Kind:** method  
**Layer:** #observability

## Source
````python
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
````

## → Calls
- [[IN-LangFuseTracer._flush_on_exit]]

## ← Called by
- [[IN-DiscoveryController._call_llm]]
- [[IN-DiscoveryController._create_child_program]]
- [[IN-DiscoveryController._run_from_scratch_iteration]]
- [[IN-LangFuseTracer.get]]
- [[IN-OpenAILLM._generate_with_image]]
- [[IN-OpenAILLM.generate]]
