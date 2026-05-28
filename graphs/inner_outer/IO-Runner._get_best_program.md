---
name: IO-Runner._get_best_program
description: method in skydiscover/runner.py (runner)
metadata:
  type: project
---

# Runner._get_best_program

**File:** `skydiscover/runner.py:437`  
**Kind:** method  
**Layer:** #runner

## Source
````python
    def _get_best_program(self) -> Optional[Program]:
        if self.database.best_program_id:
            prog = self.database.get(self.database.best_program_id)
            if prog:
                return prog
        return self.database.get_best_program()
````

## → Calls
- [[IO-base_database.Program]]

## ← Called by
- [[IO-Runner._save_checkpoint]]
- [[IO-Runner.run]]
