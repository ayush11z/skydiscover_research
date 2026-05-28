---
name: defaults.load_defaults
description: function in skydiscover/extras/external/defaults/__init__.py (external)
metadata:
  type: project
---

# defaults.load_defaults

**File:** `skydiscover/extras/external/defaults/__init__.py:10`  
**Kind:** function  
**Layer:** #external

## Source
````python
def load_defaults(filename: str) -> dict:
    """Load a YAML defaults file from the defaults directory."""
    path = os.path.join(_DIR, filename)
    if not os.path.exists(path):
        return {}
    with open(path) as f:
        return yaml.safe_load(f) or {}
````

## → Calls
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]

## ← Called by
- [[openevolve_backend._map_config]]
- [[shinkaevolve_backend._map_config]]
