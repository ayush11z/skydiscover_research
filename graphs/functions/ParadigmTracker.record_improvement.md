---
name: ParadigmTracker.record_improvement
description: method in skydiscover/search/adaevolve/paradigm/tracker.py (adaevolve)
metadata:
  type: project
---

# ParadigmTracker.record_improvement

**File:** `skydiscover/search/adaevolve/paradigm/tracker.py:56`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def record_improvement(self, improved: bool, current_best_score: float = 0.0) -> None:
        """
        Record binary improvement (1.0 if global best changed, else 0.0).

        Called after each program is added to the database, after
        _update_best_program() determines if there was improvement.

        Args:
            improved: Whether the global best changed
            current_best_score: Current best score for outcome tracking
        """
        value = 1.0 if improved else 0.0
        self.improvement_history.append(value)

        # Keep bounded to window_size
        while len(self.improvement_history) > self.window_size:
            self.improvement_history.pop(0)

        # Track best score during paradigm usage for outcome evaluation
        if self.active_paradigms and current_best_score > self.best_score_during_paradigm:
            self.best_score_during_paradigm = current_best_score
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[AdaEvolveDatabase.add]]
