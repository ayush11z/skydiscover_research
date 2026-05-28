---
name: ParadigmTracker.get_previously_tried_ideas
description: method in skydiscover/search/adaevolve/paradigm/tracker.py (adaevolve)
metadata:
  type: project
---

# ParadigmTracker.get_previously_tried_ideas

**File:** `skydiscover/search/adaevolve/paradigm/tracker.py:281`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def get_previously_tried_ideas(self) -> List[str]:
        """
        Get formatted list of previously tried ideas for paradigm generator.

        Provides feedback about what worked and what didn't to help
        the generator avoid repeating failed approaches.

        Returns:
            List of formatted strings describing previous paradigms.
        """
        if not self.tried_paradigms:
            return []

        result = []
        for p in self.tried_paradigms:
            outcome = p.get("outcome", "UNCLEAR")
            approach = p.get("approach_type", "unknown")
            idea = p.get("idea", "unknown")
            improvement = p.get("score_improvement", 0.0)

            # Format: "OUTCOME: approach_type - idea (improvement: +/-X.XXXX)"
            result.append(f"{outcome}: {approach} - {idea} (improvement: {improvement:+.4f})")

        return result
````

## → Calls
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]

## ← Called by
- [[AdaEvolveDatabase.get_previously_tried_ideas]]
