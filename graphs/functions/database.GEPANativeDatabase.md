---
name: database.GEPANativeDatabase
description: class in skydiscover/search/gepa_native/database.py (gepa)
metadata:
  type: project
---

# database.GEPANativeDatabase

**File:** `skydiscover/search/gepa_native/database.py:35`  
**Kind:** class  
**Layer:** #gepa

## Source
````python
class GEPANativeDatabase(ProgramDatabase):
    """
    Program database for GEPA Native search.

    Maintains a fixed-size elite pool sorted by combined_score.
    Supports epsilon-greedy parent selection, per-metric best tracking,
    and a rejection history deque for reflective prompting.

    Configuration options (via GEPANativeDatabaseConfig):
        population_size: Maximum elite pool size (default: 40)
        candidate_selection_strategy: Parent selection strategy (default: "epsilon_greedy")
            - "epsilon_greedy": Pick best with probability (1-epsilon), random otherwise
            - "best": Always pick the highest-scoring program
            - "pareto": Frequency-weighted sampling from the Pareto front across metrics
        epsilon: Exploration probability for epsilon-greedy (default: 0.1)
        max_rejection_history: Max rejected programs to keep (default: 20)
    """

````

## → Calls
- [[base_database.ProgramDatabase]]

## ← Called by
_(entry point — nothing in this graph calls it)_
