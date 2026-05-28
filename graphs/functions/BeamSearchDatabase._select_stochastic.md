---
name: BeamSearchDatabase._select_stochastic
description: method in skydiscover/search/beam_search/database.py (beam-search)
metadata:
  type: project
---

# BeamSearchDatabase._select_stochastic

**File:** `skydiscover/search/beam_search/database.py:365`  
**Kind:** method  
**Layer:** #beam-search

## Source
````python
    def _select_stochastic(self, candidates: List[Program]) -> Program:
        """
        Select using softmax-weighted random sampling.

        Higher temperature = more uniform distribution.
        Lower temperature = more greedy selection.
        """
        scores = [self._get_program_score(p) for p in candidates]

        # Apply temperature and softmax
        if self.temperature > 0:
            # Shift scores for numerical stability
            max_score = max(scores)
            exp_scores = [math.exp((s - max_score) / self.temperature) for s in scores]
            total = sum(exp_scores)
            probs = [e / total for e in exp_scores]
        else:
            # Temperature = 0 means greedy
            return self._select_best(candidates)

        # Weighted random selection
        r = random.random()
        cumsum = 0
        for i, prob in enumerate(probs):
            cumsum += prob
            if r <= cumsum:
                return candidates[i]

        return candidates[-1]
````

## → Calls
- [[BeamSearchDatabase._get_program_score]]
- [[BeamSearchDatabase._select_best]]
- [[base_database.Program]]

## ← Called by
- [[BeamSearchDatabase._select_diversity_weighted]]
- [[BeamSearchDatabase._select_parent]]
