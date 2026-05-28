---
name: checkpoint_manager.SafeJSONEncoder
description: class in skydiscover/search/utils/checkpoint_manager.py (search-utils)
metadata:
  type: project
---

# checkpoint_manager.SafeJSONEncoder

**File:** `skydiscover/search/utils/checkpoint_manager.py:18`  
**Kind:** class  
**Layer:** #search-utils

## Source
````python
class SafeJSONEncoder(json.JSONEncoder):
    """
    JSON encoder that handles non-serializable types gracefully.

    This is important for evolved databases where LLM-generated code may
    store non-serializable types (like sets) in program metadata.
    """

````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[AdaEvolveDatabase.save]]
- [[CheckpointManager._save_program]]
- [[GEPANativeDatabase.save]]
- [[Runner._save_best_program]]
- [[Runner._save_checkpoint]]
