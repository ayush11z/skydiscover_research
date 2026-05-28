---
name: IO-formatters.identify_search_improvement_areas
description: function in skydiscover/context_builder/evox/formatters.py (context-builder)
metadata:
  type: project
---

# formatters.identify_search_improvement_areas

**File:** `skydiscover/context_builder/evox/formatters.py:373`  
**Kind:** function  
**Layer:** #context-builder

## Source
````python
def identify_search_improvement_areas(
    current_program: Program,
    metrics: Dict[str, float],
    previous_programs: List[Program],
    simplification_threshold: Optional[int] = None,
) -> str:
    """Identify improvement areas for search algorithms based on combined_score."""

    def safe_float(val):
        if val is None:
            return 0.0
        try:
            return float(val)
        except (ValueError, TypeError):
            return 0.0

    improvement_areas = []
    current_score = safe_float(metrics.get("combined_score"))

    if previous_programs:
        prev_program = previous_programs[-1]
        prev_metrics = prog_attr(prev_program, "metrics", {}) or {}
        prev_score = safe_float(prev_metrics.get("combined_score"))

        if current_score > prev_score:
            improvement_areas.append(
                f"Search algorithm score improved: {prev_score:.4f} → {current_score:.4f}"
            )
        elif current_score < prev_score:
            improvement_areas.append(
                f"Search algorithm score declined: {prev_score:.4f} → {current_score:.4f}. Consider revising."
            )
        else:
            improvement_areas.append(f"Search algorithm score unchanged at {current_score:.4f}")

    if not improvement_areas:
        improvement_areas.append("Focus on improving the search algorithm score (combined_score)")

    if simplification_threshold:
        code_length = len(prog_attr(current_program, "solution"))
        if code_length > simplification_threshold:
            improvement_areas.append(
                f"Consider simplifying - solution length exceeds {simplification_threshold} characters"
            )

    return "\n".join(f"- {area}" for area in improvement_areas)
````

## → Calls
- [[IO-ProgramDatabase.get]]
- [[IO-base_database.Program]]
- [[IO-identify_search_improvement_areas.safe_float]]
- [[IO-utils.prog_attr]]

## ← Called by
- [[IO-EvoxContextBuilder.build_prompt]]
