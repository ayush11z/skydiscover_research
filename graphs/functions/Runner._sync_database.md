---
name: Runner._sync_database
description: method in skydiscover/runner.py (runner)
metadata:
  type: project
---

# Runner._sync_database

**File:** `skydiscover/runner.py:382`  
**Kind:** method  
**Layer:** #runner

## Source
````python
    def _sync_database(self) -> None:
        """Ensure we have the controller's latest database"""
        db = getattr(self.discovery_controller, "database", None)
        if db is not None and db is not self.database:
            self.database = db
````

## → Calls
- [[registry.create_database]]

## ← Called by
- [[Runner.run]]
- [[run.checkpoint_cb]]
