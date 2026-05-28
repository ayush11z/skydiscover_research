---
name: TopKDatabase.add
description: method in skydiscover/search/topk/database.py (topk)
metadata:
  type: project
---

# TopKDatabase.add

**File:** `skydiscover/search/topk/database.py:17`  
**Kind:** method  
**Layer:** #topk

## Source
````python
    def add(self, program: Program, iteration: Optional[int] = None, **kwargs) -> str:
        """Add a program to the database (minimal Top-K)."""
        # Store the initial program
        if iteration == 0 or program.iteration_found == 0:
            self.initial_program = program

        # Store the program
        self.programs[program.id] = program

        # Track last iteration if provided
        if iteration is not None:
            self.last_iteration = max(self.last_iteration, iteration)

        # Save to disk if configured
        if self.config.db_path:
            self._save_program(program)

        # NOTE: no enforcement on population size at all
        # Update the absolute best program tracking
        self._update_best_program(program)

        logger.debug(f"Added program {program.id} to top-k database")
        return program.id
````

## → Calls
- [[CheckpointManager._save_program]]
- [[DiscoveryControllerInput.config]]
- [[Program.id]]
- [[Program.iteration_found]]
- [[ProgramDatabase._save_program]]
- [[ProgramDatabase._update_best_program]]
- [[base_database.Program]]
- [[base_database.ProgramDatabase]]

## ← Called by
_(entry point — nothing in this graph calls it)_
