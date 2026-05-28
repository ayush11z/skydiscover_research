---
name: IO-format_db_stats_diff.fmt_scores
description: function in skydiscover/context_builder/evox/formatters.py (context-builder)
metadata:
  type: project
---

# format_db_stats_diff.fmt_scores

**File:** `skydiscover/context_builder/evox/formatters.py:214`  
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
- [[IO-formatters.format_db_stats_diff]]
