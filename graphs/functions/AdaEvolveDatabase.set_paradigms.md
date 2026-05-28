---
name: AdaEvolveDatabase.set_paradigms
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase.set_paradigms

**File:** `skydiscover/search/adaevolve/database.py:2184`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def set_paradigms(self, paradigms: List[Dict[str, Any]]) -> None:
        """Set new paradigms from generator."""
        if self.paradigm_tracker is not None:
            self.paradigm_tracker.set_paradigms(paradigms, self._global_best_score)
````

## → Calls
- [[AdaEvolveDatabase._get_fitness]]
- [[ParadigmTracker.from_dict]]
- [[ParadigmTracker.set_paradigms]]

## ← Called by
_(entry point — nothing in this graph calls it)_
