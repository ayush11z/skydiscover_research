---
name: harbor_evaluator.HarborEvaluator
description: class in skydiscover/evaluation/harbor_evaluator.py (evaluation)
metadata:
  type: project
---

# harbor_evaluator.HarborEvaluator

**File:** `skydiscover/evaluation/harbor_evaluator.py:43`  
**Kind:** class  
**Layer:** #evaluation

## Source
````python
class HarborEvaluator(ContainerizedEvaluator):
    """Evaluates programs using the Harbor container protocol.

    Extends ContainerizedEvaluator, overriding only the container interaction
    methods: image building, solution injection, test execution, and reward
    reading.
    """

````

## → Calls
- [[container_evaluator.ContainerizedEvaluator]]

## ← Called by
- [[evaluation.create_evaluator]]
