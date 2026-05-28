---
name: AdaEvolveDatabase.add
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase.add

**File:** `skydiscover/search/adaevolve/database.py:407`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def add(
        self,
        program: Program,
        iteration: Optional[int] = None,
        parent_id: Optional[str] = None,
        target_island: Optional[int] = None,
        **kwargs,
    ) -> str:
        """
        Add a program to the population and update adaptive state.

        Args:
            program: Program to add
            iteration: Current iteration (for tracking)
            parent_id: Parent's ID (for genealogy)
            target_island: Specific island (for migrations). None = current_island.

        Returns:
            Program ID
        """
        island_idx = target_island if target_island is not None else self.current_island
        is_migration = target_island is not None and target_island != self.current_island

        if island_idx < 0 or island_idx >= self.num_islands:
            raise ValueError(f"Invalid island index {island_idx}")

        # Update iteration tracking
        if iteration is not None:
            program.iteration_found = iteration
            self.last_iteration = max(self.last_iteration, iteration)

        # Add to archive or legacy list
        was_added = False
        if self.use_unified_archive and self.archives:
            was_added = self.archives[island_idx].add(program)
            if was_added:
                self.programs[program.id] = program
            else:
                logger.debug(
                    f"Archive rejected program {program.id[:8]} on island {island_idx} "
                    f"(fitness={self._get_fitness(program):.4f})"
                )
        else:
            # Legacy mode: list-based storage
            self.programs[program.id] = program
            self.islands[island_idx].append(program)
            was_added = True

            # Track sibling relationship (only for mutations, not migrations)
            if parent_id is not None and not is_migration:
                self.children_map[island_idx].setdefault(parent_id, []).append(program.id)

            # Enforce population limit in legacy mode
            self._enforce_island_population_limit(island_idx)

        if was_added:
            # Update adaptive state
            fitness = self._get_fitness(program)
            if not is_migration:
                # Regular evaluation: full update (UCB rewards, visits, G, best_score)
                self.adapter.record_evaluation(island_idx, fitness)
            else:
                # Migration: update best_score and G only (for correct search intensity)
                # UCB stats remain unchanged (island didn't earn the improvement)
                # This fixes: 1) future delta calculations, 2) exploitation mode trigger
                self.adapter.receive_external_improvement(island_idx, fitness)

            # Invalidate BEFORE _update_best_program so it can read the stale
            # cache as the "previous" front and detect front membership changes.
            self._invalidate_global_pareto_cache()

            # Update global best and track for paradigm
            global_improved = self._update_best_program(program)

            # Record improvement for paradigm tracking
            if self.paradigm_tracker is not None and not is_migration:
                self.paradigm_tracker.record_improvement(global_improved, self._global_best_score)

            # Save if configured
            if self.config.db_path:
                self._save_program(program)

            logger.debug(
                f"Added program {program.id[:8]} to island {island_idx} "
                f"(migration={is_migration})"
            )

        return program.id
````

## → Calls
- [[AdaEvolveDatabase.__init__]]
- [[AdaEvolveDatabase._enforce_island_population_limit]]
- [[AdaEvolveDatabase._get_fitness]]
- [[AdaEvolveDatabase._invalidate_global_pareto_cache]]
- [[AdaEvolveDatabase._update_best_program]]
- [[CheckpointManager._save_program]]
- [[DiscoveryControllerInput.config]]
- [[MultiDimensionalAdapter.receive_external_improvement]]
- [[MultiDimensionalAdapter.record_evaluation]]
- [[ParadigmTracker.record_improvement]]
- [[Program.id]]
- [[ProgramDatabase._save_program]]
- [[base_database.Program]]
- [[base_database.ProgramDatabase]]

## ← Called by
- [[AdaEvolveDatabase._migrate_archives]]
- [[AdaEvolveDatabase._migrate_legacy]]
- [[AdaEvolveDatabase.seed_all_islands]]
