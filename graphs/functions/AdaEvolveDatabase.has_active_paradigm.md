---
name: AdaEvolveDatabase.has_active_paradigm
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase.has_active_paradigm

**File:** `skydiscover/search/adaevolve/database.py:2167`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def has_active_paradigm(self) -> bool:
        """Check if there's an active paradigm available."""
        if self.paradigm_tracker is None:
            return False
        return self.paradigm_tracker.has_active_paradigm()
````

## → Calls
- [[ParadigmTracker.from_dict]]
- [[ParadigmTracker.has_active_paradigm]]

## ← Called by
- [[AdaEvolveDatabase.get_comprehensive_iteration_stats]]
