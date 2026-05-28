---
name: BeamSearchDatabase._diverse_selection
description: method in skydiscover/search/beam_search/database.py (beam-search)
metadata:
  type: project
---

# BeamSearchDatabase._diverse_selection

**File:** `skydiscover/search/beam_search/database.py:176`  
**Kind:** method  
**Layer:** #beam-search

## Source
````python
    def _diverse_selection(self, candidates: List[Tuple[str, Program, float]], k: int) -> List[str]:
        """
        Select k programs balancing fitness and diversity.

        Uses a greedy algorithm that iteratively selects the program
        that maximizes a combination of fitness and minimum distance
        to already selected programs.

        Args:
            candidates: List of (id, program, score) tuples
            k: Number of programs to select

        Returns:
            List of selected program IDs
        """
        if len(candidates) <= k:
            return [c[0] for c in candidates]

        selected = []
        remaining = list(candidates)

        # Always include the best program
        remaining.sort(key=lambda x: x[2], reverse=True)
        selected.append(remaining.pop(0))

        # Greedily add remaining programs
        while len(selected) < k and remaining:
            best_idx = -1
            best_combined_score = -float("inf")

            for i, (pid, prog, score) in enumerate(remaining):
                # Calculate diversity as min distance to selected
                min_diversity = min(
                    self._solution_distance(prog.solution, self.programs[s[0]].solution)
                    for s in selected
                )

                # Normalize score (assume scores are in [0, 1] or similar)
                normalized_score = score

                # Combined score
                combined = (
                    1 - self.diversity_weight
                ) * normalized_score + self.diversity_weight * min_diversity

                if combined > best_combined_score:
                    best_combined_score = combined
                    best_idx = i

            if best_idx >= 0:
                selected.append(remaining.pop(best_idx))

        return [s[0] for s in selected]
````

## → Calls
- [[BeamSearchDatabase._solution_distance]]
- [[CheckpointManager.load]]
- [[base_database.Program]]

## ← Called by
- [[BeamSearchDatabase._prune_beam]]
