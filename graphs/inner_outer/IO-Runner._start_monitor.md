---
name: IO-Runner._start_monitor
description: method in skydiscover/runner.py (runner)
metadata:
  type: project
---

# Runner._start_monitor

**File:** `skydiscover/runner.py:292`  
**Kind:** method  
**Layer:** #runner

## Source
````python
    def _start_monitor(self, max_iterations: int):
        if not self.config.monitor.enabled:
            return None
        try:
            from skydiscover.extras.monitor import MonitorServer, create_monitor_callback

            server = MonitorServer(
                host=self.config.monitor.host,
                port=self.config.monitor.port,
                max_solution_length=self.config.monitor.max_solution_length,
            )
            server.set_config_summary(f"{self.name} | max_iter={max_iterations}")
            server.start()

            callback = create_monitor_callback(server, self.database, time.time())
            self.discovery_controller.monitor_callback = callback

            url = f"http://localhost:{server.port}/"
            print(f"\n  Live monitor: {url}\n", flush=True)
            logger.info(f"Live monitor: {url}")
            return server
        except Exception as e:
            logger.warning(f"Failed to start monitor: {e}")
            return None
````

## → Calls
- [[IO-DiscoveryControllerInput.config]]
- [[IO-Runner.run]]
- [[IO-runner.Runner]]

## ← Called by
- [[IO-Runner.run]]
