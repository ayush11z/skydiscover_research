---
name: ContainerizedEvaluator.__del__
description: method in skydiscover/evaluation/container_evaluator.py (evaluation)
metadata:
  type: project
---

# ContainerizedEvaluator.__del__

**File:** `skydiscover/evaluation/container_evaluator.py:121`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    def __del__(self):
        """Safety net: stop the container if close() was never called."""
        try:
            self.close()
        except Exception:
            pass
````

## → Calls
- [[ContainerizedEvaluator.close]]

## ← Called by
_(entry point — nothing in this graph calls it)_
