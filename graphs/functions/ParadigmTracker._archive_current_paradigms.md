---
name: ParadigmTracker._archive_current_paradigms
description: method in skydiscover/search/adaevolve/paradigm/tracker.py (adaevolve)
metadata:
  type: project
---

# ParadigmTracker._archive_current_paradigms

**File:** `skydiscover/search/adaevolve/paradigm/tracker.py:234`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _archive_current_paradigms(self) -> None:
        """
        Archive current paradigms to tried list with outcome info.

        Stores each paradigm with its usage count and score improvement
        for potential feedback to the generator.
        """
        if not self.active_paradigms:
            return

        # Calculate improvement achieved during this paradigm batch
        score_improvement = self.best_score_during_paradigm - self.best_score_at_paradigm_gen

        for idx, paradigm in enumerate(self.active_paradigms):
            uses = self.paradigm_usage_counts.get(idx, 0)
            if uses == 0:
                continue  # Don't archive unused paradigms

            archived = {
                **paradigm,
                "uses": uses,
                "starting_score": self.best_score_at_paradigm_gen,
                "ending_score": self.best_score_during_paradigm,
                "score_improvement": score_improvement,
                "outcome": "SUCCESS" if score_improvement > 0.001 else "FAILED",
            }
            self.tried_paradigms.append(archived)

        # Keep tried list bounded
        while len(self.tried_paradigms) > self.max_tried_paradigms:
            self.tried_paradigms.pop(0)

        # Log archived paradigms with outcomes
        if self.active_paradigms:
            logger.info(
                f"Archived {len(self.active_paradigms)} paradigms (improvement: {score_improvement:+.6f}):"
            )
            for idx, paradigm in enumerate(self.active_paradigms):
                uses = self.paradigm_usage_counts.get(idx, 0)
                if uses > 0:
                    outcome = "SUCCESS" if score_improvement > 0.001 else "FAILED"
                    logger.info(f"  [{outcome}] {paradigm.get('idea', 'N/A')} (uses: {uses})")
````

## → Calls
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]

## ← Called by
- [[ParadigmTracker.clear_paradigms]]
- [[ParadigmTracker.set_paradigms]]
