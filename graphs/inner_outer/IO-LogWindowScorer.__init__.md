---
name: IO-LogWindowScorer.__init__
description: method in skydiscover/search/evox/utils/search_scorer.py (evox)
metadata:
  type: project
---

# LogWindowScorer.__init__

**File:** `skydiscover/search/evox/utils/search_scorer.py:17`  
**Kind:** method  
**Layer:** #evox

## Source
````python
    def __init__(self, algorithm_id: Optional[str] = None):
        self.algorithm_id = algorithm_id or "unknown"
        self._start_score: Optional[float] = None
        self._start_iteration: Optional[int] = None
        self._best_scores: List[float] = []
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-CoEvolutionController._init_search_evolution_controller]]
- [[IO-LogWindowScorer.record_step]]
