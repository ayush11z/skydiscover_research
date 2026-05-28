---
name: formatters.filter_db_stats_by_horizon
description: function in skydiscover/context_builder/evox/formatters.py (context-builder)
metadata:
  type: project
---

# formatters.filter_db_stats_by_horizon

**File:** `skydiscover/context_builder/evox/formatters.py:16`  
**Kind:** function  
**Layer:** #context-builder

## Source
````python
def filter_db_stats_by_horizon(db_stats: Dict[str, Any], horizon: int) -> Dict[str, Any]:
    """Filter db_stats to only include the last 'horizon' entries for trajectory fields."""
    if not db_stats or horizon <= 0:
        return db_stats

    filtered = dict(db_stats)
    if recent := db_stats.get("recent_solution_stats"):
        filtered_recent = dict(recent)
        for key in ["execution_trace", "score_trajectory", "parent_scores"]:
            if (val := recent.get(key)) and len(val) > horizon:
                filtered_recent[key] = val[-horizon:]
        filtered_recent["num_recent_iterations"] = min(
            horizon, recent.get("num_recent_iterations", 0)
        )
        filtered["recent_solution_stats"] = filtered_recent
    return filtered
````

## → Calls
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]

## ← Called by
- [[EvoxContextBuilder.build_prompt]]
- [[formatters.prepare_search_algorithms_data]]
