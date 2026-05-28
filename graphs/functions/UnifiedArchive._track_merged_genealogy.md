---
name: UnifiedArchive._track_merged_genealogy
description: method in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# UnifiedArchive._track_merged_genealogy

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:825`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _track_merged_genealogy(self, program: Program, parent_ids: List[str]) -> None:
        """Track genealogy for merged program with multiple parents."""
        self._parents[program.id] = list(parent_ids)
        for parent_id in parent_ids:
            self._children[parent_id].append(program.id)
````

## → Calls
- [[Program.id]]
- [[base_database.Program]]

## ← Called by
- [[UnifiedArchive.add_merged_program]]
