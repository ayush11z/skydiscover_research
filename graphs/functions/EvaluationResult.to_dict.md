---
name: EvaluationResult.to_dict
description: method in skydiscover/evaluation/evaluation_result.py (evaluation)
metadata:
  type: project
---

# EvaluationResult.to_dict

**File:** `skydiscover/evaluation/evaluation_result.py:18`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    def to_dict(self) -> Dict[str, Any]:
        result = dict(self.metrics)
        if self.artifacts:
            result["artifacts"] = self.artifacts
        return result
````

## → Calls
- [[EvaluationResult.metrics]]

## ← Called by
- [[AdaEvolveDatabase.save]]
- [[CheckpointManager._save_program]]
- [[CoEvolutionController._initialize_first_search_program]]
- [[DiscoveryController._run_iteration]]
- [[GEPANativeDatabase.save]]
- [[MultiDimensionalAdapter.to_dict]]
- [[coevolve_logging.make_json_serializable]]
