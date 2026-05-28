---
name: IO-_install_signal_handlers.on_signal
description: function in skydiscover/runner.py (runner)
metadata:
  type: project
---

# _install_signal_handlers.on_signal

**File:** `skydiscover/runner.py:362`  
**Kind:** function  
**Layer:** #runner

## Source
````python
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
````

## → Calls
- [[IO-DiscoveryController.request_shutdown]]
- [[IO-Runner.run]]
- [[IO-on_signal.force_exit]]

## ← Called by
- [[IO-Runner._install_signal_handlers]]
