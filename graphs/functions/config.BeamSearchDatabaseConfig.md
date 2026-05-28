---
name: config.BeamSearchDatabaseConfig
description: class in skydiscover/config.py (config)
metadata:
  type: project
---

# config.BeamSearchDatabaseConfig

**File:** `skydiscover/config.py:380`  
**Kind:** class  
**Layer:** #config

## Source
````python
class BeamSearchDatabaseConfig(DatabaseConfig):
    """Beam search database config."""

    beam_width: int = 5
    beam_selection_strategy: str = "diversity_weighted"
    beam_diversity_weight: float = 0.3
    beam_temperature: float = 1.0
    beam_depth_penalty: float = 0.0
````

## → Calls
- [[config.DatabaseConfig]]

## ← Called by
_(entry point — nothing in this graph calls it)_
