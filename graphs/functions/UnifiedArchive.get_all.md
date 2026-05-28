---
name: UnifiedArchive.get_all
description: method in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# UnifiedArchive.get_all

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:876`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def get_all(self) -> List[Program]:
        """Get all programs in archive."""
        return list(self._programs.values())
````

## → Calls
- [[UnifiedArchive.__init__]]
- [[base_database.Program]]

## ← Called by
- [[AdaEvolveDatabase._all_population_programs]]
- [[AdaEvolveDatabase.active_programs]]
- [[AdaEvolveDatabase.get_best_program]]
- [[AdaEvolveDatabase.save]]
