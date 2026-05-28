---
name: AdaptiveState.record_evaluation
description: method in skydiscover/search/adaevolve/adaptation.py (adaevolve)
metadata:
  type: project
---

# AdaptiveState.record_evaluation

**File:** `skydiscover/search/adaevolve/adaptation.py:84`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def record_evaluation(self, fitness: float) -> float:
        """
        Record a program evaluation and return normalized improvement delta.

        Normalizes delta by current best_score to make the algorithm
        scale-invariant. This prevents G from exploding with large fitness values.

        Args:
            fitness: The fitness of the evaluated program

        Returns:
            normalized_delta: Normalized improvement (0 if no improvement)
        """
        self.total_evaluations += 1

        if fitness > self.best_score:
            raw_delta = fitness - self.best_score
            normalized_delta = self._normalize_delta(raw_delta)

            self.best_score = fitness
            self.improvement_count += 1

            # Update accumulated signal with normalized squared delta
            # G_t = ρ * G_{t-1} + (1 - ρ) * δ²
            self.accumulated_signal = self.decay * self.accumulated_signal + (1 - self.decay) * (
                normalized_delta**2
            )

            return normalized_delta

        return 0.0
````

## → Calls
- [[AdaptiveState._normalize_delta]]

## ← Called by
- [[AdaEvolveDatabase.add_merged_program]]
