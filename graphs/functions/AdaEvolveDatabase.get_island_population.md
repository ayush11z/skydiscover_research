---
name: AdaEvolveDatabase.get_island_population
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase.get_island_population

**File:** `skydiscover/search/adaevolve/database.py:346`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def get_island_population(self, island_idx: int) -> List[Program]:
        """Get all programs in a specific island."""
        if 0 <= island_idx < self.num_islands:
            if self.use_unified_archive and self.archives:
                return self.archives[island_idx].get_all()
            else:
                return list(self.islands[island_idx])
        return []
````

## → Calls
- [[base_database.Program]]

## ← Called by
- [[AdaEvolveDatabase.get_pareto_front]]
