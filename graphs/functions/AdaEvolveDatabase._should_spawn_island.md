---
name: AdaEvolveDatabase._should_spawn_island
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase._should_spawn_island

**File:** `skydiscover/search/adaevolve/database.py:2003`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _should_spawn_island(self) -> bool:
        """
        Check if we should spawn a new island.

        Triggers spawning when:
        1. Dynamic islands is enabled
        2. Using unified archives (legacy mode doesn't support spawning)
        3. Haven't reached max_islands limit
        4. Cooldown period has passed since last spawn
        5. Global productivity is below threshold (all islands struggling)
        """
        if not self.use_dynamic_islands:
            return False

        # Dynamic spawning only works with unified archives
        if not self.use_unified_archive:
            return False

        if not self.programs:
            return False

        if self.num_islands >= self.max_islands:
            return False

        iterations_since_spawn = self._iteration_count - self.last_spawn_iteration
        if iterations_since_spawn < self.spawn_cooldown:
            return False

        # Check global productivity from adapter
        global_productivity = self.adapter.get_global_productivity()
        if global_productivity >= self.spawn_productivity_threshold:
            return False

        logger.info(
            f"Spawn conditions met: global_productivity={global_productivity:.3f} "
            f"< threshold={self.spawn_productivity_threshold}, "
            f"islands={self.num_islands}/{self.max_islands}"
        )
        return True
````

## → Calls
- [[CheckpointManager.load]]
- [[LangFuseTracer.get]]
- [[MultiDimensionalAdapter.from_dict]]
- [[MultiDimensionalAdapter.get_global_productivity]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]

## ← Called by
- [[AdaEvolveDatabase.end_iteration]]
- [[AdaEvolveDatabase.get_comprehensive_iteration_stats]]
