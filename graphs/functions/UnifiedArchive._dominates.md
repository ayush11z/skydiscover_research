---
name: UnifiedArchive._dominates
description: staticmethod in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# UnifiedArchive._dominates

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:502`  
**Kind:** staticmethod  
**Layer:** #adaevolve

## Source
````python
    def _dominates(vec_a: List[float], vec_b: List[float]) -> bool:
        """True if vec_a dominates vec_b (all >= and at least one >)."""
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
- [[UnifiedArchive._compute_elite_score_for_new]]
- [[UnifiedArchive._compute_pareto_ranking]]
