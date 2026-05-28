---
name: BeamSearchDatabase._select_diversity_weighted
description: method in skydiscover/search/beam_search/database.py (beam-search)
metadata:
  type: project
---

# BeamSearchDatabase._select_diversity_weighted

**File:** `skydiscover/search/beam_search/database.py:409`  
**Kind:** method  
**Layer:** #beam-search

## Source
````python
    def _select_diversity_weighted(self, candidates: List[Program]) -> Program:
        """
        Select balancing exploitation (high score) and exploration (diversity).

        Programs that are more different from recently expanded programs
        get a diversity bonus.
        """
        if not self.expanded:
            # No expansion history, use stochastic
            return self._select_stochastic(candidates)

        # Calculate combined scores
        combined_scores = []
        for prog in candidates:
            fitness = self._get_program_score(prog)

            # Calculate diversity from expanded programs
            recent_expanded = list(self.expanded)[-10:]  # Last 10 expanded
            if recent_expanded:
                diversity = sum(
                    self._solution_distance(prog.solution, self.programs[eid].solution)
                    for eid in recent_expanded
                    if eid in self.programs
                ) / len(recent_expanded)
            else:
                diversity = 1.0

            combined = (1 - self.diversity_weight) * fitness + self.diversity_weight * diversity
            combined_scores.append(combined)

        # Select using softmax on combined scores
        if self.temperature > 0:
            max_score = max(combined_scores)
            exp_scores = [math.exp((s - max_score) / self.temperature) for s in combined_scores]
            total = sum(exp_scores)
            probs = [e / total for e in exp_scores]

            r = random.random()
            cumsum = 0
            for i, prob in enumerate(probs):
                cumsum += prob
                if r <= cumsum:
                    return candidates[i]

        # Fallback to best combined score
        best_idx = combined_scores.index(max(combined_scores))
        return candidates[best_idx]
````

## → Calls
- [[BeamSearchDatabase._get_program_score]]
- [[BeamSearchDatabase._select_stochastic]]
- [[BeamSearchDatabase._solution_distance]]
- [[CheckpointManager.load]]
- [[Program.solution]]
- [[base_database.Program]]

## ← Called by
- [[BeamSearchDatabase._select_parent]]
