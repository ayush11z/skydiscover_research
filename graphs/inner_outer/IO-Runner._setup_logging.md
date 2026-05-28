---
name: IO-Runner._setup_logging
description: method in skydiscover/runner.py (runner)
metadata:
  type: project
---

# Runner._setup_logging

**File:** `skydiscover/runner.py:388`  
**Kind:** method  
**Layer:** #runner

## Source
````python
    def _setup_logging(self) -> None:
        log_dir = self.config.log_dir or os.path.join(self.output_dir, "logs")
        setup_search_logging(log_level=self.config.log_level, log_dir=log_dir, name=self.name)
````

## → Calls
- [[IO-DiscoveryControllerInput.config]]
- [[IO-DiscoveryControllerInput.output_dir]]
- [[IO-runner.Runner]]

## ← Called by
- [[IO-Runner.__init__]]
