---
name: IO-Runner._setup_monitor_summary
description: method in skydiscover/runner.py (runner)
metadata:
  type: project
---

# Runner._setup_monitor_summary

**File:** `skydiscover/runner.py:335`  
**Kind:** method  
**Layer:** #runner

## Source
````python
    def _setup_monitor_summary(self, monitor_server) -> None:
        if not (monitor_server and self.config.monitor.summary_model):
            return
        try:
            monitor_server.configure_summary(
                model=self.config.monitor.summary_model,
                api_key=self.config.monitor.summary_api_key or "",
                api_base=self.config.monitor.summary_api_base,
                top_k=self.config.monitor.summary_top_k,
                interval=self.config.monitor.summary_interval,
            )
        except Exception as e:
            logger.warning(f"Failed to configure AI summary: {e}")
````

## → Calls
- [[IO-DiscoveryControllerInput.config]]

## ← Called by
- [[IO-Runner.run]]
