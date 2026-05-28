---
name: AdaptiveState.receive_external_improvement
description: method in skydiscover/search/adaevolve/adaptation.py (adaevolve)
metadata:
  type: project
---

# AdaptiveState.receive_external_improvement

**File:** `skydiscover/search/adaevolve/adaptation.py:116`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def receive_external_improvement(self, fitness: float) -> float:
        """
        Handle an externally-received improvement (e.g., migration).

        Updates best_score and accumulated_signal WITHOUT updating counts.
        This ensures:
        1. Future delta calculations use correct baseline
        2. Search intensity drops to exploitation mode for the new solution
        3. UCB stats remain unaffected (island didn't earn the improvement)

        Args:
            fitness: The fitness of the received program

        Returns:
            normalized_delta: The improvement delta (0 if no improvement)
        """
        if fitness <= self.best_score:
            return 0.0

        raw_delta = fitness - self.best_score
        normalized_delta = self._normalize_delta(raw_delta)

        # Update best_score (CRITICAL: fixes future delta calculations)
        self.best_score = fitness

        # Update accumulated_signal (triggers exploitation mode)
        # The island now has a good solution worth refining
        self.accumulated_signal = self.decay * self.accumulated_signal + (1 - self.decay) * (
            normalized_delta**2
        )

        # NOTE: We do NOT update improvement_count or total_evaluations
        # because the island didn't earn this improvement

        return normalized_delta
````

## → Calls
- [[AdaptiveState._normalize_delta]]

## ← Called by
_(entry point — nothing in this graph calls it)_
