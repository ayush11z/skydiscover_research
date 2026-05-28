---
name: AdaEvolveDatabase._get_pareto_representative_sort_key
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase._get_pareto_representative_sort_key

**File:** `skydiscover/search/adaevolve/database.py:1601`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _get_pareto_representative_sort_key(
        self, program: Program
    ) -> Tuple[float, float, float, int, str]:
        """Sort key for choosing one stable representative from a Pareto front.

        Higher values win (used with ``max``).  Ties are broken by:
        proxy score → crowding distance → elite score → newer iteration → ID.
        """
        return (
            self._get_multiobjective_proxy_score(program),
            self._get_archive_crowding_distance(program),
            self._get_archive_elite_score(program),
            getattr(program, "iteration_found", 0),  # newer wins ties
            program.id,
        )
````

## → Calls
- [[AdaEvolveDatabase._get_archive_crowding_distance]]
- [[AdaEvolveDatabase._get_archive_elite_score]]
- [[AdaEvolveDatabase._get_multiobjective_proxy_score]]
- [[Program.id]]
- [[base_database.Program]]

## ← Called by
- [[AdaEvolveDatabase._choose_pareto_representative]]
- [[AdaEvolveDatabase._compute_global_pareto_front]]
- [[AdaEvolveDatabase.get_pareto_front]]
