---
name: IO-llm_pool.LLMPool
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
- [[IO-CoEvolutionController._generate_variation_operators]]
- [[IO-DiscoveryController.__init__]]
- [[IO-EvoxContextBuilder.__init__]]
- [[IO-variation_operator_generator.generate_variation_operators]]
- [[IO-variation_operator_generator.main]]
