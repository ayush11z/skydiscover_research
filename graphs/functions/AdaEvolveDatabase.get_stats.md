---
name: AdaEvolveDatabase.get_stats
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase.get_stats

**File:** `skydiscover/search/adaevolve/database.py:883`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def get_stats(self) -> Dict[str, Any]:
        """Get comprehensive statistics for logging/debugging."""
        adapter_stats = self.adapter.get_stats()

        island_stats = []
        for i in range(self.num_islands):
            dim_stats = (
                adapter_stats["dimensions"][i] if i < len(adapter_stats["dimensions"]) else {}
            )

            if self.use_unified_archive and self.archives:
                archive = self.archives[i]
                island_stats.append(
                    {
                        "island": i,
                        "population_size": archive.size(),
                        "top_count": len(archive.get_top_programs()),
                        "is_current": i == self.current_island,
                        **dim_stats,
                    }
                )
            else:
                island_stats.append(
                    {
                        "island": i,
                        "population_size": len(self.islands[i]),
                        "top_count": 0,
                        "is_current": i == self.current_island,
                        **dim_stats,
                    }
                )

        return {
            "num_islands": self.num_islands,
            "current_island": self.current_island,
            "global_best_score": self._global_best_score,
            "global_productivity": adapter_stats["global_productivity"],
            "iteration": self._iteration_count,
            "use_unified_archive": self.use_unified_archive,
            "use_adaptive_search": self.use_adaptive_search,
            "use_ucb_selection": self.use_ucb_selection,
            "islands": island_stats,
        }
````

## → Calls
- [[MultiDimensionalAdapter.get_stats]]
- [[MultiDimensionalAdapter.select_dimension_ucb]]

## ← Called by
_(entry point — nothing in this graph calls it)_
