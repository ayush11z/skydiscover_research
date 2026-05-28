---
name: ParadigmTracker.clear_paradigms
description: method in skydiscover/search/adaevolve/paradigm/tracker.py (adaevolve)
metadata:
  type: project
---

# ParadigmTracker.clear_paradigms

**File:** `skydiscover/search/adaevolve/paradigm/tracker.py:195`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def clear_paradigms(self) -> None:
        """
        Clear all active paradigms.

        Called when paradigms are exhausted or if manual reset is needed.
        Archives current paradigms before clearing.
        """
        self._archive_current_paradigms()
        self.active_paradigms = []
        self.paradigm_usage_counts = {}
        self.current_paradigm_index = 0
        logger.debug("Cleared active paradigms")
````

## → Calls
- [[ParadigmTracker._archive_current_paradigms]]

## ← Called by
_(entry point — nothing in this graph calls it)_
