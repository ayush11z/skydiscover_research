---
name: UnifiedArchive.get_best
description: method in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# UnifiedArchive.get_best

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:835`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def get_best(self) -> Optional[Program]:
        """Get program with highest fitness."""
        if not self._programs:
            return None
        return max(self._programs.values(), key=lambda p: self._get_fitness(p))
````

## → Calls
- [[UnifiedArchive.__init__]]
- [[UnifiedArchive._get_fitness]]
- [[base_database.Program]]

## ← Called by
- [[AdaEvolveDatabase.get_best_program]]
