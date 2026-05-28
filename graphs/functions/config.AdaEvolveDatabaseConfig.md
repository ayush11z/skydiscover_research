---
name: config.AdaEvolveDatabaseConfig
description: class in skydiscover/config.py (config)
metadata:
  type: project
---

# config.AdaEvolveDatabaseConfig

**File:** `skydiscover/config.py:398`  
**Kind:** class  
**Layer:** #config

## Source
````python
class AdaEvolveDatabaseConfig(DatabaseConfig):
    """AdaEvolve adaptive multi-island database config."""

    population_size: int = 20
    num_islands: int = 2
    decay: float = 0.9
    intensity_min: float = 0.15
    intensity_max: float = 0.5
    use_adaptive_search: bool = True
    use_ucb_selection: bool = True
    use_migration: bool = True
    use_unified_archive: bool = True
    fixed_intensity: float = 0.4
    migration_interval: int = 15
    migration_count: int = 5
    local_context_program_ratio: float = 0.6
    archive_elite_ratio: float = 0.2
    pareto_weight: float = 0.4
    fitness_weight: float = 1.0
    novelty_weight: float = 0.0
    k_neighbors: int = 5
    diversity_strategy: str = "code"
    use_dynamic_islands: bool = True
    max_islands: int = 5
    spawn_productivity_threshold: float = 0.015
    spawn_cooldown_iterations: int = 30
    use_paradigm_breakthrough: bool = True
    paradigm_window_size: int = 10
    paradigm_improvement_threshold: float = 0.12
    paradigm_max_uses: int = 2
    paradigm_num_to_generate: int = 3
````

## → Calls
- [[config.DatabaseConfig]]

## ← Called by
_(entry point — nothing in this graph calls it)_
