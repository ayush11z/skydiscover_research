---
name: IN-evaluation_result.EvaluationResult
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
- [[IN-Evaluator._cascade_evaluate]]
- [[IN-Evaluator._normalize_result]]
- [[IN-Evaluator.evaluate_batch]]
- [[IN-Evaluator.evaluate_program]]
