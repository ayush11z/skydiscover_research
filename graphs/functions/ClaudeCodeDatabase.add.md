---
name: ClaudeCodeDatabase.add
description: method in skydiscover/search/claude_code/database.py (claude-code)
metadata:
  type: project
---

# ClaudeCodeDatabase.add

**File:** `skydiscover/search/claude_code/database.py:11`  
**Kind:** method  
**Layer:** #claude-code

## Source
````python
    def add(self, program: Program, iteration=None, **kwargs) -> str:
        self.programs[program.id] = program
        if iteration is not None:
            self.last_iteration = max(self.last_iteration, iteration)
        if self.config.db_path:
            self._save_program(program)
        self._update_best_program(program)
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
