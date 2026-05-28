---
name: ParadigmTracker.use_paradigm
description: method in skydiscover/search/adaevolve/paradigm/tracker.py (adaevolve)
metadata:
  type: project
---

# ParadigmTracker.use_paradigm

**File:** `skydiscover/search/adaevolve/paradigm/tracker.py:146`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def use_paradigm(self) -> None:
        """
        Record one use of the current paradigm.

        Called when a child is generated using the paradigm guidance.
        Increments usage counter for round-robin tracking.
        """
        if not self.active_paradigms:
            return

        current_uses = self.paradigm_usage_counts.get(self.current_paradigm_index, 0)
        self.paradigm_usage_counts[self.current_paradigm_index] = current_uses + 1

        # Log paradigm usage with idea
        paradigm = self.active_paradigms[self.current_paradigm_index]
        logger.info(
            f"Using paradigm {self.current_paradigm_index + 1}/{len(self.active_paradigms)} "
            f"({current_uses + 1}/{self.max_paradigm_uses}): {paradigm.get('idea', 'N/A')}"
        )

        # Rotate for next use
        self._try_rotate_paradigm()
````

## → Calls
- [[LangFuseTracer.get]]
- [[ParadigmTracker._try_rotate_paradigm]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]

## ← Called by
- [[AdaEvolveDatabase.use_paradigm]]
