---
name: DefaultContextBuilder._identify_improvement_areas
description: method in skydiscover/context_builder/default/builder.py (context-builder)
metadata:
  type: project
---

# DefaultContextBuilder._identify_improvement_areas

**File:** `skydiscover/context_builder/default/builder.py:231`  
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
        """Generate bullet points: score trend vs previous attempt, simplification hint."""
        improvement_areas = []

        current_score = metrics.get("combined_score", 0.0)
        if not isinstance(current_score, (int, float)):
            try:
                current_score = float(current_score)
            except (ValueError, TypeError):
                current_score = 0.0

        if previous_programs:
            prev = previous_programs[-1]
            prev_metrics = prog_attr(prev, "metrics", {})
            prev_score = prev_metrics.get("combined_score", 0.0)
            if not isinstance(prev_score, (int, float)):
                try:
                    prev_score = float(prev_score)
                except (ValueError, TypeError):
                    prev_score = 0.0

            if current_score > prev_score:
                improvement_areas.append(
                    f"Combined score improved: {prev_score:.4f} → {current_score:.4f}"
                )
            elif current_score < prev_score:
                improvement_areas.append(
                    f"Combined score declined: {prev_score:.4f} → {current_score:.4f}. Consider revising recent changes."
                )
            elif abs(current_score - prev_score) < 1e-6:
                improvement_areas.append(f"Combined score unchanged at {current_score:.4f}")

        threshold = self.context_config.suggest_simplification_after_chars
        if threshold and len(current_program) > threshold:
            improvement_areas.append(
                f"Consider simplifying - solution length exceeds {threshold} characters"
            )

        if not improvement_areas:
            improvement_areas.append("Focus on improving the combined_score")

        return "\n".join(f"- {area}" for area in improvement_areas)
````

## → Calls
- [[Config.context_builder]]
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]
- [[base.ContextBuilder]]
- [[base_database.Program]]
- [[utils.prog_attr]]

## ← Called by
- [[AdaEvolveContextBuilder._identify_improvement_areas]]
- [[DefaultContextBuilder.build_prompt]]
