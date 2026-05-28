---
name: AdaEvolveDatabase.add_merged_program
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase.add_merged_program

**File:** `skydiscover/search/adaevolve/database.py:1956`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def add_merged_program(
        self,
        program: Program,
        parent_ids: List[str],
        iteration: Optional[int] = None,
        island_idx: Optional[int] = None,
    ) -> str:
        """Add a merged program to an island."""
        idx = island_idx if island_idx is not None else self.current_island

        if idx < 0 or idx >= self.num_islands:
            raise ValueError(f"Invalid island index {idx}")

        if iteration is not None:
            program.iteration_found = iteration
            self.last_iteration = max(self.last_iteration, iteration)

        was_added = False
        if self.use_unified_archive and self.archives:
            if hasattr(self.archives[idx], "add_merged_program"):
                was_added = self.archives[idx].add_merged_program(program, parent_ids)
            else:
                was_added = self.archives[idx].add(program)
        else:
            # Legacy mode: just add to island list
            self.islands[idx].append(program)
            was_added = True
            self._enforce_island_population_limit(idx)

        if was_added:
            self.programs[program.id] = program
            fitness = self._get_fitness(program)
            self.adapter.record_evaluation(idx, fitness)
            self._invalidate_global_pareto_cache()
            self._update_best_program(program)

            if self.config.db_path:
                self._save_program(program)

            logger.debug(f"Added merged program {program.id[:8]} to island {idx}")

        return program.id
````

## → Calls
- [[AdaEvolveDatabase._enforce_island_population_limit]]
- [[AdaEvolveDatabase._get_fitness]]
- [[AdaEvolveDatabase._invalidate_global_pareto_cache]]
- [[AdaEvolveDatabase._update_best_program]]
- [[AdaptiveState.record_evaluation]]
- [[CheckpointManager._save_program]]
- [[DiscoveryControllerInput.config]]
- [[LangFuseTracer.get]]
- [[MultiDimensionalAdapter.from_dict]]
- [[Program.id]]
- [[ProgramDatabase._save_program]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]
- [[base_database.Program]]
- [[base_database.ProgramDatabase]]

## ← Called by
_(entry point — nothing in this graph calls it)_
