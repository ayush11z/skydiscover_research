---
name: SearchStrategyDatabase.add
description: method in skydiscover/search/evox/database/search_strategy_db.py (evox)
metadata:
  type: project
---

# SearchStrategyDatabase.add

**File:** `skydiscover/search/evox/database/search_strategy_db.py:23`  
**Kind:** method  
**Layer:** #evox

## Source
````python
    def add(self, program: SearchStrategy, iteration: Optional[int] = None, **kwargs) -> str:
        """Add a program to the database."""
        self.programs[program.id] = program

        if iteration is not None:
            self.last_iteration = max(self.last_iteration, iteration)

        if self.config.db_path:
            self._save_program(program)

        self._update_best_program(program)

        logger.debug(f"Added program {program.id} to evolve database")
        return program.id
````

## → Calls
- [[CheckpointManager._save_program]]
- [[DiscoveryControllerInput.config]]
- [[Program.id]]
- [[ProgramDatabase._save_program]]
- [[ProgramDatabase._update_best_program]]
- [[base_database.ProgramDatabase]]
- [[search_strategy_db.SearchStrategy]]

## ← Called by
_(entry point — nothing in this graph calls it)_
