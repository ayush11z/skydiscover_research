---
name: LLMPool.generate
description: method in skydiscover/llm/llm_pool.py (llm)
metadata:
  type: project
---

# LLMPool.generate

**File:** `skydiscover/llm/llm_pool.py:56`  
**Kind:** method  
**Layer:** #llm

## What it does
Entry point for all LLM calls. Picks one model from the pool via [[LLMPool._sample_model]] (weighted random if multiple keys are configured), then delegates to [[OpenAILLM.generate]].

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
- [[AgenticGenerator.generate]]
- [[LLMInterface.generate]]
- [[LLMPool._sample_model]]
- [[ParadigmGenerator.generate]]
- [[base.LLMResponse]]

## ← Called by
- [[AdaEvolveController._generate_paradigms_if_needed]]
- [[DiscoveryController._call_llm]]
- [[EvoxContextBuilder._generate_batch_summaries_async]]
- [[EvoxContextBuilder._generate_problem_context_summary_async]]
- [[EvoxContextBuilder._generate_stats_insight_async]]
- [[LLMPool.generate_all]]
- [[ParadigmGenerator.generate]]
- [[variation_operator_generator.generate_variation_operators]]
