---
name: MultiDimensionalAdapter.get_search_intensity
description: method in skydiscover/search/adaevolve/adaptation.py (adaevolve)
metadata:
  type: project
---

# MultiDimensionalAdapter.get_search_intensity

**File:** `skydiscover/search/adaevolve/adaptation.py:465`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def get_search_intensity(self, dim_idx: int) -> float:
        """
        Get search intensity for a specific dimension.

        Args:
            dim_idx: Index of the dimension

        Returns:
            intensity: Float in [intensity_min, intensity_max]
        """
        if dim_idx < 0 or dim_idx >= len(self.states):
            raise ValueError(f"Invalid dimension index: {dim_idx}")
        return self.states[dim_idx].get_search_intensity()
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[AdaEvolveDatabase._sample_from_archive]]
- [[AdaEvolveDatabase._sample_legacy]]
