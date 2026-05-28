---
name: AdaEvolveContextBuilder._determine_outcome
description: method in skydiscover/context_builder/adaevolve/builder.py (context-builder)
metadata:
  type: project
---

# AdaEvolveContextBuilder._determine_outcome

**File:** `skydiscover/context_builder/adaevolve/builder.py:468`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def _determine_outcome(
        self, program_metrics: Dict[str, Any], parent_metrics: Dict[str, Any]
    ) -> str:
        """Describe attempt outcome using the configured scalar proxy in Pareto mode."""
        if not self._is_multiobjective_enabled():
            return super()._determine_outcome(program_metrics, parent_metrics)

        prog_value = self._get_progress_score(program_metrics)
        parent_value = self._get_progress_score(parent_metrics)
        missing = self._PROGRESS_SCORE_MISSING
        if prog_value == missing or parent_value == missing:
            return "Insufficient metrics for comparison"
        if prog_value > parent_value + 1e-6:
            return "Improvement in Pareto proxy"
        if prog_value < parent_value - 1e-6:
            return "Regression in Pareto proxy"
        return "No change in Pareto proxy"
````

## → Calls
- [[AdaEvolveContextBuilder._get_progress_score]]
- [[AdaEvolveContextBuilder._is_multiobjective_enabled]]
- [[DefaultContextBuilder._determine_outcome]]

## ← Called by
- [[AdaEvolveContextBuilder._format_previous_attempts]]
