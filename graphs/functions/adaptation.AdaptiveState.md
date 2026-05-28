---
name: adaptation.AdaptiveState
description: class in skydiscover/search/adaevolve/adaptation.py (adaevolve)
metadata:
  type: project
---

# adaptation.AdaptiveState

**File:** `skydiscover/search/adaevolve/adaptation.py:25`  
**Kind:** class  
**Layer:** #adaevolve

## Source
````python
class AdaptiveState:
    """
    Adaptive state for a single search dimension (e.g., an island).

    Tracks accumulated improvement signal (G) and computes search intensity
    based on historical productivity. Uses normalized delta to be scale-invariant.

    Attributes:
        accumulated_signal: G_t - decayed sum of squared normalized improvements
        best_score: Best fitness seen on this dimension
        improvement_count: Number of improvements found
        total_evaluations: Total programs evaluated
        decay: ρ - recency weight for exponential moving average
        epsilon: Numerical stability constant
        intensity_min: Minimum search intensity (more exploitation)
        intensity_max: Maximum search intensity (more exploration)
    """

    accumulated_signal: float = 0.0
    best_score: float = float("-inf")
    improvement_count: int = 0
    total_evaluations: int = 0

    # Hyperparameters
    decay: float = 0.9
    epsilon: float = 1e-8
    intensity_min: float = 0.1
    intensity_max: float = 0.7

````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[AdaEvolveDatabase.__init__]]
- [[AdaEvolveDatabase._expand_to_island_count]]
- [[AdaEvolveDatabase._spawn_island]]
- [[MultiDimensionalAdapter.add_dimension]]
- [[adaptation.MultiDimensionalAdapter]]
