---
name: AdaEvolveDatabase.get_current_paradigm
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase.get_current_paradigm

**File:** `skydiscover/search/adaevolve/database.py:2173`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def get_current_paradigm(self) -> Optional[Dict[str, Any]]:
        """Get the current active paradigm if available."""
        if self.paradigm_tracker is None:
            return None
        return self.paradigm_tracker.get_current_paradigm()
````

## → Calls
- [[ParadigmTracker.from_dict]]
- [[ParadigmTracker.get_current_paradigm]]

## ← Called by
- [[AdaEvolveDatabase.get_comprehensive_iteration_stats]]
