---
name: GEPANativeDatabase._select_parent_pareto
description: method in skydiscover/search/gepa_native/database.py (gepa)
metadata:
  type: project
---

# GEPANativeDatabase._select_parent_pareto

**File:** `skydiscover/search/gepa_native/database.py:327`  
**Kind:** method  
**Layer:** #gepa

## Source
````python
    def _select_parent_pareto(self) -> Program:
        """Frequency-weighted selection from the Pareto front across metrics."""
        if not self.program_at_metric_front or len(self.programs) < 2:
            return self.get_best_program()
        scores = {pid: get_score(prog.metrics) for pid, prog in self.programs.items()}
        try:
            pid = select_program_candidate_from_pareto_front(
                self.program_at_metric_front, scores, self.rng
            )
        except AssertionError:
            return self.get_best_program()
        return self.programs[pid]
````

## → Calls
- [[CheckpointManager.load]]
- [[EvaluationResult.metrics]]
- [[Program.metrics]]
- [[ProgramDatabase.get_best_program]]
- [[base_database.Program]]
- [[metrics.get_score]]
- [[pareto_utils.select_program_candidate_from_pareto_front]]

## ← Called by
- [[GEPANativeDatabase._select_parent]]
