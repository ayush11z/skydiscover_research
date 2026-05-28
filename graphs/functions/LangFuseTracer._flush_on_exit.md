---
name: LangFuseTracer._flush_on_exit
description: method in skydiscover/llm/langfuse_tracer.py (observability)
metadata:
  type: project
---

# LangFuseTracer._flush_on_exit

**File:** `skydiscover/llm/langfuse_tracer.py:115`  
**Kind:** method  
**Layer:** #observability

## Source
````python
    def _flush_on_exit(self) -> None:
        if self._client:
            try:
                self._client.flush()
            except Exception:
                pass
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[LangFuseTracer.__init__]]
