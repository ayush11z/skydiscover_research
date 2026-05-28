---
name: AdaEvolveDatabase._get_archive_crowding_distance
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase._get_archive_crowding_distance

**File:** `skydiscover/search/adaevolve/database.py:1579`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _get_archive_crowding_distance(self, program: Program) -> float:
        """Return archive crowding distance when available."""
        if not (self.use_unified_archive and self.archives):
            return 0.0

        for archive in self.archives:
            if archive.contains(program.id):
                archive._ensure_cache_valid()
                return archive._crowding_distances.get(program.id, 0.0)
        return 0.0
````

## → Calls
- [[AdaEvolveDatabase.__init__]]
- [[Program.id]]
- [[UnifiedArchive._ensure_cache_valid]]
- [[UnifiedArchive.contains]]
- [[base_database.Program]]

## ← Called by
- [[AdaEvolveDatabase._get_pareto_representative_sort_key]]
