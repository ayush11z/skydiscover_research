---
name: MultiDimensionalAdapter.to_dict
description: method in skydiscover/search/adaevolve/adaptation.py (adaevolve)
metadata:
  type: project
---

# MultiDimensionalAdapter.to_dict

**File:** `skydiscover/search/adaevolve/adaptation.py:526`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def to_dict(self) -> Dict[str, Any]:
        """Serialize state for checkpointing."""
        return {
            "states": [s.to_dict() for s in self.states],
            "dimension_visits": list(self.dimension_visits),
            "dimension_rewards": list(self.dimension_rewards),
            "decayed_visits": list(self.decayed_visits),
            "global_best_score": self.global_best_score,
            "ucb_exploration": self.ucb_exploration,
            "min_visits": self.min_visits,
            "decay": self.decay,
            "epsilon": self.epsilon,
        }
````

## → Calls
- [[AdaptiveState.to_dict]]
- [[Config.to_dict]]
- [[EvaluationResult.to_dict]]
- [[ParadigmTracker.to_dict]]
- [[Program.to_dict]]

## ← Called by
_(entry point — nothing in this graph calls it)_
