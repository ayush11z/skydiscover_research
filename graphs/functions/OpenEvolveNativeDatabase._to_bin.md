---
name: OpenEvolveNativeDatabase._to_bin
description: method in skydiscover/search/openevolve_native/database.py (openevolve)
metadata:
  type: project
---

# OpenEvolveNativeDatabase._to_bin

**File:** `skydiscover/search/openevolve_native/database.py:493`  
**Kind:** method  
**Layer:** #openevolve

## Source
````python
    def _to_bin(self, dim: str, value: float) -> int:
        """Update running stats, min-max scale, and return bin index."""
        self._update_feature_stats(dim, value)
        scaled = self._scale_feature_value(dim, value)
        num_bins = self.feature_bins_per_dim.get(dim, self.feature_bins)
        return max(0, min(num_bins - 1, int(scaled * num_bins)))
````

## → Calls
- [[LangFuseTracer.get]]
- [[OpenEvolveNativeDatabase._scale_feature_value]]
- [[OpenEvolveNativeDatabase._update_feature_stats]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]

## ← Called by
- [[OpenEvolveNativeDatabase._calculate_feature_coords]]
