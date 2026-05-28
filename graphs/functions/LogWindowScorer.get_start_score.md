---
name: LogWindowScorer.get_start_score
description: method in skydiscover/search/evox/utils/search_scorer.py (evox)
metadata:
  type: project
---

# LogWindowScorer.get_start_score

**File:** `skydiscover/search/evox/utils/search_scorer.py:45`  
**Kind:** method  
**Layer:** #evox

## Source
````python
    def get_start_score(self) -> Optional[float]:
        return self._start_score
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[CoEvolutionController._assign_search_score]]
- [[CoEvolutionController._initialize_first_search_program]]
- [[CoEvolutionController._record_search_window_step]]
