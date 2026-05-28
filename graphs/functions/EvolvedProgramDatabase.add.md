---
name: EvolvedProgramDatabase.add
description: method in skydiscover/search/evox/database/initial_search_strategy.py (evox)
metadata:
  type: project
---

# EvolvedProgramDatabase.add

**File:** `skydiscover/search/evox/database/initial_search_strategy.py:36`  
**Kind:** method  
**Layer:** #evox

## Source
````python
    def add(self, program: EvolvedProgram, iteration: Optional[int] = None, **kwargs) -> str:
        """Add program and update stagnation tracking."""
        if iteration == 0 or program.iteration_found == 0:
            self.initial_program = program

        self.programs[program.id] = program

        if iteration is not None:
            self.last_iteration = max(self.last_iteration, iteration)

        if self.config.db_path:
            self._save_program(program)

        self._update_best_program(program)

        # Track best score per add() call so sample() can detect stagnation.
        current_best = max(
            (p.metrics.get("combined_score", 0.0)
             for p in self.programs.values()
             if isinstance(p.metrics.get("combined_score"), (int, float))),
            default=0.0,
        )
        self._best_score_history.append(current_best)
        if self._last_best is not None:
            improved = current_best - self._last_best > 0.01
            self._stagnant_count = 0 if improved else self._stagnant_count + 1
        self._last_best = current_best

        logger.debug(f"Added program {program.id}  best={current_best:.4f}  stagnant={self._stagnant_count}")
        return program.id
````

## → Calls
- [[CheckpointManager._save_program]]
- [[CheckpointManager.load]]
- [[DiscoveryControllerInput.config]]
- [[EvaluationResult.metrics]]
- [[EvolvedProgramDatabase.__init__]]
- [[Program.id]]
- [[Program.iteration_found]]
- [[Program.metrics]]
- [[ProgramDatabase._save_program]]
- [[ProgramDatabase._update_best_program]]
- [[base_database.ProgramDatabase]]
- [[initial_search_strategy.EvolvedProgram]]

## ← Called by
_(entry point — nothing in this graph calls it)_
