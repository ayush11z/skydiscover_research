---
name: MultiDimensionalAdapter.record_evaluation
description: method in skydiscover/search/adaevolve/adaptation.py (adaevolve)
metadata:
  type: project
---

# MultiDimensionalAdapter.record_evaluation

**File:** `skydiscover/search/adaevolve/adaptation.py:318`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def record_evaluation(self, dim_idx: int, fitness: float) -> float:
        """
        Record an evaluation for a dimension.

        Updates both the dimension's AdaptiveState and the UCB rewards.

        KEY: Two different normalizations:
        1. AdaptiveState uses LOCAL best → search intensity adaptation
        2. UCB rewards use GLOBAL best → fair cross-island comparison

        This fixes "Poor Island Bias" where trash islands with high local
        percentage gains would dominate UCB over globally productive islands.

        Args:
            dim_idx: Index of the dimension
            fitness: Fitness of the evaluated program

        Returns:
            local_normalized_delta: The locally-normalized improvement (for search intensity)
        """
        if dim_idx < 0 or dim_idx >= len(self.states):
            raise ValueError(f"Invalid dimension index: {dim_idx}")

        # Get local best BEFORE update (needed for global UCB reward calculation)
        local_best_before = self.states[dim_idx].best_score

        # Update adaptive state with LOCAL normalization (for search intensity)
        # This returns locally-normalized delta
        local_normalized_delta = self.states[dim_idx].record_evaluation(fitness)

        # Update raw visit count (for exploration bonus)
        self.dimension_visits[dim_idx] += 1

        # Update DECAYED visits: V_t = ρ * V_{t-1} + 1
        self.decayed_visits[dim_idx] = self.decay * self.decayed_visits[dim_idx] + 1.0

        # Calculate GLOBAL-normalized delta for UCB rewards
        # This ensures fair comparison: a 10-point improvement is valued
        # equally whether from a high-fitness or low-fitness island
        if fitness > local_best_before:
            raw_delta = fitness - local_best_before
            global_normalized_delta = self._normalize_by_global(raw_delta)

            # Update global best if this is a new global record
            if fitness > self.global_best_score:
                self.global_best_score = fitness
        else:
            global_normalized_delta = 0.0

        # Update UCB rewards with GLOBAL-normalized delta and DECAY
        self.dimension_rewards[dim_idx] = (
            self.decay * self.dimension_rewards[dim_idx] + global_normalized_delta
        )

        return local_normalized_delta
````

## → Calls
- [[MultiDimensionalAdapter._normalize_by_global]]

## ← Called by
- [[AdaEvolveDatabase.add]]
