---
name: DefaultContextBuilder._format_single_context_program
description: method in skydiscover/context_builder/default/builder.py (context-builder)
metadata:
  type: project
---

# DefaultContextBuilder._format_single_context_program

**File:** `skydiscover/context_builder/default/builder.py:279`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def _format_single_context_program(
        self, program: Program, index: int, language: str, lines: list
    ) -> None:
        """Append one context program's header, metrics, and code to lines."""
        if program is None:
            return

        solution = prog_attr(program, "solution")
        metrics = prog_attr(program, "metrics", {})

        combined = metrics.get("combined_score") if metrics else None
        if combined is not None and isinstance(combined, (int, float)):
            lines.append(f"### Program {index} (combined_score: {combined:.4f})\n")
        else:
            lines.append(f"### Program {index}\n")

        if metrics:
            error = metrics.get("error")
            if error:
                lines.append(f"- error: {error}\n")

            other_metrics = _filter_other_metrics(metrics)
            if other_metrics:
                lines.append("Score breakdown:")
                for key, value in other_metrics.items():
                    if isinstance(value, float):
                        lines.append(f"  - {key}: {value:.4f}")
                    elif isinstance(value, (int, str, bool)):
                        lines.append(f"  - {key}: {value}")
                lines.append("\n")

        if language != "image":
            lines.append(f"\n```{language}\n{solution}\n```\n")
        lines.append("\n")
````

## → Calls
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]
- [[base_database.Program]]
- [[builder._filter_other_metrics]]
- [[utils.prog_attr]]

## ← Called by
- [[DefaultContextBuilder._format_other_context_programs]]
