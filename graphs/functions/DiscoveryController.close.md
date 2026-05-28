---
name: DiscoveryController.close
description: method in skydiscover/search/default_discovery_controller.py (inner-loop)
metadata:
  type: project
---

# DiscoveryController.close

**File:** `skydiscover/search/default_discovery_controller.py:119`  
**Kind:** method  
**Layer:** #inner-loop

## Source
````python
    def close(self):
        """Release resources held by the evaluator (e.g. Docker containers)."""
        if hasattr(self.evaluator, "close"):
            self.evaluator.close()
````

## → Calls
- [[ContainerizedEvaluator.close]]
- [[Evaluator.close]]
- [[evaluation.create_evaluator]]

## ← Called by
- [[MonitorServer._handle_connection]]
- [[MonitorServer._run_loop]]
- [[Runner.run]]
- [[_make_gepa_evaluator.gepa_evaluator]]
- [[gepa_backend.run]]
