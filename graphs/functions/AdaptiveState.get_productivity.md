---
name: AdaptiveState.get_productivity
description: method in skydiscover/search/adaevolve/adaptation.py (adaevolve)
metadata:
  type: project
---

# AdaptiveState.get_productivity

**File:** `skydiscover/search/adaevolve/adaptation.py:173`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def get_productivity(self) -> float:
        """
        Get productivity metric for this dimension.

        Returns:
            Float representing improvement rate (improvements / evaluations)
        """
        if self.total_evaluations == 0:
            return 0.0
        return self.improvement_count / self.total_evaluations
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
_(entry point — nothing in this graph calls it)_
