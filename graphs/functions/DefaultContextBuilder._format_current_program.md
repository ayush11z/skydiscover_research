---
name: DefaultContextBuilder._format_current_program
description: method in skydiscover/context_builder/default/builder.py (context-builder)
metadata:
  type: project
---

# DefaultContextBuilder._format_current_program

**File:** `skydiscover/context_builder/default/builder.py:177`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def _format_current_program(
        self, current_program: Union[Program, Dict[str, Program]], language: str
    ) -> str:
        """Format parent program with heading, score breakdown, code, and feedback.

        Returns empty string when there is no current program so the heading
        is omitted entirely from the rendered prompt.
        """
        if not current_program:
            return ""

        if isinstance(current_program, dict):
            info = list(current_program.keys())[0]
            program = list(current_program.values())[0]
        else:
            info = ""
            program = current_program

        solution = prog_attr(program, "solution")
        metrics = prog_attr(program, "metrics", {})

        lines = ["# Current Solution\n"]
        if info:
            lines.append(f"\n{info}\n")

        lines.append("\n## Program Information\n")
        if metrics:
            combined = metrics.get("combined_score")
            if combined is not None and isinstance(combined, (int, float)):
                lines.append(f"combined_score: {combined:.4f}\n")

            error = metrics.get("error")
            if error:
                lines.append(f"error: {error}\n")

            other_metrics = _filter_other_metrics(metrics)
            if other_metrics:
                lines.append("Score breakdown:")
                for key, value in other_metrics.items():
                    if isinstance(value, float):
                        lines.append(f"\n  - {key}: {value:.4f}")
                    elif isinstance(value, (int, str, bool)):
                        lines.append(f"\n  - {key}: {value}")
                lines.append("\n")

        if language != "image":
            lines.append(f"\n```{language}\n{solution}\n```\n")

        feedback_section = format_artifacts(program, heading="##")
        if feedback_section:
            lines.append(feedback_section)

        return "".join(lines)
````

## → Calls
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]
- [[base_database.Program]]
- [[builder._filter_other_metrics]]
- [[utils.format_artifacts]]
- [[utils.prog_attr]]

## ← Called by
- [[AdaEvolveContextBuilder._format_current_program]]
- [[DefaultContextBuilder.build_prompt]]
