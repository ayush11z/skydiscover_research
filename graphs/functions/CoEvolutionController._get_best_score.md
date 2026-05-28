---
name: CoEvolutionController._get_best_score
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
- [[DiscoveryControllerInput.database]]
- [[EvaluationResult.metrics]]
- [[Program.metrics]]
- [[ProgramDatabase.get_best_program]]
- [[SearchConfig.database]]

## ← Called by
- [[CoEvolutionController._assign_search_score]]
- [[CoEvolutionController._record_search_window_step]]
- [[CoEvolutionController._reset_search_window]]
- [[CoEvolutionController._should_evolve_search]]
