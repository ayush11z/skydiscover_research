---
name: config.OpenEvolveNativeDatabaseConfig
description: class in skydiscover/config.py (config)
metadata:
  type: project
---

# config.OpenEvolveNativeDatabaseConfig

**File:** `skydiscover/config.py:453`  
**Kind:** class  
**Layer:** #config

## Source
````python
class OpenEvolveNativeDatabaseConfig(DatabaseConfig):
    """OpenEvolve Native: MAP-Elites + island-based search config."""

    num_islands: int = 5
    population_size: int = 40
    archive_size: int = 100
    exploration_ratio: float = 0.2
    exploitation_ratio: float = 0.7
    elite_selection_ratio: float = 0.1
    feature_dimensions: List[str] = field(default_factory=lambda: ["complexity", "diversity"])
    feature_bins: int = 10
    diversity_reference_size: int = 20
    migration_interval: int = 10
    migration_rate: float = 0.1
    random_seed: Optional[int] = 42
````

## → Calls
- [[config.DatabaseConfig]]

## ← Called by
_(entry point — nothing in this graph calls it)_
