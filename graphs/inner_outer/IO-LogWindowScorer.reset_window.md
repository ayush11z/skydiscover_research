---
name: IO-LogWindowScorer.reset_window
description: method in skydiscover/search/evox/utils/search_scorer.py (evox)
metadata:
  type: project
---

# LogWindowScorer.reset_window

**File:** `skydiscover/search/evox/utils/search_scorer.py:23`  
**Kind:** method  
**Layer:** #evox

## What it does
Clears the score window so a fresh measurement starts for the new search strategy. Called by CoEvolutionController._evolve_search after switching strategies.

## Source
````python
    def reset_window(
        self,
        start_score: Optional[float],
        algorithm_id: Optional[str] = None,
        start_iteration: Optional[int] = None,
    ) -> None:
        self._start_score = float(start_score) if start_score is not None else 0.0
        self._start_iteration = start_iteration
        self._best_scores = []
        if algorithm_id:
            self.algorithm_id = algorithm_id
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-CoEvolutionController._reset_search_window]]
- [[IO-LogWindowScorer.record_step]]
