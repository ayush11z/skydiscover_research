---
name: IO-langfuse_tracer._infer_loop_type
description: function in skydiscover/llm/langfuse_tracer.py (observability)
metadata:
  type: project
---

# langfuse_tracer._infer_loop_type

**File:** `skydiscover/llm/langfuse_tracer.py:64`  
**Kind:** function  
**Layer:** #observability

## Source
````python
def _infer_loop_type(model_name: str) -> str:
    name = model_name.lower()
    if any(s in name for s in ("qwen", "coder")):
        return "outer"
    if "gemma" in name:
        return "inner"
    return "unknown"
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-OpenAILLM._generate_text]]
