---
name: AdaEvolveDatabase._distribute_programs_to_islands
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase._distribute_programs_to_islands

**File:** `skydiscover/search/adaevolve/database.py:1410`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _distribute_programs_to_islands(self) -> None:
        """
        Distribute programs to islands when no island membership info is available.

        Used as fallback when loading from a checkpoint without AdaEvolve metadata.
        """
        programs_list = list(self.programs.values())
        if not programs_list:
            return

        # Sort by fitness (best first)
        programs_list.sort(key=lambda p: self._get_fitness(p), reverse=True)

        # Distribute round-robin to islands
        for i, program in enumerate(programs_list):
            island_idx = i % self.num_islands
            if self.use_unified_archive and self.archives:
                if island_idx < len(self.archives):
                    self.archives[island_idx].add(program)
            else:
                if island_idx < len(self.islands):
                    self.islands[island_idx].append(program)

        self._invalidate_global_pareto_cache()
        logger.info(f"Distributed {len(programs_list)} programs across {self.num_islands} islands")
````

## → Calls
- [[AdaEvolveDatabase._get_fitness]]
- [[AdaEvolveDatabase._invalidate_global_pareto_cache]]
- [[CheckpointManager.load]]
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]

## ← Called by
- [[AdaEvolveDatabase.load]]
