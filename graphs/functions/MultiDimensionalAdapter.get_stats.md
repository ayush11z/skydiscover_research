---
name: MultiDimensionalAdapter.get_stats
description: method in skydiscover/search/adaevolve/adaptation.py (adaevolve)
metadata:
  type: project
---

# MultiDimensionalAdapter.get_stats

**File:** `skydiscover/search/adaevolve/adaptation.py:494`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def get_stats(self) -> Dict[str, Any]:
        """
        Get statistics for logging/debugging.

        Returns:
            Dictionary with per-dimension and aggregate stats
        """
        dim_stats = []
        for i, state in enumerate(self.states):
            dec_visits = self.decayed_visits[i] if i < len(self.decayed_visits) else 0.0
            dim_stats.append(
                {
                    "index": i,
                    "accumulated_signal": state.accumulated_signal,
                    "best_score": state.best_score,
                    "search_intensity": state.get_search_intensity(),
                    "improvements": state.improvement_count,
                    "evaluations": state.total_evaluations,
                    "raw_visits": self.dimension_visits[i],
                    "decayed_visits": dec_visits,
                    "decayed_reward": self.dimension_rewards[i],
                    "reward_avg": self.dimension_rewards[i] / dec_visits if dec_visits > 0 else 0.0,
                }
            )

        return {
            "num_dimensions": len(self.states),
            "global_best_score": self.global_best_score,
            "global_productivity": self.get_global_productivity(),
            "dimensions": dim_stats,
        }
````

## → Calls
- [[MultiDimensionalAdapter.get_global_productivity]]

## ← Called by
- [[AdaEvolveDatabase.get_stats]]
