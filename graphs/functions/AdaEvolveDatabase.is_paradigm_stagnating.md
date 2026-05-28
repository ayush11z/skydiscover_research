---
name: AdaEvolveDatabase.is_paradigm_stagnating
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase.is_paradigm_stagnating

**File:** `skydiscover/search/adaevolve/database.py:2161`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def is_paradigm_stagnating(self) -> bool:
        """Check if global improvement rate is below threshold for paradigm generation."""
        if self.paradigm_tracker is None:
            return False
        return self.paradigm_tracker.is_paradigm_stagnating()
````

## → Calls
- [[ParadigmTracker.from_dict]]
- [[ParadigmTracker.is_paradigm_stagnating]]

## ← Called by
- [[AdaEvolveDatabase.get_comprehensive_iteration_stats]]
