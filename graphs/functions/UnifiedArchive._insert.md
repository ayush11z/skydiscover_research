---
name: UnifiedArchive._insert
description: method in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# UnifiedArchive._insert

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:182`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _insert(self, program: Program) -> None:
        """Insert program and invalidate caches."""
        self._programs[program.id] = program
        self._invalidate_cache()
````

## → Calls
- [[UnifiedArchive._invalidate_cache]]
- [[base_database.Program]]

## ← Called by
- [[UnifiedArchive.add]]
- [[UnifiedArchive.add_merged_program]]
