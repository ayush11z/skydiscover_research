---
name: adaptation.MultiDimensionalAdapter
description: class in skydiscover/search/adaevolve/adaptation.py (adaevolve)
metadata:
  type: project
---

# adaptation.MultiDimensionalAdapter

**File:** `skydiscover/search/adaevolve/adaptation.py:221`  
**Kind:** class  
**Layer:** #adaevolve

## Source
````python
class MultiDimensionalAdapter:
    """
    Manages adaptive state across multiple search dimensions (islands).

    Provides UCB-style selection with DECAYED magnitude rewards.
    This fixes the "breakthrough memory" problem where old breakthroughs
    would dominate island selection forever.

    KEY DESIGN: Two different normalizations for two different purposes:
    1. Search Intensity (per-island): Uses LOCAL best for scale-invariant adaptation
    2. UCB Rewards (cross-island): Uses GLOBAL best for fair comparison

    This fixes the "Poor Island Bias" where trash islands with high percentage
    gains would dominate UCB over productive islands with globally valuable
    improvements.

    Attributes:
        states: List of AdaptiveState for each dimension
        dimension_visits: Raw visit count per dimension (for exploration bonus)
        dimension_rewards: Decayed cumulative rewards per dimension (GLOBAL normalized)
        decayed_visits: Decayed visit count per dimension (for reward average)
        global_best_score: Best fitness seen across ALL dimensions (for UCB normalization)
        ucb_exploration: Exploration constant for UCB (√2 is classic)
        min_visits: Minimum visits before UCB kicks in
        decay: Decay factor for rewards (same as AdaptiveState)
        epsilon: Numerical stability constant

    Note on decayed_visits:
        Both rewards and visits must decay at the same rate for reward_avg
        to remain meaningful. Without decayed visits:
            reward_avg = (decaying_sum) / (growing_count) → 0 as visits grow
````

## → Calls
- [[adaptation.AdaptiveState]]

## ← Called by
- [[AdaEvolveDatabase.__init__]]
- [[AdaEvolveDatabase.get_comprehensive_iteration_stats]]
