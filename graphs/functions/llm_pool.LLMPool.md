---
name: llm_pool.LLMPool
description: class in skydiscover/llm/llm_pool.py (llm)
metadata:
  type: project
---

# llm_pool.LLMPool

**File:** `skydiscover/llm/llm_pool.py:15`  
**Kind:** class  
**Layer:** #llm

## Source
````python
class LLMPool:
    """Weighted pool of LLM backends. Samples one per generate() call."""

````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[AdaEvolveController.__init__]]
- [[CoEvolutionController._generate_variation_operators]]
- [[DiscoveryController.__init__]]
- [[EvoxContextBuilder.__init__]]
- [[GEPANativeController._attempt_merge]]
- [[LLMJudge.__init__]]
- [[ParadigmGenerator.__init__]]
- [[variation_operator_generator.generate_variation_operators]]
- [[variation_operator_generator.main]]
