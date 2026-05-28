---
name: AdaEvolveDatabase._get_multiobjective_proxy_score
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase._get_multiobjective_proxy_score

**File:** `skydiscover/search/adaevolve/database.py:1516`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _get_multiobjective_proxy_score(self, program: Program) -> float:
        """Return a scalar proxy for adaptive state and deterministic tie-breaking."""
        metrics = getattr(program, "metrics", None) or {}
        return compute_proxy_score(
            metrics,
            fitness_key=self.fitness_key,
            pareto_objectives=self.pareto_objectives if self.is_multiobjective_enabled() else None,
            higher_is_better=self.higher_is_better,
        )
````

## → Calls
- [[AdaEvolveDatabase.is_multiobjective_enabled]]
- [[AdaEvolveDatabaseConfig.higher_is_better]]
- [[ArchiveConfig.higher_is_better]]
- [[base_database.Program]]
- [[metrics.compute_proxy_score]]

## ← Called by
- [[AdaEvolveDatabase._get_fitness]]
- [[AdaEvolveDatabase._get_pareto_representative_sort_key]]
- [[AdaEvolveDatabase.get_program_proxy_score]]
