---
name: MultiDimensionalAdapter.receive_external_improvement
description: method in skydiscover/search/adaevolve/adaptation.py (adaevolve)
metadata:
  type: project
---

# MultiDimensionalAdapter.receive_external_improvement

**File:** `skydiscover/search/adaevolve/adaptation.py:374`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def receive_external_improvement(self, dim_idx: int, fitness: float) -> float:
        """
        Handle an externally-received improvement (e.g., migration) for a dimension.

        Updates the dimension's best_score and accumulated_signal for correct
        search intensity adaptation, but does NOT update UCB rewards or visits
        since the island didn't earn this improvement.

        Also updates global_best_score if this migration brings a new global best.

        Args:
            dim_idx: Index of the dimension
            fitness: Fitness of the received program

        Returns:
            normalized_delta: The improvement delta (0 if no improvement)
        """
        if dim_idx < 0 or dim_idx >= len(self.states):
            raise ValueError(f"Invalid dimension index: {dim_idx}")

        # Update global best if migration brings new global record
        # (Must be tracked for correct UCB normalization)
        if fitness > self.global_best_score:
            self.global_best_score = fitness

        # Delegate to AdaptiveState - updates best_score and G only
        # UCB stats (visits, rewards) remain unchanged
        return self.states[dim_idx].receive_external_improvement(fitness)
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[AdaEvolveDatabase.add]]
