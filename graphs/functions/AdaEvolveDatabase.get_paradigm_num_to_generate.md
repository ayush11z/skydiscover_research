---
name: AdaEvolveDatabase.get_paradigm_num_to_generate
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase.get_paradigm_num_to_generate

**File:** `skydiscover/search/adaevolve/database.py:2195`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def get_paradigm_num_to_generate(self) -> int:
        """Get the configured number of paradigms to generate."""
        if self.paradigm_tracker is None:
            return 3
        return self.paradigm_tracker.num_paradigms_to_generate
````

## → Calls
- [[ParadigmTracker.from_dict]]
- [[ParadigmTracker.num_paradigms_to_generate]]

## ← Called by
_(entry point — nothing in this graph calls it)_
