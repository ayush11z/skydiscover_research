---
name: IO-Runner._push_existing_to_monitor
description: method in skydiscover/runner.py (runner)
metadata:
  type: project
---

# Runner._push_existing_to_monitor

**File:** `skydiscover/runner.py:349`  
**Kind:** method  
**Layer:** #runner

## Source
````python
    def _push_existing_to_monitor(self) -> None:
        if not (self.discovery_controller.monitor_callback and self.database.programs):
            return
        for prog in self.database.programs.values():
            try:
                self.discovery_controller.monitor_callback(
                    prog, getattr(prog, "iteration_found", 0)
                )
            except Exception:
                logger.debug("Monitor callback failed for program %s", prog.id, exc_info=True)
        logger.info(f"Pushed {len(self.database.programs)} existing program(s) to monitor")
````

## → Calls
- [[IO-Program.id]]
- [[IO-Runner.run]]

## ← Called by
- [[IO-Runner.run]]
