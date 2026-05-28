---
name: OpenAILLM._resolve_retry_options
description: method in skydiscover/llm/openai.py (llm)
metadata:
  type: project
---

# OpenAILLM._resolve_retry_options

**File:** `skydiscover/llm/openai.py:267`  
**Kind:** method  
**Layer:** #llm

## Source
````python
    def _resolve_retry_options(self, **kwargs) -> Tuple[int, int, int]:
        """Resolve retry/timeout options from kwargs, falling back to instance defaults."""
        retries = kwargs.get("retries", self.retries)
        if retries is None:
            retries = 0
        retry_delay = kwargs.get("retry_delay", self.retry_delay)
        if retry_delay is None:
            retry_delay = 2
        timeout = kwargs.get("timeout", self.timeout)
        if timeout is None:
            timeout = 300
        return retries, retry_delay, timeout
````

## → Calls
- [[EvaluatorConfig.timeout]]
- [[LLMModelConfig.retries]]
- [[LLMModelConfig.retry_delay]]
- [[LLMModelConfig.timeout]]

## ← Called by
- [[OpenAILLM._generate_text]]
- [[OpenAILLM._generate_with_image]]
