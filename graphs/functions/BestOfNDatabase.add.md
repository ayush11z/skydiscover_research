---
name: BestOfNDatabase.add
description: method in skydiscover/search/best_of_n/database.py (best-of-n)
metadata:
  type: project
---

# BestOfNDatabase.add

**File:** `skydiscover/search/best_of_n/database.py:34`  
**Kind:** method  
**Layer:** #best-of-n

## Source
````python
    def add(self, program: Program, iteration: Optional[int] = None, **kwargs) -> str:
        """
        Add a program to the database and increment parent iteration count.
        """
        # Store the program
        self.programs[program.id] = program

        # Track last iteration if provided
        if iteration is not None:
            self.last_iteration = max(self.last_iteration, iteration)

        # Increment counter for current parent
        if self.current_parent_id is not None:
            self.parent_iteration_count += 1

        # Save to disk if configured
        if self.config.db_path:
            self._save_program(program)

        # Update the absolute best program tracking
        self._update_best_program(program)

        logger.debug(
            f"Added program {program.id} to best-of-N database (count={self.parent_iteration_count}/{self.n})"
        )
        return program.id
````

## → Calls
- [[CheckpointManager._save_program]]
- [[DiscoveryControllerInput.config]]
- [[Program.id]]
- [[ProgramDatabase._save_program]]
- [[ProgramDatabase._update_best_program]]
- [[base_database.Program]]
- [[base_database.ProgramDatabase]]

## ← Called by
_(entry point — nothing in this graph calls it)_
