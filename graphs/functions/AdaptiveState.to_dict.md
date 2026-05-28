---
name: AdaptiveState.to_dict
description: method in skydiscover/search/adaevolve/adaptation.py (adaevolve)
metadata:
  type: project
---

# AdaptiveState.to_dict

**File:** `skydiscover/search/adaevolve/adaptation.py:191`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def to_dict(self) -> Dict[str, Any]:
        """Serialize state for checkpointing."""
        return {
            "accumulated_signal": self.accumulated_signal,
            "best_score": self.best_score,
            "improvement_count": self.improvement_count,
            "total_evaluations": self.total_evaluations,
            "decay": self.decay,
            "epsilon": self.epsilon,
            "intensity_min": self.intensity_min,
            "intensity_max": self.intensity_max,
        }
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[AdaEvolveDatabase.save]]
- [[CheckpointManager._save_program]]
- [[CoEvolutionController._initialize_first_search_program]]
- [[DiscoveryController._run_iteration]]
- [[GEPANativeDatabase.save]]
- [[MultiDimensionalAdapter.to_dict]]
- [[coevolve_logging.make_json_serializable]]
