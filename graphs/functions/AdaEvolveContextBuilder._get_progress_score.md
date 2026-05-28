---
name: AdaEvolveContextBuilder._get_progress_score
description: method in skydiscover/context_builder/adaevolve/builder.py (context-builder)
metadata:
  type: project
---

# AdaEvolveContextBuilder._get_progress_score

**File:** `skydiscover/context_builder/adaevolve/builder.py:77`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def _get_progress_score(self, metrics: Dict[str, Any]) -> float:
        """Scalar proxy used only for prompt-side progress descriptions.

        Returns ``_PROGRESS_SCORE_MISSING`` (``-inf``) for empty/missing metrics
        so that callers can distinguish "no data" from "score is zero".
        """
        db_config = self._db_config()
        pareto_objectives = getattr(db_config, "pareto_objectives", None) or None
        return compute_proxy_score(
            metrics,
            fitness_key=getattr(db_config, "fitness_key", None),
            pareto_objectives=pareto_objectives,
            higher_is_better=getattr(db_config, "higher_is_better", None) or {},
        )
````

## → Calls
- [[AdaEvolveContextBuilder._db_config]]
- [[metrics.compute_proxy_score]]

## ← Called by
- [[AdaEvolveContextBuilder._determine_outcome]]
- [[AdaEvolveContextBuilder._format_previous_attempts]]
- [[AdaEvolveContextBuilder._format_sibling_context]]
- [[AdaEvolveContextBuilder._identify_improvement_areas]]
