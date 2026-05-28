---
name: IN-langfuse_tracer.get_llm_context
description: function in skydiscover/llm/langfuse_tracer.py (observability)
metadata:
  type: project
---

# langfuse_tracer.get_llm_context

**File:** `skydiscover/llm/langfuse_tracer.py:54`  
**Kind:** function  
**Layer:** #observability

## Source
````python
def get_llm_context() -> Dict[str, Any]:
    """Return the current loop metadata dict (may be empty)."""
    return _llm_ctx.get()
````

## → Calls
- [[IN-LangFuseTracer.get]]

## ← Called by
- [[IN-OpenAILLM._generate_text]]
