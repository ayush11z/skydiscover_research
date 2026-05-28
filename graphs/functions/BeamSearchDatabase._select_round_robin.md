---
name: BeamSearchDatabase._select_round_robin
description: method in skydiscover/search/beam_search/database.py (beam-search)
metadata:
  type: project
---

# BeamSearchDatabase._select_round_robin

**File:** `skydiscover/search/beam_search/database.py:395`  
**Kind:** method  
**Layer:** #beam-search

## Source
````python
    def _select_round_robin(self, candidates: List[Program]) -> Program:
        """
        Select in round-robin order through the beam.

        Ensures all beam members get expanded equally.
        """
        # Sort by score for consistent ordering
        sorted_candidates = sorted(candidates, key=self._get_program_score, reverse=True)

        selected = sorted_candidates[self._rr_index % len(sorted_candidates)]
        self._rr_index += 1

        return selected
````

## → Calls
- [[BeamSearchDatabase._get_program_score]]
- [[base_database.Program]]

## ← Called by
- [[BeamSearchDatabase._select_parent]]
