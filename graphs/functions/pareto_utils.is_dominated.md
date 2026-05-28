---
name: pareto_utils.is_dominated
description: function in skydiscover/search/gepa_native/pareto_utils.py (gepa)
metadata:
  type: project
---

# pareto_utils.is_dominated

**File:** `skydiscover/search/gepa_native/pareto_utils.py:8`  
**Kind:** function  
**Layer:** #gepa

## Source
````python
def is_dominated(y, programs, program_at_pareto_front_valset):
    y_fronts = [front for front in program_at_pareto_front_valset.values() if y in front]
    for front in y_fronts:
        found_dominator_in_front = False
        for other_prog in front:
            if other_prog in programs:
                found_dominator_in_front = True
                break
        if not found_dominator_in_front:
            return False
    return True
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[pareto_utils.remove_dominated_programs]]
