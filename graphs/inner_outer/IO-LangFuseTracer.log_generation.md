---
name: IO-LangFuseTracer.log_generation
description: method in skydiscover/llm/langfuse_tracer.py (observability)
metadata:
  type: project
---

# LangFuseTracer.log_generation

**File:** `skydiscover/llm/langfuse_tracer.py:132`  
**Kind:** method  
**Layer:** #observability

## What it does
Sends one generation record to LangFuse (if configured). Records:
- Full prompt (messages list)
- Full response text
- Latency in seconds
- Token usage (prompt / completion / total)
- `loop_type` — "inner" or "outer" — so you can filter by loop in the UI
- `iteration` number

Called by OpenAILLM._generate_text immediately after each successful API call. No-op if `LANGFUSE_PUBLIC_KEY` / `LANGFUSE_SECRET_KEY` are not set.

## Source
````python
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
        _usage = usage or {}
        _tokens = {
            "input": _usage.get("prompt_tokens", 0),
            "output": _usage.get("completion_tokens", 0),
            "total": _usage.get("total_tokens", 0),
        }
        metadata = {
            "loop_type": loop_type,
            "iteration": iteration,
            "latency_s": round(latency_s, 3),
        }
        try:
            if hasattr(self._client, "start_observation"):
                # langfuse v3 / v4 — OpenTelemetry-based API.
                gen = self._client.start_observation(
                    name=f"{loop_type}_loop",
                    as_type="generation",
                    input=messages,
                    output=output,
                    model=model,
                    usage_details=_tokens,
                    metadata=metadata,
                )
                gen.end()
            elif hasattr(self._client, "generation"):
                # langfuse v2 — legacy direct API.
                self._client.generation(
                    name=f"{loop_type}_loop",
                    model=model,
                    input=messages,
                    output=output,
                    usage={**_tokens, "unit": "TOKENS"},
                    metadata=metadata,
                )
        except Exception as exc:
            logger.warning("LangFuse log error (non-fatal): %s", exc)
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-OpenAILLM._generate_text]]
