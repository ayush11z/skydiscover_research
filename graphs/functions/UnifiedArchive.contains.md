---
name: UnifiedArchive.contains
description: method in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# UnifiedArchive.contains

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:888`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def contains(self, program_id: str) -> bool:
        """Check if program is in archive."""
        return program_id in self._programs
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[AdaEvolveDatabase._get_archive_crowding_distance]]
- [[AdaEvolveDatabase._get_archive_elite_score]]
