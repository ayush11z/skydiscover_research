---
name: ProgramDatabase._is_better
description: method in skydiscover/search/base_database.py (database)
metadata:
  type: project
---

# ProgramDatabase._is_better

**File:** `skydiscover/search/base_database.py:213`  
**Kind:** method  
**Layer:** #database

## Source
````python
    def _is_better(self, program1: Program, program2: Program) -> bool:
        """Determine if program1 has better fitness than program2."""
        if not program1.metrics and not program2.metrics:
            # No evidence either way — keep the current best.
            return False
        if program1.metrics and not program2.metrics:
            return True
        if not program1.metrics and program2.metrics:
            return False
        return get_score(program1.metrics) > get_score(program2.metrics)
````

## → Calls
- [[EvaluationResult.metrics]]
- [[Program.metrics]]
- [[base_database.Program]]
- [[metrics.get_score]]

## ← Called by
- [[ProgramDatabase._update_best_program]]
