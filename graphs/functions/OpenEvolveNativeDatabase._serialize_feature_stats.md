---
name: OpenEvolveNativeDatabase._serialize_feature_stats
description: method in skydiscover/search/openevolve_native/database.py (openevolve)
metadata:
  type: project
---

# OpenEvolveNativeDatabase._serialize_feature_stats

**File:** `skydiscover/search/openevolve_native/database.py:913`  
**Kind:** method  
**Layer:** #openevolve

## Source
````python
    def _serialize_feature_stats(self) -> Dict[str, Any]:
        out: Dict[str, Any] = {}
        for name, stats in self.feature_stats.items():
            s: Dict[str, Any] = {}
            for k, v in stats.items():
                if k == "values":
                    s[k] = v[-100:] if isinstance(v, list) and len(v) > 100 else v
                elif hasattr(v, "item"):  # numpy scalar
                    s[k] = v.item()
                else:
                    s[k] = v
            out[name] = s
        return out
````

## → Calls
- [[OpenEvolveNativeDatabase._deserialize_feature_stats]]

## ← Called by
- [[OpenEvolveNativeDatabase.save]]
