---
name: UnifiedArchive._track_genealogy
description: method in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# UnifiedArchive._track_genealogy

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:166`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _track_genealogy(self, program: Program) -> None:
        """
        Track parent-child relationship.

        ONLY call after program is successfully added to archive.
        Safe to call when parent doesn't exist (was evicted).
        """
        parent_id = getattr(program, "parent_id", None)

        if parent_id:
            self._parents[program.id] = [parent_id]
            # Note: parent_id might not be in archive (evicted) - that's OK
            self._children[parent_id].append(program.id)
        else:
            self._parents[program.id] = []
````

## → Calls
- [[Program.id]]
- [[base_database.Program]]

## ← Called by
- [[UnifiedArchive.add]]
