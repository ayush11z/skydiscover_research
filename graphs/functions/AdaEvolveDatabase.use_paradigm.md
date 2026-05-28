---
name: AdaEvolveDatabase.use_paradigm
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase.use_paradigm

**File:** `skydiscover/search/adaevolve/database.py:2179`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def use_paradigm(self) -> None:
        """Record one use of the current paradigm."""
        if self.paradigm_tracker is not None:
            self.paradigm_tracker.use_paradigm()
````

## → Calls
- [[ParadigmTracker.from_dict]]
- [[ParadigmTracker.use_paradigm]]

## ← Called by
_(entry point — nothing in this graph calls it)_
