---
name: variation_operator_generator.load_config
description: function in skydiscover/search/evox/utils/variation_operator_generator.py (evox)
metadata:
  type: project
---

# variation_operator_generator.load_config

**File:** `skydiscover/search/evox/utils/variation_operator_generator.py:243`  
**Kind:** function  
**Layer:** #evox

## Source
````python
def load_config(config_path: str) -> dict:
    """Load and return the config.yaml contents."""
    with open(config_path, "r") as f:
        return yaml.safe_load(f)
````

## → Calls
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]

## ← Called by
- [[variation_operator_generator.main]]
