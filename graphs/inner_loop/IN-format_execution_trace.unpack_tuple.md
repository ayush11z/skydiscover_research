---
name: IN-format_execution_trace.unpack_tuple
description: function in skydiscover/context_builder/evox/formatters.py (context-builder)
metadata:
  type: project
---

# format_execution_trace.unpack_tuple

**File:** `skydiscover/context_builder/evox/formatters.py:45`  
**Kind:** function  
**Layer:** #context-builder

## Source
````python
    def unpack_tuple(t):
        if not t:
            return None, None, None
        if len(t) >= 3:
            return t[0], t[1], t[2]
        return None, t[0], t[1]
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IN-format_execution_trace.fmt_program_ref]]
- [[IN-formatters.format_execution_trace]]
