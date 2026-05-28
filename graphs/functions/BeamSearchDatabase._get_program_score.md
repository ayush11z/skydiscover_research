---
name: BeamSearchDatabase._get_program_score
description: method in skydiscover/search/beam_search/database.py (beam-search)
metadata:
  type: project
---

# BeamSearchDatabase._get_program_score

**File:** `skydiscover/search/beam_search/database.py:261`  
**Kind:** method  
**Layer:** #beam-search

## Source
````python
    def _get_program_score(self, program: Program) -> float:
        """
        Get the fitness score for a program.

        Uses combined_score if available, otherwise averages all metrics.
        Applies depth penalty if configured.

        Args:
            program: Program to score

        Returns:
            Fitness score (higher is better)
        """
        if not program.metrics:
            return 0.0

        # Get base score
        if "combined_score" in program.metrics:
            score = program.metrics["combined_score"]
        elif "score" in program.metrics:
            score = program.metrics["score"]
        else:
            # Average of all metrics
            values = [v for v in program.metrics.values() if isinstance(v, (int, float))]
            score = sum(values) / len(values) if values else 0.0

        # Apply depth penalty if configured
        if self.depth_penalty > 0 and program.id in self.depth:
            depth = self.depth[program.id]
            score = score * math.exp(-self.depth_penalty * depth)

        return score
````

## → Calls
- [[EvaluationResult.metrics]]
- [[LangFuseTracer.get]]
- [[Program.id]]
- [[Program.metrics]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]
- [[base_database.Program]]

## ← Called by
- [[BeamSearchDatabase._prune_beam]]
- [[BeamSearchDatabase._select_best]]
- [[BeamSearchDatabase._select_diversity_weighted]]
- [[BeamSearchDatabase._select_round_robin]]
- [[BeamSearchDatabase._select_stochastic]]
- [[BeamSearchDatabase.get_beam_programs]]
- [[BeamSearchDatabase.get_unexpanded_beam]]
- [[BeamSearchDatabase.log_status]]
- [[BeamSearchDatabase.sample]]
