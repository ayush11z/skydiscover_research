---
name: format_execution_trace.fmt_score
description: function in skydiscover/context_builder/evox/formatters.py (context-builder)
metadata:
  type: project
---

# format_execution_trace.fmt_score

**File:** `skydiscover/context_builder/evox/formatters.py:42`  
**Kind:** function  
**Layer:** #context-builder

## Source
````python
    def fmt_score(s):
        return f"{s:.4f}" if s is not None else "N/A"
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[format_execution_trace.fmt_program_ref]]
- [[formatters.format_execution_trace]]
