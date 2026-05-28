---
name: AdaEvolveDatabase._invalidate_global_pareto_cache
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase._invalidate_global_pareto_cache

**File:** `skydiscover/search/adaevolve/database.py:1623`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _invalidate_global_pareto_cache(self) -> None:
        """Mark the cached global Pareto front as stale.

        The *stale* cache is intentionally preserved (not cleared) so that
        ``_update_best_program`` can read the pre-mutation front and detect
        whether a newly added program entered the front.
        """
        self._global_pareto_cache_valid = False
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[AdaEvolveDatabase._distribute_programs_to_islands]]
- [[AdaEvolveDatabase._seed_new_island]]
- [[AdaEvolveDatabase.add]]
- [[AdaEvolveDatabase.add_merged_program]]
- [[AdaEvolveDatabase.load]]
