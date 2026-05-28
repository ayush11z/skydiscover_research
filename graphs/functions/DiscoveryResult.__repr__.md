---
name: DiscoveryResult.__repr__
description: method in skydiscover/api.py (api)
metadata:
  type: project
---

# DiscoveryResult.__repr__

**File:** `skydiscover/api.py:53`  
**Kind:** method  
**Layer:** #api

## Source
````python
    def __repr__(self) -> str:
        init = f"{self.initial_score:.4f}" if self.initial_score is not None else "N/A"
        return f"DiscoveryResult(best_score={self.best_score:.4f}, initial_score={init})"
````

## → Calls
- [[DiscoveryResult.best_score]]

## ← Called by
_(entry point — nothing in this graph calls it)_
