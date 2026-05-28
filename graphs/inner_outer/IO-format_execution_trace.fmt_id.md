---
name: IO-format_execution_trace.fmt_id
description: function in skydiscover/context_builder/evox/formatters.py (context-builder)
metadata:
  type: project
---

# format_execution_trace.fmt_id

**File:** `skydiscover/context_builder/evox/formatters.py:39`  
**Kind:** function  
**Layer:** #context-builder

## Source
````python
    def fmt_id(pid):
        return pid[:8] if pid and len(pid) > 8 else (pid or "None")
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-format_execution_trace.fmt_program_ref]]
