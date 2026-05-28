---
name: IN-formatters.format_population_state
description: function in skydiscover/context_builder/evox/formatters.py (context-builder)
metadata:
  type: project
---

# formatters.format_population_state

**File:** `skydiscover/context_builder/evox/formatters.py:227`  
**Kind:** function  
**Layer:** #context-builder

## Source
````python
def format_population_state(db_stats: Dict[str, Any]) -> str:
    """Format the population state from db_stats into clean, actionable lines."""
    if not db_stats:
        return ""

    def fmt_scores(scores):
        return [f"{s:.4f}" if s is not None else "N/A" for s in scores]

    lines = []
    pop_size = db_stats.get("population_size")
    lines.append(f"- population_size: {pop_size}")

    score_summary = db_stats.get("solution_score_summary") or {}
    sota = db_stats.get("SOTA_score")
    best = score_summary.get("best")
    q75, q50, q25 = (
        score_summary.get("q75"),
        score_summary.get("q50") or score_summary.get("median"),
        score_summary.get("q25"),
    )
    worst = score_summary.get("worst")

    if best is not None:
        pct = lambda v: (v / best * 100) if best > 0 and v is not None else 0

        dist_parts = [f"current_best={best:.4f}"]
        for name, val in [("75th_pct", q75), ("50th_pct", q50), ("25th_pct", q25)]:
            if val is not None:
                dist_parts.append(f"{name}={val:.4f} ({pct(val):.0f}%)")
        if worst is not None:
            dist_parts.append(f"worst={worst:.4f}")

        lines.append(f"- score_distribution: {', '.join(dist_parts)}")
        if sota is not None:
            lines.append(f"- gap_to_SOTA: SOTA={sota:.4f}, gap={sota - best:.4f}")

        if tiers := score_summary.get("score_tiers"):
            tier_parts = [
                f"{n} ({d.get('threshold','')}): {d.get('pct_programs',0):.0f}%"
                for n, d in tiers.items()
            ]
            lines.append(f"- programs_by_score_tier: {', '.join(tier_parts)}")

        if (unique := score_summary.get("unique_scores")) is not None:
            lines.append(f"- unique_score_values: {unique}")

    if (avg := db_stats.get("avg_solutions_per_parent")) is not None and pop_size:
        lines.append(f"- {avg / pop_size * 100:.1f}% of solutions share the same parent on average")

    if top_scores := db_stats.get("top_solution_scores"):
        best_score = top_scores[0]
        best_count = (
            sum(
                1
                for s in top_scores
                if isinstance(s, (int, float)) and round(s, 4) == round(best_score, 4)
            )
            if isinstance(best_score, (int, float))
            else 0
        )
        lines.append(f"- top_{len(top_scores)}_scores: {fmt_scores(top_scores)}")
        if best_count > 1:
            lines.append(f"  - Top score ({best_score:.4f}) repeated {best_count}x")
        if best_count == len(top_scores):
            lines.append(f"  (⚠️ ALL {best_count} identical)")

    if recent := db_stats.get("recent_solution_stats"):
        if (iters := recent.get("iterations_without_improvement")) and iters > 0:
            thresh = recent.get("improvement_threshold", 0.0)
            thresh_str = f" by more than {thresh:.4f}" if thresh > 0 else ""
            lines.append(f"- No improvement{thresh_str} for {iters} iterations")

        def score_bucket(score):
            if score is None or best is None:
                return None
            if score >= best:
                return "at best"
            if q75 and score >= q75:
                return "75-100th"
            if q50 and score >= q50:
                return "50-75th"
            if q25 and score >= q25:
                return "25-50th"
            return "0-25th"

        for key, label in [("most_reused_parent", "parent"), ("most_reused_context", "context")]:
            if (ratio := recent.get(f"{key}_ratio")) and ratio > 0:
                bucket = score_bucket(recent.get(f"{key}_score"))
                score_str = f", score {bucket}" if bucket else ""
                lines.append(f"- {label}: {ratio*100:.0f}% reuse rate{score_str}")

        if traj := recent.get("score_trajectory"):
            lines.append(f"- recent_scores (last {len(traj)}): {fmt_scores(traj)}")
            if parent := recent.get("parent_scores"):
                lines.append(f"- recent_parent_scores: {fmt_scores(parent)}")

    return "\n".join(lines)
````

## → Calls
- [[IN-ProgramDatabase.get]]
- [[IN-format_population_state.fmt_scores]]
- [[IN-format_population_state.score_bucket]]

## ← Called by
- [[IN-EvoxContextBuilder.build_prompt]]
- [[IN-build_prompt.gather_llm_calls]]
