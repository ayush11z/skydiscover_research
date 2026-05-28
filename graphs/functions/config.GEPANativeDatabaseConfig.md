---
name: config.GEPANativeDatabaseConfig
description: class in skydiscover/config.py (config)
metadata:
  type: project
---

# config.GEPANativeDatabaseConfig

**File:** `skydiscover/config.py:484`  
**Kind:** class  
**Layer:** #config

## Source
````python
class GEPANativeDatabaseConfig(DatabaseConfig):
    """Configuration for GEPA Native search database.

    GEPA (Guided Evolution for Program Adaptation) uses an elite pool with
    epsilon-greedy selection, acceptance gating, and LLM-mediated merge.
    """

    population_size: int = 40
    candidate_selection_strategy: str = "epsilon_greedy"  # "epsilon_greedy", "best", "pareto"
    epsilon: float = 0.1
    max_rejection_history: int = 20

    # Controller-read settings (stored here for single config source)
    acceptance_gating: bool = True
    use_merge: bool = True
    merge_after_stagnation: int = 15
    max_merge_attempts: int = 10
    max_recent_failures: int = 5
    random_seed: Optional[int] = 42
````

## → Calls
- [[config.DatabaseConfig]]

## ← Called by
_(entry point — nothing in this graph calls it)_
