---
name: IO-format_population_state.score_bucket
description: function in skydiscover/context_builder/evox/formatters.py (context-builder)
metadata:
  type: project
---

# format_population_state.score_bucket

**File:** `skydiscover/context_builder/evox/formatters.py:299`  
**Kind:** function  
**Layer:** #context-builder

## Source
````python
        def score_bucket(score):
            if score is None or best is None:
                return None
            if score >= best:
                return "at best"
            if q75 and score >= q75:
                return "75-100th"
            if q50 and score >= q50:
                return "50-75th"
            if q25 and score >= q25:
                return "25-50th"
            return "0-25th"
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-formatters.format_population_state]]
