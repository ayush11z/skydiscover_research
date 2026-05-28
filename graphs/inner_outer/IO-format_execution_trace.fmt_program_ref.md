---
name: IO-format_execution_trace.fmt_program_ref
description: function in skydiscover/context_builder/evox/formatters.py (context-builder)
metadata:
  type: project
---

# format_execution_trace.fmt_program_ref

**File:** `skydiscover/context_builder/evox/formatters.py:52`  
**Kind:** function  
**Layer:** #context-builder

## Source
````python
    def fmt_program_ref(t, prefix=""):
        label, pid, score = unpack_tuple(t)
        if pid is None:
            return f"{prefix}=None (seed program)" if prefix else "None"
        label_str = f'label="{label}", ' if label else ""
        return (
            f"{prefix} ({label_str}id={fmt_id(pid)}, score={fmt_score(score)})"
            if prefix
            else f"({label_str}id={fmt_id(pid)}, score={fmt_score(score)})"
        )
````

## → Calls
- [[IO-format_execution_trace.fmt_id]]
- [[IO-format_execution_trace.fmt_score]]
- [[IO-format_execution_trace.unpack_tuple]]

## ← Called by
- [[IO-formatters.format_execution_trace]]
