---
name: ContainerizedEvaluator.evaluate_batch
description: method in skydiscover/evaluation/container_evaluator.py (evaluation)
metadata:
  type: project
---

# ContainerizedEvaluator.evaluate_batch

**File:** `skydiscover/evaluation/container_evaluator.py:180`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    async def evaluate_batch(
        self,
        programs: List[Tuple[str, str]],
    ) -> List[EvaluationResult]:
        """Evaluate multiple programs concurrently.

        Args:
            programs: List of (solution, program_id) tuples.

        Returns:
            Results in the same order as *programs*.
        """
        return await self.task_pool.gather(
            coros=[self.evaluate_program] * len(programs),
            args_list=list(programs),
        )
````

## → Calls
- [[ContainerizedEvaluator.evaluate_program]]
- [[TaskPool.gather]]
- [[evaluation_result.EvaluationResult]]

## ← Called by
_(entry point — nothing in this graph calls it)_
