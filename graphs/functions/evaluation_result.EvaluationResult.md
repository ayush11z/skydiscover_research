---
name: evaluation_result.EvaluationResult
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
- [[ClaudeCodeController._final_evaluation]]
- [[ContainerizedEvaluator._parse_output]]
- [[ContainerizedEvaluator._run_container]]
- [[ContainerizedEvaluator._run_single_in_container]]
- [[ContainerizedEvaluator.evaluate_batch]]
- [[ContainerizedEvaluator.evaluate_program]]
- [[Evaluator._cascade_evaluate]]
- [[Evaluator._normalize_result]]
- [[Evaluator.evaluate_batch]]
- [[Evaluator.evaluate_program]]
- [[HarborEvaluator._read_reward]]
- [[HarborEvaluator._run_container]]
- [[LLMJudge.evaluate]]
