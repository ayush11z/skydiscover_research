---
name: AdaEvolveDatabase.get_top_programs_for_island
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase.get_top_programs_for_island

**File:** `skydiscover/search/adaevolve/database.py:1872`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def get_top_programs_for_island(self, island_idx: Optional[int] = None) -> List[Program]:
        """Get top programs for an island (current island if not specified)."""
        idx = island_idx if island_idx is not None else self.current_island
        if 0 <= idx < self.num_islands:
            if self.use_unified_archive and self.archives:
                return self.archives[idx].get_top_programs()
            else:
                # Legacy mode: return top 25% programs
                population = self.islands[idx]
                if not population:
                    return []
                sorted_pop = sorted(population, key=self._get_fitness, reverse=True)
                return sorted_pop[: max(1, len(sorted_pop) // 4)]
        return []
````

## → Calls
- [[AdaEvolveDatabase._get_fitness]]
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]
- [[base_database.Program]]

## ← Called by
- [[AdaEvolveDatabase.get_archive_stats]]
- [[AdaEvolveDatabase.get_pareto_front]]
