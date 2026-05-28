---
name: IO-LogWindowScorer.get_window_size
description: method in skydiscover/search/evox/utils/search_scorer.py (evox)
metadata:
  type: project
---

# LogWindowScorer.get_window_size

**File:** `skydiscover/search/evox/utils/search_scorer.py:42`  
**Kind:** method  
**Layer:** #evox

## Source
````python
    def get_window_size(self) -> int:
        return len(self._best_scores)
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-CoEvolutionController._assign_search_score]]
