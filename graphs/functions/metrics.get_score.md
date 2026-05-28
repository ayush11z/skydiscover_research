---
name: metrics.get_score
description: function in skydiscover/utils/metrics.py (utils)
metadata:
  type: project
---

# metrics.get_score

**File:** `skydiscover/utils/metrics.py:19`  
**Kind:** function  
**Layer:** #utils

## Source
````python
def get_score(metrics: Dict[str, Any]) -> float:
    """Return combined_score if available, otherwise average of all numeric metric values."""
    if not metrics:
        return 0.0
    if "combined_score" in metrics:
        try:
            return float(metrics["combined_score"])
        except (ValueError, TypeError):
            pass
    numeric_values = [v for v in metrics.values() if is_numeric_metric(v)]
    return sum(numeric_values) / len(numeric_values) if numeric_values else 0.0
````

## → Calls
- [[metrics.is_numeric_metric]]

## ← Called by
- [[GEPANativeContextBuilder._format_rejection_history]]
- [[GEPANativeController._acceptance_gate]]
- [[GEPANativeController._attempt_merge]]
- [[GEPANativeController._build_merge_prompt]]
- [[GEPANativeController._build_prompt]]
- [[GEPANativeController.run_discovery]]
- [[GEPANativeDatabase._rebuild_elite_pool]]
- [[GEPANativeDatabase._select_parent_pareto]]
- [[GEPANativeDatabase.add]]
- [[ProgramDatabase._is_better]]
- [[ProgramDatabase.get_best_program]]
- [[ProgramDatabase.get_top_programs]]
- [[Runner._add_initial_program]]
- [[Runner.initial_score]]
- [[api._run_discovery_async]]
- [[metrics.compute_proxy_score]]
