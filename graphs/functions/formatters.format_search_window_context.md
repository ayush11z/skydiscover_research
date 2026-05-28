---
name: formatters.format_search_window_context
description: function in skydiscover/context_builder/evox/formatters.py (context-builder)
metadata:
  type: project
---

# formatters.format_search_window_context

**File:** `skydiscover/context_builder/evox/formatters.py:421`  
**Kind:** function  
**Layer:** #context-builder

## Source
````python
def format_search_window_context(context: Dict[str, Any]) -> str:
    """Format the current search window context from context['search_stats']."""
    stats = context.get("search_stats") or {}
    window_start = int(stats.get("window_start_iteration") or 0)
    total = int(stats.get("total_iterations") or 100)
    horizon = int(stats.get("search_window_horizon", 0))
    improvement_threshold = float(stats.get("improvement_threshold") or 0.0)

    lines = []

    window_line = f"- Your newly designed search algorithm will start at iteration {window_start} out of {total}."
    if horizon > 0:
        if improvement_threshold > 0:
            window_line += f" It will run for at least {horizon} iterations (potentially more if improving), but will be cut to just {horizon} iterations if it fails to improve the solution score by more than {improvement_threshold:.4f}."
        else:
            window_line += f" It will run for at least {horizon} iterations (potentially more if improving), but will be cut to just {horizon} iterations if it fails to improve the solution score."
    lines.append(window_line)

    if improvement_threshold > 0:
        lines.append(
            f"- If your algorithm fails to improve the solution score by more than {improvement_threshold:.4f} during this window, it will be replaced."
        )
    else:
        lines.append(
            "- If your algorithm fails to improve the solution score during this window, it will be replaced."
        )

    lines.append(
        "- Goal: Design a better search strategy (e.g. how to select and manage solution programs) to improve the downstream solution score."
    )
    lines.append(
        "- NOTE: Exactly one program is generated per iteration. Keep the population size in mind when designing your search algorithm."
    )

    return "\n".join(lines)
````

## → Calls
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]

## ← Called by
- [[EvoxContextBuilder.build_prompt]]
