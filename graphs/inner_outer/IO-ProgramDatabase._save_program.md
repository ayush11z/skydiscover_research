---
name: IO-ProgramDatabase._save_program
description: method in skydiscover/search/base_database.py (database)
metadata:
  type: project
---

# ProgramDatabase._save_program

**File:** `skydiscover/search/base_database.py:189`  
**Kind:** method  
**Layer:** #database

## Source
````python
    def _save_program(
        self,
        program: Program,
        base_path: Optional[str] = None,
        prompts: Optional[Dict[str, Dict[str, str]]] = None,
    ) -> None:
        """
        Save a single program to disk.

        This is a convenience method that delegates to CheckpointManager.
        Subclasses should use this method when they need to save individual programs
        (e.g., during add() operations).

        Args:
            program: Program to save
            base_path: Base path to save to (uses config.db_path if None)
            prompts: Optional prompts to save with the program
        """
        self.checkpoint_manager._save_program(program, base_path, prompts)
````

## → Calls
- [[IO-base_database.Program]]

## ← Called by
- [[IO-EvolvedProgramDatabase.add]]
- [[IO-SearchStrategyDatabase.add]]
