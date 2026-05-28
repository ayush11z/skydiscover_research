---
name: metrics.compute_proxy_score
description: function in skydiscover/utils/metrics.py (utils)
metadata:
  type: project
---

# metrics.compute_proxy_score

**File:** `skydiscover/utils/metrics.py:77`  
**Kind:** function  
**Layer:** #utils

## Source
````python
def compute_proxy_score(
    metrics: Dict[str, Any],
    *,
    fitness_key: Optional[str] = None,
    pareto_objectives: Optional[List[str]] = None,
    higher_is_better: Optional[Dict[str, bool]] = None,
) -> float:
    """Compute a scalar proxy score from a metrics dict.

    Implements a single fallback chain used by both the database layer and
    the prompt/context builder:

    1. ``fitness_key`` (normalised via *higher_is_better*)
    2. ``combined_score`` (taken as-is)
    3. Average of normalised *pareto_objectives* values
    4. :func:`get_score` (generic numeric average)

    Returns ``-inf`` when *metrics* is empty so callers can distinguish
    "no data" from "score is zero".
    """
    if not metrics:
        return float("-inf")

    hib = higher_is_better or {}

    if fitness_key is not None:
        normalized = normalize_metric_value(fitness_key, metrics.get(fitness_key), hib)
        if normalized is not None:
            return normalized

    combined_score = metrics.get("combined_score")
    if is_numeric_metric(combined_score):
        return float(combined_score)

    if pareto_objectives:
        objective_values = []
        for objective in pareto_objectives:
            normalized = normalize_metric_value(objective, metrics.get(objective), hib)
            if normalized is not None:
                objective_values.append(normalized)
        if objective_values:
            return sum(objective_values) / len(objective_values)

    return get_score(metrics)
````

## → Calls
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]
- [[metrics.get_score]]
- [[metrics.is_numeric_metric]]
- [[metrics.normalize_metric_value]]

## ← Called by
- [[AdaEvolveContextBuilder._get_progress_score]]
- [[AdaEvolveDatabase._get_multiobjective_proxy_score]]
