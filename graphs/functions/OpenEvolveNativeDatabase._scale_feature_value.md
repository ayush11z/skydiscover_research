---
name: OpenEvolveNativeDatabase._scale_feature_value
description: method in skydiscover/search/openevolve_native/database.py (openevolve)
metadata:
  type: project
---

# OpenEvolveNativeDatabase._scale_feature_value

**File:** `skydiscover/search/openevolve_native/database.py:522`  
**Kind:** method  
**Layer:** #openevolve

## Source
````python
    def _scale_feature_value(self, feature_name: str, value: float) -> float:
        if feature_name not in self.feature_stats:
            return min(1.0, max(0.0, value))
        stats = self.feature_stats[feature_name]
        min_val, max_val = stats["min"], stats["max"]
        if max_val == min_val:
            return 0.5
        return min(1.0, max(0.0, (value - min_val) / (max_val - min_val)))
````

## → Calls
- [[OpenEvolveNativeDatabase._deserialize_feature_stats]]

## ← Called by
- [[OpenEvolveNativeDatabase._to_bin]]
