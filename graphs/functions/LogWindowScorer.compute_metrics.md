---
name: LogWindowScorer.compute_metrics
description: method in skydiscover/search/evox/utils/search_scorer.py (evox)
metadata:
  type: project
---

# LogWindowScorer.compute_metrics

**File:** `skydiscover/search/evox/utils/search_scorer.py:48`  
**Kind:** method  
**Layer:** #evox

## Source
````python
    def compute_metrics(
        self,
        start_score: Optional[float] = None,
        best_scores: Optional[List[float]] = None,
        horizon: Optional[int] = None,
        start_iteration: Optional[int] = None,
        total_iterations: Optional[int] = None,
    ) -> Dict[str, Any]:
        if start_iteration is None:
            start_iteration = self._start_iteration
        start = float(start_score if start_score is not None else (self._start_score or 0.0))
        scores_to_use = best_scores if best_scores is not None else self._best_scores
        T_obs = len(scores_to_use) if scores_to_use else 0
        horizon_int = int(horizon) if horizon else max(1, T_obs)

        running_best = start
        for s in scores_to_use:
            running_best = max(running_best, float(s))

        improvement = running_best - start
        log_weight = 1.0 + math.log(1.0 + max(0.0, start))
        combined_score = improvement * log_weight / math.sqrt(horizon_int)

        logger.info(
            f"Search strategy score: combined={combined_score:.6f}, "
            f"improvement={improvement:.6f}, start={start:.6f}, "
            f"end={running_best:.6f}, horizon={horizon_int}"
        )

        return {
            "combined_score": combined_score,
            "window_start_iteration": start_iteration,
            "search_window_start_score": start,
            "search_window_end_score": running_best,
            "search_horizon": horizon_int,
        }
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[CoEvolutionController._compute_search_metrics]]
