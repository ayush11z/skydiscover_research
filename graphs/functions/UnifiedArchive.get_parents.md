---
name: UnifiedArchive.get_parents
description: method in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# UnifiedArchive.get_parents

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:729`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def get_parents(self, program_id: str) -> List[Program]:
        """Get parents of a program."""
        parent_ids = self._parents.get(program_id, [])
        return [self._programs[pid] for pid in parent_ids if pid in self._programs]
````

## → Calls
- [[UnifiedArchive.__init__]]
- [[base_database.Program]]

## ← Called by
_(entry point — nothing in this graph calls it)_
