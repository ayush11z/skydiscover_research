---
name: IO-EvaluationResult.to_dict
description: method in skydiscover/evaluation/evaluation_result.py (evaluation)
metadata:
  type: project
---

# EvaluationResult.to_dict

**File:** `skydiscover/evaluation/evaluation_result.py:18`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    def to_dict(self) -> Dict[str, Any]:
        result = dict(self.metrics)
        if self.artifacts:
            result["artifacts"] = self.artifacts
        return result
````

## → Calls
- [[IO-EvaluationResult.metrics]]

## ← Called by
- [[IO-DiscoveryController._run_iteration]]
