---
name: Runner._install_signal_handlers
description: method in skydiscover/runner.py (runner)
metadata:
  type: project
---

# Runner._install_signal_handlers

**File:** `skydiscover/runner.py:361`  
**Kind:** method  
**Layer:** #runner

## Source
````python
    def _install_signal_handlers(self) -> None:
        def on_signal(signum, frame):
            logger.info(f"Signal {signum} received, shutting down...")
            if self.discovery_controller is not None:
                self.discovery_controller.request_shutdown()

            def force_exit(signum, frame):
                sys.exit(128 + signum)

            # After the first termination signal, ensure subsequent SIGINT/SIGTERM
            # cause an immediate exit instead of re-running the soft handler.
            signal.signal(signal.SIGINT, force_exit)
            signal.signal(signal.SIGTERM, force_exit)

        signal.signal(signal.SIGINT, on_signal)
        signal.signal(signal.SIGTERM, on_signal)
````

## → Calls
- [[_install_signal_handlers.on_signal]]

## ← Called by
- [[Runner.run]]
