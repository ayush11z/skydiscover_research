---
name: database.get_island_config_preset
description: function in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# database.get_island_config_preset

**File:** `skydiscover/search/adaevolve/database.py:142`  
**Kind:** function  
**Layer:** #adaevolve

## Source
````python
def get_island_config_preset(name: str) -> Dict[str, Any]:
    """Get an island configuration preset by name."""
    for preset in ISLAND_CONFIG_PRESETS:
        if preset["name"] == name:
            return preset.copy()
    raise ValueError(f"Unknown island config preset: {name}")
````

## → Calls
- [[database.ISLAND_CONFIG_PRESETS]]

## ← Called by
- [[AdaEvolveDatabase._expand_to_island_count]]
