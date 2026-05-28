---
name: ParadigmTracker.to_dict
description: method in skydiscover/search/adaevolve/paradigm/tracker.py (adaevolve)
metadata:
  type: project
---

# ParadigmTracker.to_dict

**File:** `skydiscover/search/adaevolve/paradigm/tracker.py:310`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def to_dict(self) -> Dict[str, Any]:
        """Serialize state for checkpointing."""
        return {
            "window_size": self.window_size,
            "improvement_threshold": self.improvement_threshold,
            "max_paradigm_uses": self.max_paradigm_uses,
            "max_tried_paradigms": self.max_tried_paradigms,
            "num_paradigms_to_generate": self.num_paradigms_to_generate,
            "improvement_history": list(self.improvement_history),
            "active_paradigms": list(self.active_paradigms),
            "paradigm_usage_counts": dict(self.paradigm_usage_counts),
            "current_paradigm_index": self.current_paradigm_index,
            "tried_paradigms": list(self.tried_paradigms),
            "best_score_at_paradigm_gen": self.best_score_at_paradigm_gen,
            "best_score_during_paradigm": self.best_score_during_paradigm,
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
