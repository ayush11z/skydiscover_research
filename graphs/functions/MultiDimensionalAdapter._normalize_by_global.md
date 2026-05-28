---
name: MultiDimensionalAdapter._normalize_by_global
description: method in skydiscover/search/adaevolve/adaptation.py (adaevolve)
metadata:
  type: project
---

# MultiDimensionalAdapter._normalize_by_global

**File:** `skydiscover/search/adaevolve/adaptation.py:290`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _normalize_by_global(self, raw_delta: float) -> float:
        """
        Normalize improvement delta by GLOBAL best score for UCB rewards.

        This ensures fair comparison across islands - a 10-point improvement
        is valued the same whether it comes from a high-fitness or low-fitness
        island.

        Args:
            raw_delta: The raw improvement (fitness - old_best)

        Returns:
            Normalized delta using global best, capped at 1.0
        """
        if raw_delta <= 0:
            return 0.0

        # Handle first evaluation where global_best is -inf
        if math.isinf(self.global_best_score):
            return 1.0  # First improvement is always "significant"

        # Safe normalization using global best
        denominator = abs(self.global_best_score) + self.epsilon
        normalized = raw_delta / denominator

        # Cap at 1.0 to prevent extreme values
        return min(normalized, 1.0)
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[MultiDimensionalAdapter.record_evaluation]]
