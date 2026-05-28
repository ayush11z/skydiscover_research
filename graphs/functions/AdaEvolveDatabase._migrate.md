---
name: AdaEvolveDatabase._migrate
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase._migrate

**File:** `skydiscover/search/adaevolve/database.py:797`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _migrate(self) -> None:
        """
        Ring migration: copy top programs to next island.

        Ring topology: island i → island (i+1) % num_islands
        """
        if self.use_unified_archive and self.archives:
            self._migrate_archives()
        else:
            self._migrate_legacy()
````

## → Calls
- [[AdaEvolveDatabase._migrate_archives]]
- [[AdaEvolveDatabase._migrate_legacy]]

## ← Called by
- [[AdaEvolveDatabase.end_iteration]]
