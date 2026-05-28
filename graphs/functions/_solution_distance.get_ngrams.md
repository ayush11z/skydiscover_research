---
name: _solution_distance.get_ngrams
description: function in skydiscover/search/beam_search/database.py (beam-search)
metadata:
  type: project
---

# _solution_distance.get_ngrams

**File:** `skydiscover/search/beam_search/database.py:246`  
**Kind:** function  
**Layer:** #beam-search

## Source
````python
        def get_ngrams(s: str, n: int) -> Set[str]:
            return set(s[i : i + n] for i in range(len(s) - n + 1))
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[BeamSearchDatabase._solution_distance]]
