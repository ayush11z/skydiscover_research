---
name: AdaEvolveDatabase.active_programs
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase.active_programs

**File:** `skydiscover/search/adaevolve/database.py:333`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def active_programs(self) -> Dict[str, Program]:
        """Programs currently in all island populations."""
        result = {}
        if self.use_unified_archive and self.archives:
            for archive in self.archives:
                for p in archive.get_all():
                    result[p.id] = p
        else:
            for island in self.islands:
                for p in island:
                    result[p.id] = p
        return result
````

## → Calls
- [[AdaEvolveDatabase.__init__]]
- [[UnifiedArchive.get_all]]
- [[base_database.Program]]

## ← Called by
_(entry point — nothing in this graph calls it)_
