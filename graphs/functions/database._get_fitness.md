---
name: database._get_fitness
description: function in skydiscover/search/openevolve_native/database.py (openevolve)
metadata:
  type: project
---

# database._get_fitness

**File:** `skydiscover/search/openevolve_native/database.py:58`  
**Kind:** function  
**Layer:** #openevolve

## Source
````python
def _get_fitness(
    metrics: Dict[str, Any],
    feature_dimensions: List[str] = (),
) -> float:
    """Fitness score, preferring ``combined_score`` and excluding feature dims."""
    if not metrics:
        return 0.0
    if "combined_score" in metrics:
        try:
            return float(metrics["combined_score"])
        except (ValueError, TypeError):
            pass

    feature_dims = set(feature_dimensions) if feature_dimensions else set()
    fitness_metrics: Dict[str, float] = {}
    for key, value in metrics.items():
        if key not in feature_dims and isinstance(value, (int, float)):
            try:
                fv = float(value)
                if fv == fv:
                    fitness_metrics[key] = fv
            except (ValueError, TypeError, OverflowError):
                continue

    if not fitness_metrics:
        return _safe_numeric_average(metrics)
    return _safe_numeric_average(fitness_metrics)
````

## → Calls
- [[database._safe_numeric_average]]

## ← Called by
- [[OpenEvolveNativeDatabase._calculate_feature_coords]]
- [[OpenEvolveNativeDatabase._cleanup_stale_island_bests]]
- [[OpenEvolveNativeDatabase._enforce_population_limit]]
- [[OpenEvolveNativeDatabase._is_better]]
- [[OpenEvolveNativeDatabase._log_island_status]]
- [[OpenEvolveNativeDatabase._migrate_programs]]
- [[OpenEvolveNativeDatabase._sample_other_context_programs]]
- [[OpenEvolveNativeDatabase._update_archive]]
