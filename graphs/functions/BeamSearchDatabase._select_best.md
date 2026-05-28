---
name: BeamSearchDatabase._select_best
description: method in skydiscover/search/beam_search/database.py (beam-search)
metadata:
  type: project
---

# BeamSearchDatabase._select_best

**File:** `skydiscover/search/beam_search/database.py:361`  
**Kind:** method  
**Layer:** #beam-search

## Source
````python
    def _select_best(self, candidates: List[Program]) -> Program:
        """Select the highest scoring program."""
        return max(candidates, key=self._get_program_score)
````

## → Calls
- [[BeamSearchDatabase._get_program_score]]
- [[base_database.Program]]

## ← Called by
- [[BeamSearchDatabase._select_parent]]
- [[BeamSearchDatabase._select_stochastic]]
