---
name: builder._filter_other_metrics
description: function in skydiscover/context_builder/default/builder.py (context-builder)
metadata:
  type: project
---

# builder._filter_other_metrics

**File:** `skydiscover/context_builder/default/builder.py:39`  
**Kind:** function  
**Layer:** #context-builder

## Source
````python
def _filter_other_metrics(metrics: dict) -> dict:
    return {k: v for k, v in metrics.items() if k not in {"combined_score", "error"}}
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[DefaultContextBuilder._format_current_program]]
- [[DefaultContextBuilder._format_metrics]]
- [[DefaultContextBuilder._format_single_context_program]]
