---
name: AdaEvolveDatabase._has_duplicate_solution
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase._has_duplicate_solution

**File:** `skydiscover/search/adaevolve/database.py:872`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _has_duplicate_solution(self, island_idx: int, solution: str) -> bool:
        """Check if island already has a program with identical solution."""
        if self.use_unified_archive and self.archives:
            return any(p.solution == solution for p in self.archives[island_idx].get_all())
        else:
            return any(p.solution == solution for p in self.islands[island_idx])
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[AdaEvolveDatabase._migrate_archives]]
- [[AdaEvolveDatabase._migrate_legacy]]
