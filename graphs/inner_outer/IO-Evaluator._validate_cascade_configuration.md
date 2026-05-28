---
name: IO-Evaluator._validate_cascade_configuration
description: method in skydiscover/evaluation/evaluator.py (evaluation)
metadata:
  type: project
---

# Evaluator._validate_cascade_configuration

**File:** `skydiscover/evaluation/evaluator.py:83`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    def _validate_cascade_configuration(self, module) -> None:
        if not self.config.cascade_evaluation:
            return
        if not hasattr(module, "evaluate_stage1"):
            logger.warning(
                f"cascade_evaluation is true but {self.evaluation_file} has no evaluate_stage1 — will fall back to direct evaluation"
            )
        elif not hasattr(module, "evaluate_stage2"):
            logger.warning(f"{self.evaluation_file} has evaluate_stage1 but no evaluate_stage2")
````

## → Calls
- [[IO-Evaluator.__init__]]

## ← Called by
- [[IO-Evaluator._load_evaluation_function]]
