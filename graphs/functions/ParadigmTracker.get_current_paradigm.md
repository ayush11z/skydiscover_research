---
name: ParadigmTracker.get_current_paradigm
description: method in skydiscover/search/adaevolve/paradigm/tracker.py (adaevolve)
metadata:
  type: project
---

# ParadigmTracker.get_current_paradigm

**File:** `skydiscover/search/adaevolve/paradigm/tracker.py:133`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def get_current_paradigm(self) -> Optional[Dict[str, Any]]:
        """
        Get the current active paradigm if available.

        Returns:
            Paradigm dict with keys: idea, description, what_to_optimize,
            cautions, approach_type. Returns None if no active paradigm.
        """
        if not self.has_active_paradigm():
            return None

        return self.active_paradigms[self.current_paradigm_index]
````

## → Calls
- [[ParadigmTracker.has_active_paradigm]]

## ← Called by
- [[AdaEvolveDatabase.get_comprehensive_iteration_stats]]
- [[AdaEvolveDatabase.get_current_paradigm]]
