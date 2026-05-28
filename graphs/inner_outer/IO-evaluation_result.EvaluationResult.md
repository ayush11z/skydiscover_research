---
name: IO-evaluation_result.EvaluationResult
description: class in skydiscover/evaluation/evaluation_result.py (evaluation)
metadata:
  type: project
---

# evaluation_result.EvaluationResult

**File:** `skydiscover/evaluation/evaluation_result.py:6`  
**Kind:** class  
**Layer:** #evaluation

## Source
````python
class EvaluationResult:
    """
    Result of program evaluation containing both metrics and optional artifacts
    """

    metrics: Dict[str, float]
    artifacts: Dict[str, Union[str, bytes]] = field(default_factory=dict)

    @classmethod
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-Evaluator._cascade_evaluate]]
- [[IO-Evaluator._normalize_result]]
- [[IO-Evaluator.evaluate_batch]]
- [[IO-Evaluator.evaluate_program]]
