---
name: langfuse_tracer.LangFuseTracer
description: class in skydiscover/llm/langfuse_tracer.py (observability)
metadata:
  type: project
---

# langfuse_tracer.LangFuseTracer

**File:** `skydiscover/llm/langfuse_tracer.py:77`  
**Kind:** class  
**Layer:** #observability

## Source
````python
class LangFuseTracer:
    """LangFuse tracing singleton.

    Safe to call even when LangFuse is not configured — all methods
    become no-ops in that case.
    """

    _instance: Optional["LangFuseTracer"] = None
    _client: Any = None

````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[LangFuseTracer.get]]
