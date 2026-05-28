---
name: IN-LangFuseTracer.get
description: classmethod in skydiscover/llm/langfuse_tracer.py (observability)
metadata:
  type: project
---

# LangFuseTracer.get

**File:** `skydiscover/llm/langfuse_tracer.py:123`  
**Kind:** classmethod  
**Layer:** #observability

## Source
````python
    def get(cls) -> "LangFuseTracer":
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
````

## → Calls
- [[IN-LangFuseTracer.__init__]]
- [[IN-langfuse_tracer.LangFuseTracer]]

## ← Called by
- [[IN-DiscoveryController._run_iteration]]
- [[IN-OpenAILLM.__init__]]
- [[IN-OpenAILLM._call_api_via_responses]]
- [[IN-OpenAILLM._generate_text]]
- [[IN-langfuse_tracer.get_llm_context]]
