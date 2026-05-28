---
name: IN-ProgramDatabase.load
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
- [[IN-ProgramDatabase.log_status]]

## ← Called by
- [[IN-ProgramDatabase.__init__]]
- [[IN-ProgramDatabase._update_best_program]]
- [[IN-ProgramDatabase.get_best_program]]
- [[IN-ProgramDatabase.get_statistics]]
- [[IN-ProgramDatabase.get_top_programs]]
- [[IN-ProgramDatabase.log_status]]
- [[IN-ProgramDatabase.save]]
