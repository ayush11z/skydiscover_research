---
name: IO-LLMPool.generate
description: method in skydiscover/llm/llm_pool.py (llm)
metadata:
  type: project
---

# LLMPool.generate

**File:** `skydiscover/llm/llm_pool.py:56`  
**Kind:** method  
**Layer:** #llm

## What it does
Entry point for all LLM calls. Picks one model from the pool via LLMPool._sample_model (weighted random if multiple keys are configured), then delegates to OpenAILLM.generate.

## Source
````python
    async def generate(
        self, system_message: str, messages: List[Dict[str, Any]], **kwargs
    ) -> LLMResponse:
        """Sample a model and generate a response."""
        model = self._sample_model()
        return await model.generate(system_message, messages, **kwargs)
````

## → Calls
- [[IO-LLMInterface.generate]]
- [[IO-LLMPool._sample_model]]
- [[IO-base.LLMResponse]]

## ← Called by
- [[IO-DiscoveryController._call_llm]]
- [[IO-EvoxContextBuilder._generate_batch_summaries_async]]
- [[IO-EvoxContextBuilder._generate_problem_context_summary_async]]
- [[IO-EvoxContextBuilder._generate_stats_insight_async]]
- [[IO-LLMPool.generate_all]]
- [[IO-variation_operator_generator.generate_variation_operators]]
