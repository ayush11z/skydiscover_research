---
name: IO-ProgramDatabase.load
description: method in skydiscover/search/base_database.py (database)
metadata:
  type: project
---

# ProgramDatabase.load

**File:** `skydiscover/search/base_database.py:175`  
**Kind:** method  
**Layer:** #database

## Source
````python
    def load(self, path: str) -> None:
        """
        Load the database from disk

        Args:
            path: Path to load from
        """
        programs, best_id, last_iter = self.checkpoint_manager.load(path)
        self.programs = programs
        self.best_program_id = best_id
        self.last_iteration = last_iter

        self.log_status()
````

## → Calls
- [[IO-ProgramDatabase.log_status]]

## ← Called by
- [[IO-EvolvedProgramDatabase.add]]
- [[IO-EvolvedProgramDatabase.sample]]
- [[IO-ProgramDatabase.__init__]]
- [[IO-ProgramDatabase._update_best_program]]
- [[IO-ProgramDatabase.get_best_program]]
- [[IO-ProgramDatabase.get_statistics]]
- [[IO-ProgramDatabase.get_top_programs]]
- [[IO-ProgramDatabase.log_status]]
- [[IO-ProgramDatabase.save]]
- [[IO-SearchStrategyDatabase.sample]]
