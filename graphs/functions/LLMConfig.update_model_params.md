---
name: LLMConfig.update_model_params
description: method in skydiscover/config.py (config)
metadata:
  type: project
---

# LLMConfig.update_model_params

**File:** `skydiscover/config.py:229`  
**Kind:** method  
**Layer:** #config

## Source
````python
    def update_model_params(self, args: Dict[str, Any], overwrite: bool = False) -> None:
        """Update model parameters for all models (including guide_models)."""
        all_models = self.models + self.evaluator_models + self.guide_models
        for model in all_models:
            for key, value in args.items():
                if overwrite or getattr(model, key, None) is None:
                    setattr(model, key, value)
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[LLMConfig.__post_init__]]
- [[config.load_config]]
