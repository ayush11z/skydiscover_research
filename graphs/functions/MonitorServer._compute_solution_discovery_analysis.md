---
name: MonitorServer._compute_solution_discovery_analysis
description: method in skydiscover/extras/monitor/server.py (monitor)
metadata:
  type: project
---

# MonitorServer._compute_solution_discovery_analysis

**File:** `skydiscover/extras/monitor/server.py:851`  
**Kind:** method  
**Layer:** #monitor

## Source
````python
    def _compute_solution_discovery_analysis(self) -> str:
        """Compute evolution progress, improvement patterns, and stagnation analysis."""
        programs = self._programs
        if not programs:
            return ""

        scored = [p for p in programs if isinstance(p.get("score"), (int, float))]
        if not scored:
            return ""

        lines = []
        n = len(scored)

        improvements = 0
        regressions = 0
        total_with_parent = 0
        improvement_deltas = []
        for p in scored:
            parent_score = p.get("parent_score")
            if isinstance(parent_score, (int, float)):
                total_with_parent += 1
                delta = p["score"] - parent_score
                if delta > 0:
                    improvements += 1
                    improvement_deltas.append(delta)
                elif delta < 0:
                    regressions += 1

        if total_with_parent > 0:
            hit_rate = improvements / total_with_parent * 100
            avg_gain = (
                sum(improvement_deltas) / len(improvement_deltas) if improvement_deltas else 0
            )
            lines.append("=== Improvement Rate ===")
            lines.append(
                f"  {improvements}/{total_with_parent} programs improved over parent ({hit_rate:.0f}% hit rate)"
            )
            lines.append(f"  Avg improvement when positive: {avg_gain:+.4f}")

        if n >= 10:
            quarter = max(n // 4, 1)
            early_scores = [p["score"] for p in scored[:quarter]]
            mid_scores = [p["score"] for p in scored[quarter : quarter * 2]]
            recent_scores = [p["score"] for p in scored[-quarter:]]
            early_avg = sum(early_scores) / len(early_scores)
            mid_avg = sum(mid_scores) / len(mid_scores) if mid_scores else early_avg
            recent_avg = sum(recent_scores) / len(recent_scores)

            lines.append("\n=== Score Trend ===")
            lines.append(
                f"  Early avg (first {quarter}): {early_avg:.4f}  |  "
                f"Mid avg: {mid_avg:.4f}  |  "
                f"Recent avg (last {quarter}): {recent_avg:.4f}"
            )
            if recent_avg > mid_avg + 0.001:
                lines.append("  Trend: IMPROVING")
            elif recent_avg < mid_avg - 0.005:
                lines.append("  Trend: REGRESSING")
            elif abs(recent_avg - mid_avg) < 0.001 and n > 30:
                lines.append("  Trend: PLATEAUED")
            else:
                lines.append("  Trend: STABLE")

        if n >= 5:
            best_so_far = -float("inf")
            streak = 0
            longest_streak = 0
            for p in scored:
                if p["score"] > best_so_far:
                    best_so_far = p["score"]
                    streak = 0
                else:
                    streak += 1
                    longest_streak = max(longest_streak, streak)
            lines.append("\n=== Stagnation ===")
            lines.append(
                f"  Current non-improving streak: {streak} iterations  |  "
                f"Longest streak: {longest_streak}"
            )

        islands: Dict[Any, list] = {}
        for p in scored:
            isl = p.get("island")
            if isl is not None:
                islands.setdefault(isl, []).append(p["score"])
        if len(islands) > 1:
            lines.append(f"\n=== Island Diversity ({len(islands)} islands) ===")
            for isl in sorted(islands.keys()):
                scores = islands[isl]
                lines.append(
                    f"  Island {isl}: {len(scores)} programs, "
                    f"best={max(scores):.4f}, avg={sum(scores)/len(scores):.4f}"
                )

        return "\n".join(lines)
````

## → Calls
- [[LangFuseTracer.get]]
- [[MonitorServer.__init__]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]

## ← Called by
- [[MonitorServer._build_summary_prompt]]
