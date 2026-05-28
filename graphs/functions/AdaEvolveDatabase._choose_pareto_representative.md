---
name: AdaEvolveDatabase._choose_pareto_representative
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase._choose_pareto_representative

**File:** `skydiscover/search/adaevolve/database.py:1617`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _choose_pareto_representative(self, front: List[Program]) -> Optional[Program]:
        """Choose a deterministic representative program from a Pareto front."""
        if not front:
            return None
        return max(front, key=self._get_pareto_representative_sort_key)
````

## → Calls
- [[AdaEvolveDatabase._get_pareto_representative_sort_key]]
- [[base_database.Program]]

## ← Called by
- [[AdaEvolveDatabase._update_best_program]]
- [[AdaEvolveDatabase.get_best_program]]
