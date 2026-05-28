---
name: BeamSearchDatabase._solution_distance
description: method in skydiscover/search/beam_search/database.py (beam-search)
metadata:
  type: project
---

# BeamSearchDatabase._solution_distance

**File:** `skydiscover/search/beam_search/database.py:230`  
**Kind:** method  
**Layer:** #beam-search

## Source
````python
    def _solution_distance(self, solution1: str, solution2: str) -> float:
        """
        Calculate normalized distance between two code strings.

        Uses a simple character-level comparison. For production use,
        consider AST-based or embedding-based similarity.

        Returns:
            Distance in [0, 1] where 1 means completely different
        """
        if not solution1 or not solution2:
            return 1.0

        # Simple Jaccard distance on character n-grams
        n = 3

        def get_ngrams(s: str, n: int) -> Set[str]:
            return set(s[i : i + n] for i in range(len(s) - n + 1))

        ngrams1 = get_ngrams(solution1, n)
        ngrams2 = get_ngrams(solution2, n)

        if not ngrams1 and not ngrams2:
            return 0.0

        intersection = len(ngrams1 & ngrams2)
        union = len(ngrams1 | ngrams2)

        similarity = intersection / union if union > 0 else 0
        return 1.0 - similarity
````

## → Calls
- [[_solution_distance.get_ngrams]]

## ← Called by
- [[BeamSearchDatabase._diverse_selection]]
- [[BeamSearchDatabase._select_diversity_weighted]]
