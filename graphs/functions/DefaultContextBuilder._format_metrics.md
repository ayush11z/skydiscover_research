---
name: DefaultContextBuilder._format_metrics
description: method in skydiscover/context_builder/default/builder.py (context-builder)
metadata:
  type: project
---

# DefaultContextBuilder._format_metrics

**File:** `skydiscover/context_builder/default/builder.py:440`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def _format_metrics(self, metrics: Dict[str, float]) -> str:
        """Format metrics: combined_score first, then error, then per-metric breakdown."""
        if not metrics:
            return "No metrics available"

        lines = []
        combined_score = metrics.get("combined_score")
        if combined_score is not None:
            lines.append(f"- combined_score: {combined_score:.4f}")

        error = metrics.get("error")
        if error:
            lines.append(f"- error: {error}")

        other_metrics = _filter_other_metrics(metrics)
        if other_metrics:
            lines.append("")
            lines.append("Metrics:")
            for key, value in other_metrics.items():
                if isinstance(value, float):
                    lines.append(f"  - {key}: {value:.4f}")
                elif isinstance(value, (int, str, bool)):
                    lines.append(f"  - {key}: {value}")

        return "\n".join(lines) if lines else "No metrics available"
````

## → Calls
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]
- [[builder._filter_other_metrics]]

## ← Called by
- [[DefaultContextBuilder.build_prompt]]
