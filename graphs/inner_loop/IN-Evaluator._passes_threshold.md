---
name: IN-Evaluator._passes_threshold
description: method in skydiscover/evaluation/evaluator.py (evaluation)
metadata:
  type: project
---

# Evaluator._passes_threshold

**File:** `skydiscover/evaluation/evaluator.py:310`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    def _passes_threshold(self, metrics: Dict[str, float], threshold: float) -> bool:
        """Check if metrics pass the threshold (combined_score or average)."""
        if not metrics:
            return False

        if "combined_score" in metrics:
            score = metrics["combined_score"]
            if isinstance(score, (int, float)):
                return float(score) >= threshold

        valid = [
            float(v) for k, v in metrics.items() if k != "error" and isinstance(v, (int, float))
        ]
        return (sum(valid) / len(valid)) >= threshold if valid else False
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IN-Evaluator._cascade_evaluate]]
