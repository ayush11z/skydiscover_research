---
name: IN-ProgramDatabase._update_best_program
description: method in skydiscover/search/base_database.py (database)
metadata:
  type: project
---

# ProgramDatabase._update_best_program

**File:** `skydiscover/search/base_database.py:224`  
**Kind:** method  
**Layer:** #database

## Source
````python
    def _update_best_program(self, program: Program) -> None:
        """Update the best program tracking after a new program is added."""
        if self.best_program_id is None:
            self.best_program_id = program.id
            logger.debug(f"Set initial best program to {program.id}")
            return
        # If the best program is not in the database, set it to the new program
        if self.best_program_id not in self.programs:
            self.best_program_id = program.id
            return

        current_best = self.programs[self.best_program_id]

        # If the new program is better than the current best, set it to the new program
        if self._is_better(program, current_best):
            self.best_program_id = program.id
````

## → Calls
- [[IN-Program.id]]
- [[IN-ProgramDatabase._is_better]]
- [[IN-ProgramDatabase.load]]
- [[IN-base_database.Program]]

## ← Called by
_(entry point — nothing in this graph calls it)_
