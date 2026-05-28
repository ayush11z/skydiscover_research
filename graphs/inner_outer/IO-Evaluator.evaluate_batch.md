---
name: IO-Evaluator.evaluate_batch
description: method in skydiscover/evaluation/evaluator.py (evaluation)
metadata:
  type: project
---

# Evaluator.evaluate_batch

**File:** `skydiscover/evaluation/evaluator.py:179`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    async def evaluate_batch(
        self,
        programs: List[Tuple[str, str]],
    ) -> List[EvaluationResult]:
        """Evaluate multiple programs concurrently.

        Concurrency is bounded by ``max_concurrent`` (passed at init,
        default 4).

        Args:
            programs: List of ``(solution, program_id)`` tuples.

        Returns:
            List of EvaluationResult in the same order as *programs*.
        """
        return await self.task_pool.gather(
            coros=[self.evaluate_program] * len(programs),
            args_list=list(programs),
        )
````

## → Calls
- [[IO-Evaluator.evaluate_program]]
- [[IO-evaluation_result.EvaluationResult]]

## ← Called by
_(entry point — nothing in this graph calls it)_
