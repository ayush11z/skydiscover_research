---
name: MultiDimensionalAdapter.get_global_productivity
description: method in skydiscover/search/adaevolve/adaptation.py (adaevolve)
metadata:
  type: project
---

# MultiDimensionalAdapter.get_global_productivity

**File:** `skydiscover/search/adaevolve/adaptation.py:479`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def get_global_productivity(self) -> float:
        """
        Get aggregate productivity across all dimensions.

        Returns:
            Float representing overall improvement rate
        """
        total_improvements = sum(s.improvement_count for s in self.states)
        total_evaluations = sum(s.total_evaluations for s in self.states)

        if total_evaluations == 0:
            return 1.0  # Assume productive if no data

        return total_improvements / total_evaluations
````

## → Calls
- [[AdaptiveState.improvement_count]]
- [[AdaptiveState.total_evaluations]]

## ← Called by
- [[AdaEvolveDatabase._should_spawn_island]]
- [[AdaEvolveDatabase.get_comprehensive_iteration_stats]]
- [[MultiDimensionalAdapter.get_stats]]
