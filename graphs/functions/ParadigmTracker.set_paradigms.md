---
name: ParadigmTracker.set_paradigms
description: method in skydiscover/search/adaevolve/paradigm/tracker.py (adaevolve)
metadata:
  type: project
---

# ParadigmTracker.set_paradigms

**File:** `skydiscover/search/adaevolve/paradigm/tracker.py:173`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def set_paradigms(self, paradigms: List[Dict[str, Any]], current_best_score: float) -> None:
        """
        Set new paradigms from generator.

        Archives current paradigms with outcome data, then sets new batch.

        Args:
            paradigms: List of paradigm dicts from generator
            current_best_score: Best score at time of generation
        """
        # Archive current paradigms with their outcomes
        self._archive_current_paradigms()

        # Set new paradigms
        self.active_paradigms = paradigms
        self.paradigm_usage_counts = {}
        self.current_paradigm_index = 0
        self.best_score_at_paradigm_gen = current_best_score
        self.best_score_during_paradigm = current_best_score

        logger.info(f"Set {len(paradigms)} new paradigms (best score: {current_best_score:.6f})")
````

## → Calls
- [[ParadigmTracker._archive_current_paradigms]]

## ← Called by
- [[AdaEvolveDatabase.set_paradigms]]
