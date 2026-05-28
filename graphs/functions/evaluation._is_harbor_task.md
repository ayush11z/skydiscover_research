---
name: evaluation._is_harbor_task
description: function in skydiscover/evaluation/__init__.py (evaluation)
metadata:
  type: project
---

# evaluation._is_harbor_task

**File:** `skydiscover/evaluation/__init__.py:39`  
**Kind:** function  
**Layer:** #evaluation

## Source
````python
def _is_harbor_task(path: str) -> bool:
    """Detect a Harbor task directory (instruction.md + tests/test.sh + environment/Dockerfile)."""
    return (
        os.path.isdir(path)
        and os.path.exists(os.path.join(path, "instruction.md"))
        and os.path.exists(os.path.join(path, "tests", "test.sh"))
        and os.path.isdir(os.path.join(path, "environment"))
        and os.path.exists(os.path.join(path, "environment", "Dockerfile"))
    )
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[evaluation.create_evaluator]]
