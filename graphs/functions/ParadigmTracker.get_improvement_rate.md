---
name: ParadigmTracker.get_improvement_rate
description: method in skydiscover/search/adaevolve/paradigm/tracker.py (adaevolve)
metadata:
  type: project
---

# ParadigmTracker.get_improvement_rate

**File:** `skydiscover/search/adaevolve/paradigm/tracker.py:78`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def get_improvement_rate(self) -> float:
        """
        Calculate improvement rate over the current window.

        Returns:
            Float in [0.0, 1.0] - fraction of recent iterations that improved.
        """
        if not self.improvement_history:
            return 0.0
        return sum(self.improvement_history) / len(self.improvement_history)
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[AdaEvolveDatabase.get_comprehensive_iteration_stats]]
- [[ParadigmTracker.is_paradigm_stagnating]]
