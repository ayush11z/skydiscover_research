---
name: ContainerizedEvaluator._run_container
description: method in skydiscover/evaluation/container_evaluator.py (evaluation)
metadata:
  type: project
---

# ContainerizedEvaluator._run_container

**File:** `skydiscover/evaluation/container_evaluator.py:201`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    def _run_container(self, program_solution: str, mode: str) -> EvaluationResult:
        """Inject the candidate program and run evaluate.sh inside the container.

        Uses a unique /tmp path per call so concurrent evaluations don't collide.

        Override this method to target a different container interface
        (e.g. Harbor: cp to /solution/, read reward from /logs/verifier/reward.json).
        """
        candidate_path = self._inject_file(program_solution, self.program_suffix)
        try:
            return self._run_single_in_container(candidate_path, mode)
        finally:
            self._remove_file(candidate_path)
````

## → Calls
- [[ContainerizedEvaluator._inject_file]]
- [[ContainerizedEvaluator._remove_file]]
- [[ContainerizedEvaluator._run_single_in_container]]
- [[EvaluatorConfig.file_suffix]]
- [[evaluation_result.EvaluationResult]]

## ← Called by
- [[ContainerizedEvaluator.evaluate_program]]
