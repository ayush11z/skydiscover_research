---
name: IN-Evaluator._run_stage
description: method in skydiscover/evaluation/evaluator.py (evaluation)
metadata:
  type: project
---

# Evaluator._run_stage

**File:** `skydiscover/evaluation/evaluator.py:207`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    async def _run_stage(self, func, program_path: str) -> Any:
        """Run a single evaluation function in a thread with timeout."""
        loop = asyncio.get_running_loop()

        return await asyncio.wait_for(
            loop.run_in_executor(None, self._call_with_env, func, program_path),
            timeout=self.config.timeout,
        )
````

## → Calls
- [[IN-Evaluator.__init__]]
- [[IN-Evaluator._call_with_env]]

## ← Called by
- [[IN-Evaluator._cascade_evaluate]]
- [[IN-Evaluator.evaluate_program]]
