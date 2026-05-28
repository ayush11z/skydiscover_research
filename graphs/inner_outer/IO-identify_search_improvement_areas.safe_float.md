---
name: IO-identify_search_improvement_areas.safe_float
description: function in skydiscover/context_builder/evox/formatters.py (context-builder)
metadata:
  type: project
---

# identify_search_improvement_areas.safe_float

**File:** `skydiscover/context_builder/evox/formatters.py:381`  
**Kind:** function  
**Layer:** #context-builder

## Source
````python
    def safe_float(val):
        if val is None:
            return 0.0
        try:
            return float(val)
        except (ValueError, TypeError):
            return 0.0
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-formatters.identify_search_improvement_areas]]
