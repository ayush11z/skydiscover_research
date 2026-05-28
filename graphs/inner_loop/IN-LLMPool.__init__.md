---
name: IN-LLMPool.__init__
description: method in skydiscover/llm/llm_pool.py (llm)
metadata:
  type: project
---

# LLMPool.__init__

**File:** `skydiscover/llm/llm_pool.py:18`  
**Kind:** method  
**Layer:** #llm

## Source
````python
    def __init__(self, models_cfg: List[LLMModelConfig]):
        if not models_cfg:
            raise ValueError("LLMPool requires at least one model config")

        self.models_cfg = models_cfg

        # Validate weights before creating clients to fail fast on bad config.
        self.weights = [m.weight for m in models_cfg]
        if any(w < 0 for w in self.weights):
            raise ValueError("LLMPool model weights must be non-negative")
        total = sum(self.weights)
        if total <= 0:
            raise ValueError("LLMPool model weights must sum to a positive value")
        self.weights = [w / total for w in self.weights]

        self.models = [
            model_cfg.init_client(model_cfg) if model_cfg.init_client else OpenAILLM(model_cfg)
            for model_cfg in models_cfg
        ]
        self.random_state = random.Random()

        # Logging
        if len(models_cfg) > 1:
            pool_key = tuple((c.name, w) for c, w in zip(models_cfg, self.weights))
            if not hasattr(logger, "_logged_pools"):
                logger._logged_pools = set()
            if pool_key not in logger._logged_pools:
                parts = ", ".join(f"{c.name}={w:.2f}" for c, w in zip(models_cfg, self.weights))
                logger.info(f"Pool weights: {parts}")
                logger._logged_pools.add(pool_key)
````

## → Calls
- [[IN-OpenAILLM.__init__]]
- [[IN-openai.OpenAILLM]]

## ← Called by
- [[IN-DiscoveryController.__init__]]
- [[IN-DiscoveryController._call_llm]]
- [[IN-DiscoveryController._create_child_program]]
- [[IN-DiscoveryController._run_from_scratch_iteration]]
- [[IN-EvoxContextBuilder.__init__]]
