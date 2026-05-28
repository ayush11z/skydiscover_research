---
name: IO-coevolve_logging.make_json_serializable
description: function in skydiscover/search/evox/utils/coevolve_logging.py (evox)
metadata:
  type: project
---

# coevolve_logging.make_json_serializable

**File:** `skydiscover/search/evox/utils/coevolve_logging.py:18`  
**Kind:** function  
**Layer:** #evox

## Source
````python
def make_json_serializable(obj: Any) -> Any:
    """Recursively convert objects to JSON-serializable types."""
    if obj is None:
        return None
    if isinstance(obj, bool):
        return obj
    if isinstance(obj, (str, int, float)):
        return obj
    if isinstance(obj, dict):
        return {str(k): make_json_serializable(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [make_json_serializable(item) for item in obj]
    if isinstance(obj, (set, frozenset)):
        return sorted([make_json_serializable(item) for item in obj], key=lambda x: str(x))
    if hasattr(obj, "to_dict"):
        return make_json_serializable(obj.to_dict())
    return str(obj)
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-CoEvolutionController._assign_search_score]]
- [[IO-CoEvolutionController._generate_and_validate_search_algorithm]]
- [[IO-CoEvolutionController._initialize_first_search_program]]
- [[IO-coevolve_logging.update_saved_search_algorithm_score]]
