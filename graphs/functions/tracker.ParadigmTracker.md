---
name: tracker.ParadigmTracker
description: class in skydiscover/search/adaevolve/paradigm/tracker.py (adaevolve)
metadata:
  type: project
---

# tracker.ParadigmTracker

**File:** `skydiscover/search/adaevolve/paradigm/tracker.py:16`  
**Kind:** class  
**Layer:** #adaevolve

## Source
````python
class ParadigmTracker:
    """
    Tracks improvement history and manages paradigm state.

    Two separate stagnation concepts:
    1. Iteration-based stagnation: iterations_since_improvement > threshold
       -> Handled by existing multi-child generation (per-island)
    2. Improvement-rate stagnation: improvement_rate < threshold over window
       -> Triggers paradigm generation (global, this tracker)

    When both trigger, paradigm guidance is added to the prompt context
    while multi-child can still generate multiple children independently.
    """

    # Configuration (tunable hyperparameters)
    window_size: int = 30
    improvement_threshold: float = 0.05
    max_paradigm_uses: int = 5
    max_tried_paradigms: int = 10
    num_paradigms_to_generate: int = 3

    # Improvement tracking - bounded list of binary values
    improvement_history: List[float] = field(default_factory=list)

    # Active paradigms and usage tracking
    active_paradigms: List[Dict[str, Any]] = field(default_factory=list)
    paradigm_usage_counts: Dict[int, int] = field(default_factory=dict)
    current_paradigm_index: int = 0

    # Previously tried paradigms with outcomes - bounded list
    tried_paradigms: List[Dict[str, Any]] = field(default_factory=list)
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[AdaEvolveDatabase.__init__]]
