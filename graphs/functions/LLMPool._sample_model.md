---
name: LLMPool._sample_model
description: method in skydiscover/llm/llm_pool.py (llm)
metadata:
  type: project
---

# LLMPool._sample_model

**File:** `skydiscover/llm/llm_pool.py:49`  
**Kind:** method  
**Layer:** #llm

## What it does
Picks which `OpenAILLM` instance to use for this call. With a single API key this always returns the same instance; with multiple keys it samples proportionally to weights.

## Source
````python
    def _sample_model(self):
        """
        Simple weighted sampling mechanism. Override this to implement a more complex sampling mechanism.
        """
        idx = self.random_state.choices(range(len(self.models)), weights=self.weights, k=1)[0]
        return self.models[idx]
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[LLMPool.generate]]
