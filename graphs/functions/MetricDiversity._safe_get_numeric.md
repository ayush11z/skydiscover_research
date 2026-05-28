---
name: MetricDiversity._safe_get_numeric
description: method in skydiscover/search/adaevolve/archive/diversity.py (adaevolve)
metadata:
  type: project
---

# MetricDiversity._safe_get_numeric

**File:** `skydiscover/search/adaevolve/archive/diversity.py:225`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _safe_get_numeric(self, metrics: Dict, key: str, default: float) -> Optional[float]:
        """Safely get a numeric value from metrics, returning None if not numeric."""
        val = metrics.get(key)
        if val is None:
            return default
        if isinstance(val, (int, float)):
            return float(val)
        # Try to convert string to float (might be a stringified number)
        if isinstance(val, str):
            try:
                return float(val)
            except (ValueError, TypeError):
                return None
        return None
````

## → Calls
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]

## ← Called by
- [[MetricDiversity.distance]]
