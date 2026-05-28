---
name: AdaptiveState._normalize_delta
description: method in skydiscover/search/adaevolve/adaptation.py (adaevolve)
metadata:
  type: project
---

# AdaptiveState._normalize_delta

**File:** `skydiscover/search/adaevolve/adaptation.py:54`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _normalize_delta(self, raw_delta: float) -> float:
        """
        Normalize improvement delta to be scale-invariant.

        Uses abs(best_score) + epsilon to handle:
        - Infinite best_score (first evaluation, best_score = -inf)
        - Zero best_score (start of run)
        - Negative best_score (error minimization tasks)
        - Small positive best_score (prevents explosion)

        Args:
            raw_delta: The raw improvement (fitness - best_score)

        Returns:
            Normalized delta, capped at 1.0 to prevent extreme values
        """
        # Handle first evaluation where best_score is -inf
        # In this case, any finite improvement is significant but we cap it
        if math.isinf(self.best_score):
            return 1.0  # First improvement is always "significant"

        # Safe normalization: handles zero, negative, and small positive values
        # abs() handles negative fitness scales (e.g., error minimization)
        # epsilon prevents division by zero
        denominator = abs(self.best_score) + self.epsilon
        normalized = raw_delta / denominator

        # Cap at 1.0 to prevent extreme values from dominating G
        return min(normalized, 1.0)
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[AdaptiveState.receive_external_improvement]]
- [[AdaptiveState.record_evaluation]]
