---
name: IO-CoEvolutionController._assign_search_score
description: method in skydiscover/search/evox/controller.py (outer-loop)
metadata:
  type: project
---

# CoEvolutionController._assign_search_score

**File:** `skydiscover/search/evox/controller.py:580`  
**Kind:** method  
**Layer:** #outer-loop

## What it does
Asks LogWindowScorer.get_score for the improvement metric over the last window, then attaches it to the pending search result as `metrics["combined_score"]`.

## Source
````python
    def _assign_search_score(self) -> bool:
        """Assign score to pending search algorithm. Returns True if new best."""
        if not self._pending_search_result:
            return False

        if self.search_scorer.get_window_size() > 0:
            metrics = self._compute_search_metrics(horizon=self._switch_interval)
        else:
            start = self.search_scorer.get_start_score() or 0.0
            metrics = self._compute_search_metrics(
                start_score=start,
                best_scores=[self._get_best_score()],
                horizon=self._switch_interval,
            )

        score = float(metrics.get("combined_score", 0.0) or 0.0)

        child_dict = self._pending_search_result.child_program_dict or {}
        child_dict.setdefault("metrics", {}).update(metrics)
        child_dict.setdefault("metadata", {})["end_db_stats"] = make_json_serializable(
            self.database.get_statistics(improvement_threshold=self.DEFAULT_IMPROVEMENT_THRESHOLD)
        )
        self._pending_search_result.child_program_dict = child_dict

        is_new_best = self._best_search_score is not None and score > self._best_search_score
        if is_new_best:
            logger.info(
                f"New best search score: {score:.6f} (+{score - self._best_search_score:.6f})"
            )
        if is_new_best or self._best_search_score is None:
            self._best_search_score = score
        return is_new_best
````

## → Calls
- [[IO-CoEvolutionController._compute_search_metrics]]
- [[IO-CoEvolutionController._get_best_score]]
- [[IO-CoEvolutionController._restore_fallback_database]]
- [[IO-LangFuseTracer.get]]
- [[IO-LogWindowScorer.get_start_score]]
- [[IO-LogWindowScorer.get_window_size]]
- [[IO-coevolve_logging.make_json_serializable]]

## ← Called by
- [[IO-CoEvolutionController._finalize_pending_search]]
