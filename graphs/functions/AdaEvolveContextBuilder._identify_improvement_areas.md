---
name: AdaEvolveContextBuilder._identify_improvement_areas
description: method in skydiscover/context_builder/adaevolve/builder.py (context-builder)
metadata:
  type: project
---

# AdaEvolveContextBuilder._identify_improvement_areas

**File:** `skydiscover/context_builder/adaevolve/builder.py:234`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def _identify_improvement_areas(
        self,
        current_program: str,
        metrics: Dict[str, float],
        previous_programs: List[Program],
    ) -> str:
        """Generate improvement bullets for scalar or Pareto mode."""
        if not self._is_multiobjective_enabled():
            return super()._identify_improvement_areas(current_program, metrics, previous_programs)

        improvement_areas = [
            "Focus on Pareto trade-offs across: " + ", ".join(self._objective_descriptions())
        ]

        current_score = self._get_progress_score(metrics)
        if previous_programs:
            prev_metrics = prog_attr(previous_programs[-1], "metrics", {}) or {}
            prev_score = self._get_progress_score(prev_metrics)
            # Only show delta text when both scores are valid (not missing).
            missing = self._PROGRESS_SCORE_MISSING
            if current_score != missing and prev_score != missing:
                if current_score > prev_score + 1e-6:
                    improvement_areas.append(
                        f"Pareto proxy improved: {prev_score:.4f} -> {current_score:.4f}"
                    )
                elif current_score < prev_score - 1e-6:
                    improvement_areas.append(
                        f"Pareto proxy declined: {prev_score:.4f} -> {current_score:.4f}. Revisit recent trade-offs."
                    )
                else:
                    improvement_areas.append(f"Pareto proxy unchanged at {current_score:.4f}")
            elif current_score != missing:
                improvement_areas.append(f"Pareto proxy at {current_score:.4f} (first measurement)")

        threshold = self.context_config.suggest_simplification_after_chars
        if threshold and len(current_program) > threshold:
            improvement_areas.append(
                f"Consider simplifying - solution length exceeds {threshold} characters"
            )

        return "\n".join(f"- {area}" for area in improvement_areas)
````

## → Calls
- [[AdaEvolveContextBuilder._get_progress_score]]
- [[AdaEvolveContextBuilder._is_multiobjective_enabled]]
- [[AdaEvolveContextBuilder._objective_descriptions]]
- [[DefaultContextBuilder._identify_improvement_areas]]
- [[base_database.Program]]
- [[utils.prog_attr]]

## ← Called by
_(entry point — nothing in this graph calls it)_
