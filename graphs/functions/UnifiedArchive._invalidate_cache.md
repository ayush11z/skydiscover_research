---
name: UnifiedArchive._invalidate_cache
description: method in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# UnifiedArchive._invalidate_cache

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:230`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _invalidate_cache(self) -> None:
        """Mark caches as invalid."""
        self._cache_valid = False
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[UnifiedArchive._evict]]
- [[UnifiedArchive._insert]]
