---
name: OpenEvolveNativeDatabase._get_cached_diversity
description: method in skydiscover/search/openevolve_native/database.py (openevolve)
metadata:
  type: project
---

# OpenEvolveNativeDatabase._get_cached_diversity

**File:** `skydiscover/search/openevolve_native/database.py:544`  
**Kind:** method  
**Layer:** #openevolve

## Source
````python
    def _get_cached_diversity(self, program: Program) -> float:
        code_hash = hash(program.solution)

        if code_hash in self.diversity_cache:
            return self.diversity_cache[code_hash]["value"]

        if (
            not self.diversity_reference_set
            or len(self.diversity_reference_set) < self.diversity_reference_size
        ):
            self._update_diversity_reference_set()

        scores = [
            self._fast_code_diversity(program.solution, ref)
            for ref in self.diversity_reference_set
            if ref != program.solution
        ]
        diversity = sum(scores) / max(1, len(scores)) if scores else 0.0

        # LRU eviction
        if len(self.diversity_cache) >= self.diversity_cache_size:
            oldest = min(self.diversity_cache, key=lambda h: self.diversity_cache[h]["timestamp"])
            del self.diversity_cache[oldest]

        self.diversity_cache[code_hash] = {
            "value": diversity,
            "timestamp": time.time(),
        }
        return diversity
````

## → Calls
- [[OpenEvolveNativeDatabase._fast_code_diversity]]
- [[OpenEvolveNativeDatabase._update_diversity_reference_set]]
- [[Program.solution]]
- [[base_database.Program]]

## ← Called by
- [[OpenEvolveNativeDatabase._calculate_feature_coords]]
