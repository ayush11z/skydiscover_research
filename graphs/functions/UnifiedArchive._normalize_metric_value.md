---
name: UnifiedArchive._normalize_metric_value
description: method in skydiscover/search/adaevolve/archive/unified_archive.py (adaevolve)
metadata:
  type: project
---

# UnifiedArchive._normalize_metric_value

**File:** `skydiscover/search/adaevolve/archive/unified_archive.py:528`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _normalize_metric_value(self, key: str, value: Any) -> Optional[float]:
        """Convert a metric to an internal score where larger is always better."""
        from skydiscover.utils.metrics import normalize_metric_value

        return normalize_metric_value(key, value, self.config.higher_is_better)
````

## → Calls
- [[DiscoveryControllerInput.config]]
- [[metrics.normalize_metric_value]]

## ← Called by
- [[UnifiedArchive._get_fitness]]
