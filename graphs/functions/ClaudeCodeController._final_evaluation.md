---
name: ClaudeCodeController._final_evaluation
description: method in skydiscover/search/claude_code/controller.py (claude-code)
metadata:
  type: project
---

# ClaudeCodeController._final_evaluation

**File:** `skydiscover/search/claude_code/controller.py:547`  
**Kind:** method  
**Layer:** #claude-code

## Source
````python
    async def _final_evaluation(
        self, solution_path: Path, initial_code: str, initial: Optional[Program]
    ):
        """Evaluate the final solution, falling back to the best checkpoint."""

        class _FinalResult:
            __slots__ = ("solution", "er", "source")

            def __init__(self, solution, er, source):
                self.solution = solution
                self.er = er
                self.source = source

        try:
            final_code = solution_path.read_text()
        except OSError:
            final_code = initial_code
        if not final_code.strip():
            final_code = initial_code

        # Try evaluating the last solution Claude wrote.
        try:
            er = await self.evaluator.evaluate_program(final_code, str(uuid.uuid4()))
            if er.metrics.get("timeout") or er.metrics.get("combined_score") is None:
                raise ValueError("Final eval timed out or returned no score")
            return _FinalResult(final_code, er, "final_eval")
        except Exception as e:
            logger.warning(f"Final eval failed ({e}), re-evaluating best checkpoint code")

        # Fall back to re-evaluating the best checkpoint's code.
        best = self.database.get_best_program()
        if best and best.solution and best.solution.strip():
            try:
                er = await self.evaluator.evaluate_program(best.solution, str(uuid.uuid4()))
                return _FinalResult(best.solution, er, "best_program_reeval")
            except Exception as e2:
                logger.warning(f"Best program re-eval also failed ({e2})")

        return _FinalResult(final_code, _EMPTY_RESULT, "none")
````

## → Calls
- [[ContainerizedEvaluator.evaluate_program]]
- [[Evaluator.evaluate_program]]
- [[Program.solution]]
- [[ProgramDatabase.get_best_program]]
- [[_FinalResult.__init__]]
- [[_final_evaluation._FinalResult]]
- [[base_database.Program]]
- [[evaluation.create_evaluator]]
- [[evaluation_result.EvaluationResult]]

## ← Called by
- [[ClaudeCodeController.run_discovery]]
