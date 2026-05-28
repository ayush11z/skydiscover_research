---
name: IN-ProgramDatabase.save
description: method in skydiscover/search/base_database.py (database)
metadata:
  type: project
---

# ProgramDatabase.save

**File:** `skydiscover/search/base_database.py:159`  
**Kind:** method  
**Layer:** #database

## Source
````python
    def save(self, path: Optional[str] = None, iteration: int = 0) -> None:
        """
        Save the database to disk

        Args:
            path: Path to save to (uses config.db_path if None)
            iteration: Current iteration number
        """
        self.checkpoint_manager.save(
            programs=self.programs,
            prompts_by_program=self.prompts_by_program,
            best_program_id=self.best_program_id,
            last_iteration=iteration if iteration is not None else self.last_iteration,
            path=path,
        )
````

## → Calls
- [[IN-ProgramDatabase.load]]

## ← Called by
_(entry point — nothing in this graph calls it)_
