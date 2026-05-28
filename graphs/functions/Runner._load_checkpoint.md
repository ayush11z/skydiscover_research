---
name: Runner._load_checkpoint
description: method in skydiscover/runner.py (runner)
metadata:
  type: project
---

# Runner._load_checkpoint

**File:** `skydiscover/runner.py:431`  
**Kind:** method  
**Layer:** #runner

## Source
````python
    def _load_checkpoint(self, checkpoint_path: str) -> None:
        if not os.path.exists(checkpoint_path):
            raise FileNotFoundError(f"Checkpoint not found: {checkpoint_path}")
        self.database.load(checkpoint_path)
        logger.info(f"Loaded checkpoint (iteration {self.database.last_iteration})")
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[Runner.run]]
