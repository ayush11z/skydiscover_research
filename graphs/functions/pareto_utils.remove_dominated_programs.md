---
name: pareto_utils.remove_dominated_programs
description: function in skydiscover/search/gepa_native/pareto_utils.py (gepa)
metadata:
  type: project
---

# pareto_utils.remove_dominated_programs

**File:** `skydiscover/search/gepa_native/pareto_utils.py:21`  
**Kind:** function  
**Layer:** #gepa

## Source
````python
def remove_dominated_programs(program_at_pareto_front_valset, scores=None):
    freq = {}
    for front in program_at_pareto_front_valset.values():
        for p in front:
            freq[p] = freq.get(p, 0) + 1

    dominated = set()
    programs = list(freq.keys())

    if scores is None:
        scores = dict.fromkeys(programs, 1)

    programs = sorted(programs, key=lambda x: scores[x], reverse=False)

    found_to_remove = True
    while found_to_remove:
        found_to_remove = False
        for y in programs:
            if y in dominated:
                continue
            if is_dominated(
                y,
                set(programs).difference({y}).difference(dominated),
                program_at_pareto_front_valset,
            ):
                dominated.add(y)
                found_to_remove = True
                break

    dominators = [p for p in programs if p not in dominated]
    return {
        val_id: {prog_idx for prog_idx in front if prog_idx in dominators}
        for val_id, front in program_at_pareto_front_valset.items()
    }
````

## → Calls
- [[pareto_utils.is_dominated]]

## ← Called by
- [[pareto_utils.select_program_candidate_from_pareto_front]]
