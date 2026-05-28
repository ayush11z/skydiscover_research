---
name: GEPANativeController._should_merge
description: method in skydiscover/search/gepa_native/controller.py (gepa)
metadata:
  type: project
---

# GEPANativeController._should_merge

**File:** `skydiscover/search/gepa_native/controller.py:274`  
**Kind:** method  
**Layer:** #gepa

## Source
````python
    def _should_merge(self) -> bool:
        """Check if a stagnation-triggered merge should be attempted."""
        return (
            self.use_merge
            and self._iterations_without_improvement >= self.merge_after_stagnation
            and self._merge_attempts_used < self.max_merge_attempts
        )
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[GEPANativeController.run_discovery]]
