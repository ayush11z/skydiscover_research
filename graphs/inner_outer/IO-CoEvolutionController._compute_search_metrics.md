---
name: IO-CoEvolutionController._compute_search_metrics
description: method in skydiscover/search/evox/controller.py (outer-loop)
metadata:
  type: project
---

# CoEvolutionController._compute_search_metrics

**File:** `skydiscover/search/evox/controller.py:552`  
**Kind:** method  
**Layer:** #outer-loop

## Source
````python
    def _compute_search_metrics(
        self,
        start_score: Optional[float] = None,
        best_scores: Optional[List[float]] = None,
        horizon: Optional[int] = None,
        start_iteration: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Compute scoring metrics using the configured scorer."""

        return self.search_scorer.compute_metrics(
            start_score=start_score,
            best_scores=best_scores,
            horizon=horizon,
            total_iterations=self._max_solution_iterations,
            start_iteration=start_iteration,
        )
````

## → Calls
- [[IO-LogWindowScorer.compute_metrics]]

## ← Called by
- [[IO-CoEvolutionController._assign_search_score]]
- [[IO-CoEvolutionController._initialize_first_search_program]]
