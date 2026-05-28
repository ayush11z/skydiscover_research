---
name: OpenEvolveNativeDatabase._update_feature_stats
description: method in skydiscover/search/openevolve_native/database.py (openevolve)
metadata:
  type: project
---

# OpenEvolveNativeDatabase._update_feature_stats

**File:** `skydiscover/search/openevolve_native/database.py:508`  
**Kind:** method  
**Layer:** #openevolve

## Source
````python
    def _update_feature_stats(self, feature_name: str, value: float) -> None:
        if feature_name not in self.feature_stats:
            self.feature_stats[feature_name] = {
                "min": value,
                "max": value,
                "values": [],
            }
        stats = self.feature_stats[feature_name]
        stats["min"] = min(stats["min"], value)
        stats["max"] = max(stats["max"], value)
        stats["values"].append(value)
        if len(stats["values"]) > 1000:
            stats["values"] = stats["values"][-1000:]
````

## → Calls
- [[OpenEvolveNativeDatabase._deserialize_feature_stats]]

## ← Called by
- [[OpenEvolveNativeDatabase._to_bin]]
