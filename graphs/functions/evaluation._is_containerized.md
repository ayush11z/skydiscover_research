---
name: evaluation._is_containerized
description: function in skydiscover/evaluation/__init__.py (evaluation)
metadata:
  type: project
---

# evaluation._is_containerized

**File:** `skydiscover/evaluation/__init__.py:50`  
**Kind:** function  
**Layer:** #evaluation

## Source
````python
def _is_containerized(path: str) -> bool:
    """Detect a standard containerized benchmark (Dockerfile + evaluate.sh)."""
    return (
        os.path.isdir(path)
        and os.path.exists(os.path.join(path, "Dockerfile"))
        and os.path.exists(os.path.join(path, "evaluate.sh"))
    )
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[evaluation.create_evaluator]]
