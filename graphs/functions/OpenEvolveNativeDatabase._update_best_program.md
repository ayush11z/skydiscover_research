---
name: OpenEvolveNativeDatabase._update_best_program
description: method in skydiscover/search/openevolve_native/database.py (openevolve)
metadata:
  type: project
---

# OpenEvolveNativeDatabase._update_best_program

**File:** `skydiscover/search/openevolve_native/database.py:653`  
**Kind:** method  
**Layer:** #openevolve

## Source
````python
    def _update_best_program(self, program: Program) -> None:
        if self.best_program_id is None:
            self.best_program_id = program.id
            return
        if self.best_program_id not in self.programs:
            self.best_program_id = program.id
            return
        current_best = self.programs[self.best_program_id]
        if self._is_better(program, current_best):
            old_id = self.best_program_id
            self.best_program_id = program.id
            if "combined_score" in program.metrics and "combined_score" in current_best.metrics:
                logger.info(
                    "New best program %s replaces %s (%.4f -> %.4f)",
                    program.id,
                    old_id,
                    current_best.metrics["combined_score"],
                    program.metrics["combined_score"],
                )
````

## → Calls
- [[CheckpointManager.load]]
- [[EvaluationResult.metrics]]
- [[OpenEvolveNativeDatabase._is_better]]
- [[Program.id]]
- [[Program.metrics]]
- [[base_database.Program]]

## ← Called by
- [[OpenEvolveNativeDatabase.add]]
