---
name: pareto_utils.select_program_candidate_from_pareto_front
description: function in skydiscover/search/gepa_native/pareto_utils.py (gepa)
metadata:
  type: project
---

# pareto_utils.select_program_candidate_from_pareto_front

**File:** `skydiscover/search/gepa_native/pareto_utils.py:57`  
**Kind:** function  
**Layer:** #gepa

## Source
````python
def select_program_candidate_from_pareto_front(
    pareto_front_programs: Mapping[Any, set],
    scores: Mapping[Any, float],
    rng: random.Random,
):
    new_front = remove_dominated_programs(pareto_front_programs, scores=scores)
    freq = {}
    for front in new_front.values():
        for prog_id in front:
            freq[prog_id] = freq.get(prog_id, 0) + 1
    sampling_list = [prog_id for prog_id, f in freq.items() for _ in range(f)]
    assert len(sampling_list) > 0
    return rng.choice(sampling_list)
````

## → Calls
- [[pareto_utils.remove_dominated_programs]]

## ← Called by
- [[GEPANativeDatabase._select_parent_pareto]]
