---
name: IN-langfuse_tracer.set_llm_context
description: function in skydiscover/llm/langfuse_tracer.py (observability)
metadata:
  type: project
---

# langfuse_tracer.set_llm_context

**File:** `skydiscover/llm/langfuse_tracer.py:32`  
**Kind:** function  
**Layer:** #observability

## Source
````python
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
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IN-DiscoveryController._run_iteration]]
