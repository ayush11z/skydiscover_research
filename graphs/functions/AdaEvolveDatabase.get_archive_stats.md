---
name: AdaEvolveDatabase.get_archive_stats
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase.get_archive_stats

**File:** `skydiscover/search/adaevolve/database.py:1923`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def get_archive_stats(self, island_idx: Optional[int] = None) -> Dict[str, Any]:
        """Get archive statistics for an island."""
        idx = island_idx if island_idx is not None else self.current_island
        if 0 <= idx < self.num_islands:
            if self.use_unified_archive and self.archives and hasattr(self.archives[idx], "stats"):
                return self.archives[idx].stats()
        top_count = len(self.get_top_programs_for_island(idx))
        return {
            "size": self.get_island_size(idx),
            "max_size": self.population_size,
            "top_count": top_count,
            "pareto_count": top_count,  # Backwards compatibility
        }
````

## → Calls
- [[AdaEvolveDatabase.get_island_size]]
- [[AdaEvolveDatabase.get_top_programs_for_island]]
- [[AdaEvolveDatabaseConfig.population_size]]
- [[GEPANativeDatabaseConfig.population_size]]
- [[LangFuseTracer.get]]
- [[OpenEvolveNativeDatabaseConfig.population_size]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]

## ← Called by
_(entry point — nothing in this graph calls it)_
