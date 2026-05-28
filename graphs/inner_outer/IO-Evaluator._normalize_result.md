---
name: IO-Evaluator._normalize_result
description: method in skydiscover/evaluation/evaluator.py (evaluation)
metadata:
  type: project
---

# Evaluator._normalize_result

**File:** `skydiscover/evaluation/evaluator.py:238`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    def _normalize_result(self, result: Any) -> EvaluationResult:
        if isinstance(result, EvaluationResult):
            return result
        if isinstance(result, dict):
            return EvaluationResult.from_dict(result)

        logger.warning(f"Unexpected result type: {type(result)}")
        return EvaluationResult(metrics={"error": 0.0})
````

## → Calls
- [[IO-EvaluationResult.from_dict]]
- [[IO-Evaluator.__init__]]
- [[IO-evaluation_result.EvaluationResult]]

## ← Called by
- [[IO-Evaluator._cascade_evaluate]]
- [[IO-Evaluator.evaluate_program]]
