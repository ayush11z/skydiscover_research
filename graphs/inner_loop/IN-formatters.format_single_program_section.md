---
name: IN-formatters.format_single_program_section
description: function in skydiscover/context_builder/evox/formatters.py (context-builder)
metadata:
  type: project
---

# formatters.format_single_program_section

**File:** `skydiscover/context_builder/evox/formatters.py:538`  
**Kind:** function  
**Layer:** #context-builder

## Source
````python
def format_single_program_section(
    program: Program, idx: int, language: str, summaries_by_num: Dict[int, str]
) -> List[str]:
    """Format a single program with metrics and solution/summary."""
    solution = prog_attr(program, "solution")
    metrics = prog_attr(program, "metrics", {})

    window_start = int(metrics.get("window_start_iteration", 0))
    horizon = int(metrics.get("search_window_horizon", 0))
    start_score = metrics.get("search_window_start_score", 0.0)
    end_score = metrics.get("search_window_end_score", 0.0)
    combined_score = metrics.get("combined_score", 0.0)

    lines = [
        f"### Program {idx}\n",
        "#### Metrics",
        f"Search Algorithm Score = {combined_score:.4f}",
        f"Ran iterations {window_start} to {window_start + horizon} ({horizon} iterations)",
        f"Score changed: {start_score:.4f} -> {end_score:.4f} (+{end_score - start_score:.4f})",
    ]

    if idx in summaries_by_num:
        lines.append(f"\n#### Summary\n{summaries_by_num[idx]}\n")
    else:
        lines.extend(["\n#### Solution", f"```{language}", solution, "```\n"])

    artifact_section = format_artifacts(program, heading="####")
    if artifact_section:
        lines.append(artifact_section)

    return lines
````

## → Calls
- [[IN-ProgramDatabase.get]]
- [[IN-base_database.Program]]
- [[IN-utils.format_artifacts]]
- [[IN-utils.prog_attr]]

## ← Called by
- [[IN-formatters.format_search_algorithms]]
