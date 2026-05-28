---
name: AdaEvolveDatabase.get_global_pareto_front
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase.get_global_pareto_front

**File:** `skydiscover/search/adaevolve/database.py:1656`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def get_global_pareto_front(self) -> List[Program]:
        """Return the non-dominated Pareto front across all islands (cached)."""
        if not self.is_multiobjective_enabled():
            return []

        if not self._global_pareto_cache_valid:
            self._global_pareto_cache = self._compute_global_pareto_front()
            self._global_pareto_cache_valid = True

        return list(self._global_pareto_cache or [])
````

## → Calls
- [[AdaEvolveDatabase._compute_global_pareto_front]]
- [[AdaEvolveDatabase.is_multiobjective_enabled]]
- [[base_database.Program]]

## ← Called by
- [[AdaEvolveDatabase._sample_global_top]]
- [[AdaEvolveDatabase._update_best_program]]
- [[AdaEvolveDatabase.get_best_program]]
- [[AdaEvolveDatabase.get_comprehensive_iteration_stats]]
- [[AdaEvolveDatabase.get_pareto_front]]
- [[AdaEvolveDatabase.get_top_programs]]
