---
name: AdaEvolveDatabase.end_iteration
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase.end_iteration

**File:** `skydiscover/search/adaevolve/database.py:768`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def end_iteration(self, iteration: int) -> None:
        """
        End-of-iteration housekeeping.

        Handles:
        - Dynamic island spawning (if enabled and stagnating)
        - Island selection (UCB with decayed magnitude rewards OR round-robin)
        - Migration (at interval)
        """
        self._iteration_count = iteration

        # Check if we should spawn a new island
        if self._should_spawn_island():
            self._spawn_island()

        # Select next island: UCB (adaptive) or round-robin (ablation)
        if self.use_ucb_selection:
            self.current_island = self.adapter.select_dimension_ucb(iteration)
        else:
            # Round-robin selection for ablation
            # Use (iteration + 1) because this is called at END of current iteration
            # and sets the island for the NEXT iteration
            self.current_island = (iteration + 1) % self.num_islands

        # Periodic migration (can be disabled for ablation)
        if self.use_migration and iteration > 0 and iteration % self.migration_interval == 0:
            self._migrate()
            logger.info(f"Migration completed at iteration {iteration}")
````

## → Calls
- [[AdaEvolveDatabase._migrate]]
- [[AdaEvolveDatabase._should_spawn_island]]
- [[AdaEvolveDatabase._spawn_island]]
- [[MultiDimensionalAdapter.select_dimension_ucb]]

## ← Called by
_(entry point — nothing in this graph calls it)_
