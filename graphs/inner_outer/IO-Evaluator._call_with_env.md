---
name: IO-Evaluator._call_with_env
description: method in skydiscover/evaluation/evaluator.py (evaluation)
metadata:
  type: project
---

# Evaluator._call_with_env

**File:** `skydiscover/evaluation/evaluator.py:234`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    def _call_with_env(self, func, program_path: str) -> Any:
        with self._scoped_env():
            return func(program_path)
````

## → Calls
- [[IO-Evaluator._scoped_env]]

## ← Called by
- [[IO-Evaluator._run_stage]]
