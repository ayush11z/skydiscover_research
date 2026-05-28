---
name: langfuse_tracer.reset_llm_context
description: function in skydiscover/llm/langfuse_tracer.py (observability)
metadata:
  type: project
---

# langfuse_tracer.reset_llm_context

**File:** `skydiscover/llm/langfuse_tracer.py:49`  
**Kind:** function  
**Layer:** #observability

## Source
````python
def reset_llm_context(token: Any) -> None:
    """Restore context to the state before the matching set_llm_context call."""
    _llm_ctx.reset(token)
````

## → Calls
- [[AdaptiveState.reset]]

## ← Called by
- [[CoEvolutionController._generate_and_validate_search_algorithm]]
- [[DiscoveryController._run_iteration]]
