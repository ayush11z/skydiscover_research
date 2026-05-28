---
name: ParadigmTracker.is_paradigm_stagnating
description: method in skydiscover/search/adaevolve/paradigm/tracker.py (adaevolve)
metadata:
  type: project
---

# ParadigmTracker.is_paradigm_stagnating

**File:** `skydiscover/search/adaevolve/paradigm/tracker.py:93`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def is_paradigm_stagnating(self) -> bool:
        """
        Check if improvement rate is below threshold.

        Paradigm stagnation requires:
        1. Enough history (at least window_size iterations)
        2. Improvement rate below threshold
        3. No active paradigms currently available

        Returns:
            True if paradigm generation should be triggered.
        """
        # Need enough data to make a judgment
        if len(self.improvement_history) < self.window_size:
            return False

        # If we have active paradigms still available, use them first
        if self.has_active_paradigm():
            return False

        # Check improvement rate against threshold
        return self.get_improvement_rate() < self.improvement_threshold
````

## → Calls
- [[ParadigmTracker.get_improvement_rate]]
- [[ParadigmTracker.has_active_paradigm]]

## ← Called by
- [[AdaEvolveDatabase.get_comprehensive_iteration_stats]]
- [[AdaEvolveDatabase.is_paradigm_stagnating]]
