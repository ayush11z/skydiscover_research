---
name: format_population_state.fmt_scores
description: function in skydiscover/context_builder/evox/formatters.py (context-builder)
metadata:
  type: project
---

# format_population_state.fmt_scores

**File:** `skydiscover/context_builder/evox/formatters.py:232`  
**Kind:** function  
**Layer:** #context-builder

## Source
````python
    def fmt_scores(scores):
        return [f"{s:.4f}" if s is not None else "N/A" for s in scores]
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[formatters.format_population_state]]
