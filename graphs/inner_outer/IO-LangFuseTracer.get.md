---
name: IO-LangFuseTracer.get
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
- [[IO-LangFuseTracer.__init__]]
- [[IO-langfuse_tracer.LangFuseTracer]]

## ← Called by
- [[IO-CoEvolutionController._assign_search_score]]
- [[IO-CoEvolutionController._initialize_first_search_program]]
- [[IO-DiscoveryController._run_iteration]]
- [[IO-OpenAILLM.__init__]]
- [[IO-OpenAILLM._call_api_via_responses]]
- [[IO-OpenAILLM._generate_text]]
- [[IO-langfuse_tracer.get_llm_context]]
