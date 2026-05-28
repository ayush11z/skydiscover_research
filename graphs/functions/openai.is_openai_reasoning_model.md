---
name: openai.is_openai_reasoning_model
description: function in skydiscover/llm/openai.py (llm)
metadata:
  type: project
---

# openai.is_openai_reasoning_model

**File:** `skydiscover/llm/openai.py:51`  
**Kind:** function  
**Layer:** #llm

## Source
````python
def is_openai_reasoning_model(model_name: str, api_base: str) -> bool:
    """Check if a model is an OpenAI reasoning model requiring special parameters."""
    api_base_lower = (api_base or "").lower()
    is_openai_api = (
        any(api_base_lower.startswith(p) for p in _OPENAI_API_PREFIXES)
        or ".openai.azure.com" in api_base_lower
    )
    return is_openai_api and model_name.lower().startswith(REASONING_MODEL_PREFIXES)
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[AgenticGenerator._call_llm]]
- [[AgenticGenerator._call_llm_responses]]
- [[OpenAILLM._generate_text]]
