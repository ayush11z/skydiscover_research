---
name: IN-DiscoveryController.close
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
- [[IN-Evaluator.close]]

## ← Called by
_(entry point — nothing in this graph calls it)_
