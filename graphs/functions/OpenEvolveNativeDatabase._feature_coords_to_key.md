---
name: OpenEvolveNativeDatabase._feature_coords_to_key
description: staticmethod in skydiscover/search/openevolve_native/database.py (openevolve)
metadata:
  type: project
---

# OpenEvolveNativeDatabase._feature_coords_to_key

**File:** `skydiscover/search/openevolve_native/database.py:501`  
**Kind:** staticmethod  
**Layer:** #openevolve

## Source
````python
    def _feature_coords_to_key(coords: List[int]) -> str:
        return "-".join(str(c) for c in coords)
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[OpenEvolveNativeDatabase._sample_other_context_programs]]
- [[OpenEvolveNativeDatabase.add]]
