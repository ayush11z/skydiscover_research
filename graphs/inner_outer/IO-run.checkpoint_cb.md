---
name: IO-run.checkpoint_cb
description: function in skydiscover/runner.py (runner)
metadata:
  type: project
---

# run.checkpoint_cb

**File:** `skydiscover/runner.py:171`  
**Kind:** function  
**Layer:** #runner

## Source
````python
            def checkpoint_cb(iteration: int) -> None:
                self._sync_database()
                self._save_checkpoint(iteration)
````

## → Calls
- [[IO-Runner._save_checkpoint]]
- [[IO-Runner._sync_database]]

## ← Called by
- [[IO-Runner.run]]
