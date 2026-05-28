---
name: ParadigmTracker._try_rotate_paradigm
description: method in skydiscover/search/adaevolve/paradigm/tracker.py (adaevolve)
metadata:
  type: project
---

# ParadigmTracker._try_rotate_paradigm

**File:** `skydiscover/search/adaevolve/paradigm/tracker.py:212`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _try_rotate_paradigm(self) -> bool:
        """
        Try to rotate to the next available paradigm.

        Returns:
            True if rotation successful, False if all paradigms exhausted.
        """
        if not self.active_paradigms:
            return False

        # Look for a paradigm that isn't exhausted
        for i in range(len(self.active_paradigms)):
            next_idx = (self.current_paradigm_index + 1 + i) % len(self.active_paradigms)
            if self.paradigm_usage_counts.get(next_idx, 0) < self.max_paradigm_uses:
                self.current_paradigm_index = next_idx
                logger.debug(f"Rotated to paradigm {next_idx}")
                return True

        # All paradigms exhausted
        logger.info("All paradigms exhausted, will archive on next check")
        return False
````

## → Calls
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]

## ← Called by
- [[ParadigmTracker.has_active_paradigm]]
- [[ParadigmTracker.use_paradigm]]
