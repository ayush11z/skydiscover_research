---
name: DefaultContextBuilder._format_previous_attempts
description: method in skydiscover/context_builder/default/builder.py (context-builder)
metadata:
  type: project
---

# DefaultContextBuilder._format_previous_attempts

**File:** `skydiscover/context_builder/default/builder.py:376`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def _format_previous_attempts(
        self, previous_programs: List[Program], num_previous_attempts: int = 3
    ) -> str:
        """Format top N previous attempts with their changes, metrics, and outcome."""
        if not previous_programs:
            return "No previous attempts yet."

        try:
            previous_attempt_template = self.template_manager.get_template("previous_attempt")
        except (ValueError, KeyError):
            previous_attempt_template = "### Attempt {attempt_number}\n- Changes: {changes}\n- Metrics: {performance}\n- Outcome: {outcome}"

        previous_programs = sorted(
            previous_programs,
            key=lambda p: prog_attr(p, "metrics", {}).get("combined_score", 0.0),
            reverse=True,
        )
        selected = previous_programs[: min(num_previous_attempts, len(previous_programs))]

        lines = []
        for i, program in enumerate(reversed(selected)):
            attempt_number = len(selected) - i
            metadata = prog_attr(program, "metadata", {}) or {}
            metrics = prog_attr(program, "metrics", {}) or {}

            changes = metadata.get("changes", "Unknown changes")
            performance_parts = []
            for name, value in metrics.items():
                if isinstance(value, (int, float)):
                    try:
                        performance_parts.append(f"{name}: {value:.4f}")
                    except (ValueError, TypeError):
                        performance_parts.append(f"{name}: {value}")
                else:
                    performance_parts.append(f"{name}: {value}")
            performance_str = ", ".join(performance_parts) if performance_parts else "No metrics"

            parent_metrics = metadata.get("parent_metrics", {})
            outcome = self._determine_outcome(metrics, parent_metrics)

            lines.append(
                previous_attempt_template.format(
                    attempt_number=attempt_number,
                    changes=changes,
                    performance=performance_str,
                    outcome=outcome,
                )
                + "\n\n"
            )

        return "".join(lines)
````

## → Calls
- [[DefaultContextBuilder._determine_outcome]]
- [[TemplateManager.get_template]]
- [[_ConsoleFormatter.format]]
- [[base_database.Program]]
- [[utils.prog_attr]]

## ← Called by
- [[AdaEvolveContextBuilder._format_previous_attempts]]
- [[DefaultContextBuilder.build_prompt]]
