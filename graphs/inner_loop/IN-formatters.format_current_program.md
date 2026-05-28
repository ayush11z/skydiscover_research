---
name: IN-formatters.format_current_program
description: function in skydiscover/context_builder/evox/formatters.py (context-builder)
metadata:
  type: project
---

# formatters.format_current_program

**File:** `skydiscover/context_builder/evox/formatters.py:326`  
**Kind:** function  
**Layer:** #context-builder

## Source
````python
def format_current_program(
    current_program: Union[Program, Dict[str, Program]],
    language: str,
    improvement_areas: Optional[str] = None,
) -> str:
    """Format current program with metrics and solution."""
    if not current_program:
        return ""

    if isinstance(current_program, dict) and current_program:
        label = list(current_program.keys())[0] or "Current Search Program"
        program = list(current_program.values())[0]
    else:
        label = "Current Search Program"
        program = current_program
    solution = prog_attr(program, "solution")
    metrics = prog_attr(program, "metrics", {})

    window_start = int(metrics.get("window_start_iteration", 0))
    horizon = int(metrics.get("search_window_horizon") or 0)
    window_end = window_start + horizon
    start_score = metrics.get("search_window_start_score", 0.0)
    end_score = metrics.get("search_window_end_score", 0.0)
    combined_score = metrics.get("combined_score", 0.0)
    improvement = end_score - start_score

    lines = [f"## {label}\n", "### Metrics"]
    if improvement_areas:
        lines.append(f"Focus areas:\n{improvement_areas}\n")
    lines.append(f"Search Algorithm Score = {combined_score:.4f}")
    lines.append(
        f"This search algorithm ran from iteration {window_start} to {window_end} ({horizon} iterations)"
    )
    lines.append(
        f"This search algorithm changed the downstream solution combined_score by: {start_score:.4f} -> {end_score:.4f} (+{improvement:.4f})"
    )
    lines.append(f"\n### Solution\n```{language}")
    lines.append(solution)
    lines.append("```\n")

    artifact_section = format_artifacts(program, heading="###")
    if artifact_section:
        lines.append(artifact_section)

    return "\n".join(lines)
````

## → Calls
- [[IN-ProgramDatabase.get]]
- [[IN-base_database.Program]]
- [[IN-utils.format_artifacts]]
- [[IN-utils.prog_attr]]

## ← Called by
- [[IN-EvoxContextBuilder.build_prompt]]
