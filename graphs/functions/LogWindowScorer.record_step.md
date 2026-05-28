---
name: LogWindowScorer.record_step
description: method in skydiscover/search/evox/utils/search_scorer.py (evox)
metadata:
  type: project
---

# LogWindowScorer.record_step

**File:** `skydiscover/search/evox/utils/search_scorer.py:35`  
**Kind:** method  
**Layer:** #evox

## What it does
Records the best score seen so far into the sliding window buffer. Called once per inner-loop iteration by [[CoEvolutionController.run_discovery]].

## Source
````python
    def record_step(self, best_score: Optional[float]) -> None:
        if self._start_score is None:
            self.reset_window(best_score)
        if best_score is None:
            best_score = self._best_scores[-1] if self._best_scores else self._start_score
        self._best_scores.append(float(best_score))
````

## → Calls
- [[LogWindowScorer.__init__]]
- [[LogWindowScorer.reset_window]]

## ← Called by
- [[CoEvolutionController._record_search_window_step]]
