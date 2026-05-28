---
name: AdaEvolveDatabase.get_previously_tried_ideas
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase.get_previously_tried_ideas

**File:** `skydiscover/search/adaevolve/database.py:2189`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def get_previously_tried_ideas(self) -> List[str]:
        """Get formatted list of previously tried paradigm ideas."""
        if self.paradigm_tracker is None:
            return []
        return self.paradigm_tracker.get_previously_tried_ideas()
````

## → Calls
- [[ParadigmTracker.from_dict]]
- [[ParadigmTracker.get_previously_tried_ideas]]

## ← Called by
_(entry point — nothing in this graph calls it)_
