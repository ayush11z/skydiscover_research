---
name: Evaluator.close
description: method in skydiscover/evaluation/evaluator.py (evaluation)
metadata:
  type: project
---

# Evaluator.close

**File:** `skydiscover/evaluation/evaluator.py:199`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    def close(self) -> None:
        """Remove the dynamically loaded evaluation module from sys.modules."""
        sys.modules.pop(getattr(self, "_module_name", None), None)
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[DiscoveryController.close]]
- [[MonitorServer._handle_connection]]
- [[MonitorServer._run_loop]]
- [[Runner.run]]
- [[_make_gepa_evaluator.gepa_evaluator]]
- [[gepa_backend.run]]
