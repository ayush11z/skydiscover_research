---
name: ProgramDatabase.load
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
- [[CheckpointManager.load]]
- [[ProgramDatabase.log_status]]

## ← Called by
- [[AdaEvolveDatabase.load]]
- [[AgenticGenerator._call_llm]]
- [[BeamSearchDatabase.load]]
- [[CheckpointManager.load]]
- [[GEPANativeDatabase.load]]
- [[OpenEvolveNativeDatabase.add]]
- [[OpenEvolveNativeDatabase.load]]
- [[ProgramDatabase.__init__]]
- [[coevolve_logging.log_active_algorithm]]
- [[coevolve_logging.log_failed_attempt]]
- [[coevolve_logging.update_saved_search_algorithm_score]]
- [[variation_operator_generator.get_available_packages]]
- [[viewer.load_programs]]
