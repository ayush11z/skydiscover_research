---
name: IO-ProgramDatabase.get_statistics
description: method in skydiscover/search/base_database.py (database)
metadata:
  type: project
---

# ProgramDatabase.get_statistics

**File:** `skydiscover/search/base_database.py:345`  
**Kind:** method  
**Layer:** #database

## Source
````python
    def get_statistics(
        self, num_recent_iterations: int = 100, k: int = 20, improvement_threshold: float = 0.10
    ) -> Dict[str, Any]:
        """
        Get statistics about the database population.

        Args:
            num_recent_iterations: Number of recent iterations to include in trajectory stats
            k: Number of top scores to return
            improvement_threshold: Minimum score improvement to count as meaningful improvement.
        """
        import statistics

        population_size = len(self.programs)

        if self.programs:
            actual_last_iter = max(
                (
                    p.iteration_found
                    for p in self.programs.values()
                    if isinstance(p.iteration_found, int)
                ),
                default=0,
            )
            self.last_iteration = max(self.last_iteration, actual_last_iter)
        else:
            actual_last_iter = 0

        scores = [
            p.metrics.get("combined_score")
            for p in self.programs.values()
            if p.metrics.get("combined_score") is not None
        ]

        if scores:
            scores_sorted = sorted(scores, reverse=True)
            n = len(scores_sorted)
            if n >= 4:
                quartiles = statistics.quantiles(scores, n=4)
                q25, q50, q75 = quartiles[0], quartiles[1], quartiles[2]
            else:
                q25 = q50 = q75 = statistics.median(scores)
            score_stats = {
                "best": scores_sorted[0],
                "q75": q75,
                "q50": q50,
                "q25": q25,
                "worst": scores_sorted[-1],
            }

            top_scores = scores_sorted[:k]
            n = len(scores)

            pct_top = sum(1 for s in scores if s >= q75) / n * 100
            pct_upper_mid = sum(1 for s in scores if q50 <= s < q75) / n * 100
            pct_lower_mid = sum(1 for s in scores if q25 <= s < q50) / n * 100
            pct_bottom = sum(1 for s in scores if s < q25) / n * 100

            unique_scores = len(set(round(s, 4) for s in scores))

            score_stats["score_tiers"] = {
                "top": {"threshold": f"score >= {q75:.4f}", "pct_programs": pct_top},
                "upper_mid": {
                    "threshold": f"{q50:.4f} <= score < {q75:.4f}",
                    "pct_programs": pct_upper_mid,
                },
                "lower_mid": {
                    "threshold": f"{q25:.4f} <= score < {q50:.4f}",
                    "pct_programs": pct_lower_mid,
                },
                "bottom": {"threshold": f"score < {q25:.4f}", "pct_programs": pct_bottom},
            }
            score_stats["unique_scores"] = unique_scores
        else:
            score_stats = {"best": None, "q75": None, "q50": None, "q25": None, "worst": None}
            top_scores = []

        programs_with_parents = [p for p in self.programs.values() if p.parent_id is not None]
        unique_parents = len({p.parent_id for p in programs_with_parents})
        avg_solutions_per_parent = (
            len(programs_with_parents) / unique_parents if unique_parents > 0 else 0.0
        )

        iterations_without_improvement = 0
        if scores:
            best_score = max(scores)
            near_best_programs = [
                p
                for p in self.programs.values()
                if p.metrics.get("combined_score") is not None
                and p.metrics.get("combined_score") >= best_score - improvement_threshold
            ]
            if near_best_programs:
                iteration_near_best_achieved = min(
                    p.iteration_found
                    for p in near_best_programs
                    if isinstance(p.iteration_found, int)
                )
                iterations_without_improvement = actual_last_iter - iteration_near_best_achieved

        if not self.programs:
            recent_stats = {}
            recent_programs = []
        else:
            recent_programs = [
                p
                for p in self.programs.values()
                if p.metrics.get("combined_score") is not None
                and isinstance(p.iteration_found, int)
                and p.iteration_found > actual_last_iter - num_recent_iterations
            ]
            recent_programs.sort(key=lambda p: p.iteration_found)

            execution_trace = []
            recent_scores = []
            parent_scores = []

            for p in recent_programs:
                prog_id = p.id
                prog_score = p.metrics.get("combined_score")
                recent_scores.append(prog_score)

                if p.parent_id is not None:
                    parent_id = p.parent_id
                    parent_label = None
                    if p.parent_info is not None:
                        parent_label = p.parent_info[0]
                    if parent_id in self.programs:
                        parent_program = self.programs[parent_id]
                        parent_score = parent_program.metrics.get("combined_score")
                        parent_scores.append(parent_score)
                    else:
                        parent_score = None
                        parent_scores.append(None)
                    parent_tuple = (parent_label, parent_id, parent_score)
                else:
                    parent_tuple = None
                    parent_scores.append(None)

                context_tuples = []
                if p.other_context_ids:
                    context_label_map = {}
                    if p.context_info is not None:
                        for label, ctx_id in p.context_info:
                            context_label_map[ctx_id] = label

                    for other_context_id in p.other_context_ids:
                        ctx_label = context_label_map.get(other_context_id)
                        if other_context_id in self.programs:
                            ctx_score = self.programs[other_context_id].metrics.get(
                                "combined_score"
                            )
                            context_tuples.append((ctx_label, other_context_id, ctx_score))
                        else:
                            context_tuples.append((ctx_label, other_context_id, None))

                trace_entry = {
                    "iteration": p.iteration_found,
                    "program": (prog_id, prog_score),
                    "parent": parent_tuple,
                    "context": context_tuples if context_tuples else None,
                }
                execution_trace.append(trace_entry)

            from collections import Counter

            recent_programs_with_parents = [p for p in recent_programs if p.parent_id is not None]

            most_reused_parent_ratio = 0.0
            most_reused_parent_score = None
            most_reused_context_ratio = 0.0
            most_reused_context_score = None

            if recent_programs_with_parents:
                parent_counts = Counter(
                    p.parent_id for p in recent_programs_with_parents if p.parent_id
                )
                if parent_counts:
                    top_parent_id, parent_count = parent_counts.most_common(1)[0]
                    most_reused_parent_ratio = parent_count / len(recent_programs_with_parents)
                    if top_parent_id in self.programs:
                        most_reused_parent_score = self.programs[top_parent_id].metrics.get(
                            "combined_score"
                        )

            if recent_programs:
                context_counts = Counter()
                programs_with_context = 0
                for p in recent_programs:
                    if p.other_context_ids:
                        programs_with_context += 1
                        for ctx_id in p.other_context_ids:
                            context_counts[ctx_id] += 1
                if context_counts and programs_with_context > 0:
                    top_ctx_id, context_count = context_counts.most_common(1)[0]
                    most_reused_context_ratio = context_count / programs_with_context
                    if top_ctx_id in self.programs:
                        most_reused_context_score = self.programs[top_ctx_id].metrics.get(
                            "combined_score"
                        )

            recent_stats = {
                "num_recent_iterations": min(num_recent_iterations, len(recent_scores)),
                "execution_trace": execution_trace,
                "score_trajectory": recent_scores,
                "parent_scores": parent_scores,
                "iterations_without_improvement": iterations_without_improvement,
                "improvement_threshold": improvement_threshold,
                "most_reused_parent_ratio": most_reused_parent_ratio,
                "most_reused_parent_score": most_reused_parent_score,
                "most_reused_context_ratio": most_reused_context_ratio,
                "most_reused_context_score": most_reused_context_score,
            }

        return {
            "previous_programs": recent_programs,
            "population_size": population_size,
            "solution_score_summary": score_stats,
            "avg_solutions_per_parent": avg_solutions_per_parent,
            "top_solution_scores": top_scores,
            "recent_solution_stats": recent_stats,
        }
````

## → Calls
- [[IO-Program.context_info]]
- [[IO-Program.id]]
- [[IO-Program.iteration_found]]
- [[IO-Program.metrics]]
- [[IO-Program.other_context_ids]]
- [[IO-Program.parent_id]]
- [[IO-Program.parent_info]]
- [[IO-ProgramDatabase.load]]

## ← Called by
- [[IO-DiscoveryController._build_prompt]]
