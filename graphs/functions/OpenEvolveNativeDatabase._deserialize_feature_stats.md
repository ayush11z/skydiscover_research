---
name: OpenEvolveNativeDatabase._deserialize_feature_stats
description: method in skydiscover/search/openevolve_native/database.py (openevolve)
metadata:
  type: project
---

# OpenEvolveNativeDatabase._deserialize_feature_stats

**File:** `skydiscover/search/openevolve_native/database.py:927`  
**Kind:** method  
**Layer:** #openevolve

## Source
````python
    def _deserialize_feature_stats(self, raw: Dict[str, Any]) -> Dict[str, Any]:
        if not raw:
            return {}
        out: Dict[str, Any] = {}
        for name, stats in raw.items():
            if isinstance(stats, dict):
                out[name] = {
                    "min": float(stats.get("min", 0.0)),
                    "max": float(stats.get("max", 1.0)),
                    "values": list(stats.get("values", [])),
                }
        return out
````

## → Calls
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]

## ← Called by
- [[OpenEvolveNativeDatabase._scale_feature_value]]
- [[OpenEvolveNativeDatabase._serialize_feature_stats]]
- [[OpenEvolveNativeDatabase._update_feature_stats]]
- [[OpenEvolveNativeDatabase.load]]
