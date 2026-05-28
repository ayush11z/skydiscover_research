---
name: UnifiedArchive.get_children
description: method in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# UnifiedArchive.get_children

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:724`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def get_children(self, program_id: str) -> List[Program]:
        """Get all children of a program (for sibling context)."""
        child_ids = self._children.get(program_id, [])
        return [self._programs[cid] for cid in child_ids if cid in self._programs]
````

## → Calls
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]
- [[base_database.Program]]

## ← Called by
_(entry point — nothing in this graph calls it)_
