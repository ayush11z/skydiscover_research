---
name: IO-CoEvolutionController._get_best_score
description: method in skydiscover/search/evox/controller.py (outer-loop)
metadata:
  type: project
---

# CoEvolutionController._get_best_score

**File:** `skydiscover/search/evox/controller.py:530`  
**Kind:** method  
**Layer:** #outer-loop

## Source
````python
    def _get_best_score(self) -> float:
        """Get the current best solution score (combined_score metric)."""

        best = self.database.get_best_program()

        if best and best.metrics:
            score = best.metrics.get("combined_score")
            return float(score) if isinstance(score, (int, float)) else 0.0
        return getattr(self.database, "initial_program_score", None) or 0.0
````

## → Calls
- [[IO-DiscoveryControllerInput.database]]

## ← Called by
- [[IO-CoEvolutionController._assign_search_score]]
- [[IO-CoEvolutionController._record_search_window_step]]
- [[IO-CoEvolutionController._reset_search_window]]
- [[IO-CoEvolutionController._should_evolve_search]]
