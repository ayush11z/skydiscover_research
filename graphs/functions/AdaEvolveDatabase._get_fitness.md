---
name: AdaEvolveDatabase._get_fitness
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase._get_fitness

**File:** `skydiscover/search/adaevolve/database.py:1667`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _get_fitness(self, program: Program) -> float:
        """Get scalar fitness score used by adaptive state and fallbacks."""
        return self._get_multiobjective_proxy_score(program)
````

## → Calls
- [[AdaEvolveDatabase._get_multiobjective_proxy_score]]
- [[base_database.Program]]

## ← Called by
- [[AdaEvolveDatabase._distribute_programs_to_islands]]
- [[AdaEvolveDatabase._enforce_island_population_limit]]
- [[AdaEvolveDatabase._migrate_legacy]]
- [[AdaEvolveDatabase._sample_global_top]]
- [[AdaEvolveDatabase._sample_top]]
- [[AdaEvolveDatabase._sample_weighted]]
- [[AdaEvolveDatabase._seed_new_island]]
- [[AdaEvolveDatabase._update_best_program]]
- [[AdaEvolveDatabase.add]]
- [[AdaEvolveDatabase.add_merged_program]]
- [[AdaEvolveDatabase.get_best_program]]
- [[AdaEvolveDatabase.get_top_programs]]
- [[AdaEvolveDatabase.get_top_programs_for_island]]
- [[AdaEvolveDatabase.set_paradigms]]
