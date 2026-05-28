---
name: UnifiedArchive._novelty_to_percentile
description: method in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# UnifiedArchive._novelty_to_percentile

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:379`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _novelty_to_percentile(self, novelty: float) -> float:
        """Convert novelty score to percentile based on archive."""
        if not self._novelty_scores:
            return 0.5

        all_novelties = list(self._novelty_scores.values())
        lower_count = sum(1 for n in all_novelties if n < novelty)
        return lower_count / max(len(all_novelties), 1)
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[UnifiedArchive._compute_elite_score]]
