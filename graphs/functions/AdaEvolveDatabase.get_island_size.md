---
name: AdaEvolveDatabase.get_island_size
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase.get_island_size

**File:** `skydiscover/search/adaevolve/database.py:355`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def get_island_size(self, island_idx: int) -> int:
        """Get number of programs in a specific island."""
        if 0 <= island_idx < self.num_islands:
            if self.use_unified_archive and self.archives:
                return self.archives[island_idx].size()
            else:
                return len(self.islands[island_idx])
        return 0
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[AdaEvolveDatabase.get_archive_stats]]
- [[AdaEvolveDatabase.seed_all_islands]]
