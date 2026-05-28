---
name: MonitorServer._run_loop
description: method in skydiscover/extras/monitor/server.py (monitor)
metadata:
  type: project
---

# MonitorServer._run_loop

**File:** `skydiscover/extras/monitor/server.py:253`  
**Kind:** method  
**Layer:** #monitor

## Source
````python
    def _run_loop(self) -> None:
        self._loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self._loop)
        try:
            self._loop.run_until_complete(self._serve())
        except (RuntimeError, asyncio.CancelledError):
            pass  # Normal on shutdown
        except Exception:
            logger.exception("Monitor server error")
        finally:
            # Drain any remaining cancelled tasks so they don't warn on GC
            try:
                pending = asyncio.all_tasks(self._loop)
                if pending:
                    for t in pending:
                        t.cancel()
                    self._loop.run_until_complete(asyncio.gather(*pending, return_exceptions=True))
            except Exception:
                logger.debug("Error cancelling tasks during stop", exc_info=True)
            try:
                self._loop.close()
            except Exception:
                logger.debug("Error closing event loop", exc_info=True)
````

## → Calls
- [[ContainerizedEvaluator.close]]
- [[DiscoveryController.close]]
- [[Evaluator.close]]
- [[MonitorServer._serve]]
- [[TaskPool.gather]]

## ← Called by
- [[MonitorServer.start]]
