---
name: AdaEvolveDatabase._dominates
description: staticmethod in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase._dominates

**File:** `skydiscover/search/adaevolve/database.py:1565`  
**Kind:** staticmethod  
**Layer:** #adaevolve

## Source
````python
    def _dominates(vec_a: List[float], vec_b: List[float]) -> bool:
        """True if vec_a Pareto-dominates vec_b (same-length vectors required)."""
        if len(vec_a) != len(vec_b):
            raise ValueError(
                f"Objective vectors must have equal length, got {len(vec_a)} vs {len(vec_b)}"
            )
        at_least_one_better = False
        for a, b in zip(vec_a, vec_b):
            if a < b:
                return False
            if a > b:
                at_least_one_better = True
        return at_least_one_better
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[AdaEvolveDatabase._compute_global_pareto_front]]
- [[AdaEvolveDatabase.get_pareto_front]]
