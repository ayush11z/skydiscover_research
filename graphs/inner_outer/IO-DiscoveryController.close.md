---
name: IO-DiscoveryController.close
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
- [[IO-Evaluator.close]]

## ← Called by
- [[IO-Runner.run]]
