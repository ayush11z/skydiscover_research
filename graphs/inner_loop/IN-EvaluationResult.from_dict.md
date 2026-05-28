---
name: IN-EvaluationResult.from_dict
description: classmethod in skydiscover/evaluation/evaluation_result.py (evaluation)
metadata:
  type: project
---

# EvaluationResult.from_dict

**File:** `skydiscover/evaluation/evaluation_result.py:15`  
**Kind:** classmethod  
**Layer:** #evaluation

## Source
````python
    def from_dict(cls, metrics: Dict[str, float]) -> "EvaluationResult":
        return cls(metrics=metrics)
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IN-Evaluator._normalize_result]]
