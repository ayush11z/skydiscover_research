---
name: UnifiedArchive._evict
description: method in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# UnifiedArchive._evict

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:187`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _evict(self, program_id: str) -> None:
        """
        Remove program from archive with complete genealogy cleanup.

        Cleans up:
        - Program's entry in _parents
        - Program's entry in _children (its children list)
        - References to program in other entries' children lists
        """
        if program_id not in self._programs:
            return

        self._cleanup_genealogy(program_id)
        del self._programs[program_id]
        self._invalidate_cache()
````

## → Calls
- [[UnifiedArchive._cleanup_genealogy]]
- [[UnifiedArchive._invalidate_cache]]

## ← Called by
- [[UnifiedArchive.add]]
- [[UnifiedArchive.add_merged_program]]
