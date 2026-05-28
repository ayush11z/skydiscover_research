---
name: IN-formatters.format_db_stats_diff
description: function in skydiscover/context_builder/evox/formatters.py (context-builder)
metadata:
  type: project
---

# formatters.format_db_stats_diff

**File:** `skydiscover/context_builder/evox/formatters.py:106`  
**Kind:** function  
**Layer:** #context-builder

## Source
````python
def format_db_stats_diff(
    start_stats: Dict[str, Any], end_stats: Dict[str, Any], horizon: Optional[int] = None
) -> str:
    """Format start -> end db_stats comparison for a search algorithm's window."""
    if not start_stats or not end_stats:
        return ""

    lines = ["Population Statistics Change (Start -> End of Search Window):"]

    start_pop = start_stats.get("population_size", "?")
    end_pop = end_stats.get("population_size", "?")
    lines.append(f"- population_size: {start_pop} -> {end_pop}")

    start_summary = start_stats.get("solution_score_summary", {})
    end_summary = end_stats.get("solution_score_summary", {})
    if start_summary and end_summary:
        parts = []
        key_names = [
            ("best", "current_best"),
            ("q75", "75th_pct"),
            ("q50", "50th_pct (median)"),
            ("q25", "25th_pct"),
            ("worst", "worst"),
        ]
        for key, display_name in key_names:
            s = start_summary.get(key)
            e = end_summary.get(key)
            if s is not None and e is not None:
                diff = e - s
                sign = "+" if diff >= 0 else ""
                parts.append(f"{display_name}: {s:.4f} -> {e:.4f} ({sign}{diff:.4f})")
        if parts:
            lines.append(f"- {', '.join(parts)}")

    start_top = start_stats.get("top_solution_scores", [])
    end_top = end_stats.get("top_solution_scores", [])
    if start_top and end_top:
        k = min(len(start_top), len(end_top))
        start_fmt = [f"{s:.4f}" for s in start_top[:k]]
        end_fmt = [f"{s:.4f}" for s in end_top[:k]]
        lines.append(f"- top_{k}_solution_scores: {start_fmt} -> {end_fmt}")

    start_avg = start_stats.get("avg_solutions_per_parent")
    end_avg = end_stats.get("avg_solutions_per_parent")
    if start_avg is not None and end_avg is not None and start_pop and end_pop:
        start_pct = (start_avg / start_pop * 100) if start_pop != "?" else 0
        end_pct = (end_avg / end_pop * 100) if end_pop != "?" else 0
        lines.append(
            f"- % of solutions share the same parent on average: {start_pct:.1f}% -> {end_pct:.1f}%"
        )

    sota = end_stats.get("SOTA_score")
    if sota is not None and start_summary and end_summary:
        start_best = start_summary.get("best")
        end_best = end_summary.get("best")
        if start_best is not None and end_best is not None:
            start_gap = sota - start_best
            end_gap = sota - end_best
            gap_diff = end_gap - start_gap
            sign = "+" if gap_diff >= 0 else ""
            lines.append(
                f"- gap_to_SOTA (lower is better): {start_gap:.4f} -> {end_gap:.4f} ({sign}{gap_diff:.4f})"
            )

    start_tiers = start_summary.get("score_tiers") if start_summary else None
    end_tiers = end_summary.get("score_tiers") if end_summary else None
    if start_tiers and end_tiers:
        tier_parts = []
        for tier_name in end_tiers.keys():
            start_data = start_tiers.get(tier_name, {})
            end_data = end_tiers.get(tier_name, {})
            start_pct = start_data.get("pct_programs", 0)
            end_pct = end_data.get("pct_programs", 0)
            start_threshold = start_data.get("threshold", "")
            end_threshold = end_data.get("threshold", "")
            diff = end_pct - start_pct
            sign = "+" if diff >= 0 else ""
            tier_parts.append(
                f"\n  {tier_name}: [{start_threshold}] {start_pct:.0f}% -> [{end_threshold}] {end_pct:.0f}% ({sign}{diff:.0f}%)"
            )
        lines.append(f"- programs_by_score_tier:{','.join(tier_parts)}")

    end_recent = end_stats.get("recent_solution_stats", {})
    if end_recent:
        iters_no_improve = end_recent.get("iterations_without_improvement")
        threshold = end_recent.get("improvement_threshold", 0.0)
        if iters_no_improve is not None:
            if threshold > 0:
                lines.append(
                    f"- iterations_without_improvement (improvement <= {threshold:.4f}): {iters_no_improve}"
                )
            else:
                lines.append(f"- iterations_without_improvement: {iters_no_improve}")

        execution_trace = end_recent.get("execution_trace")
        if execution_trace:
            if horizon:
                execution_trace = execution_trace[-horizon:]

            first_iter = execution_trace[0].get("iteration", "?")
            last_iter = execution_trace[-1].get("iteration", "?")
            lines.append(f"\n### Execution Trace (iterations {first_iter}-{last_iter})")
            window_start_score = start_summary.get("best") if start_summary else None
            lines.append(
                format_execution_trace(execution_trace, window_start_score=window_start_score)
            )
        else:

            def fmt_scores(scores):
                return [f"{s:.4f}" if s is not None else "N/A" for s in scores]

            if score_trajectory := end_recent.get("score_trajectory"):
                lines.append(
                    f"- recent_score_trajectory (last {len(score_trajectory)}): {fmt_scores(score_trajectory)}"
                )
                if parent_scores := end_recent.get("parent_scores"):
                    lines.append(f"- recent_parent_scores: {fmt_scores(parent_scores)}")

    return "\n".join(lines)
````

## → Calls
- [[IN-ProgramDatabase.get]]
- [[IN-format_db_stats_diff.fmt_scores]]
- [[IN-formatters.format_execution_trace]]

## ← Called by
- [[IN-formatters.prepare_search_algorithms_data]]
