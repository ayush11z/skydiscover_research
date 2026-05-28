---
name: AdaEvolveDatabase._get_objective_vector
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase._get_objective_vector

**File:** `skydiscover/search/adaevolve/database.py:1546`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _get_objective_vector(self, program: Program) -> Optional[List[float]]:
        """Return the configured objective vector for a program.

        Missing or non-numeric objectives are filled with ``-inf`` so that
        programs with incomplete metrics cannot accidentally dominate
        fully-evaluated programs (all objectives are in "higher is better"
        space after normalisation).
        """
        if not self.is_multiobjective_enabled():
            return None

        metrics = getattr(program, "metrics", None) or {}
        vector: List[float] = []
        for objective in self.pareto_objectives:
            normalized = self._metric_to_maximization_value(objective, metrics.get(objective))
            vector.append(normalized if normalized is not None else float("-inf"))
        return vector
````

## → Calls
- [[AdaEvolveDatabase._metric_to_maximization_value]]
- [[AdaEvolveDatabase.is_multiobjective_enabled]]
- [[base_database.Program]]

## ← Called by
- [[AdaEvolveDatabase._compute_global_pareto_front]]
- [[AdaEvolveDatabase.get_pareto_front]]
