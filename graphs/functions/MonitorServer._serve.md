---
name: MonitorServer._serve
description: method in skydiscover/extras/monitor/server.py (monitor)
metadata:
  type: project
---

# MonitorServer._serve

**File:** `skydiscover/extras/monitor/server.py:277`  
**Kind:** method  
**Layer:** #monitor

## Source
````python
    async def _serve(self) -> None:
        # Try configured port, then auto-increment if already in use
        port = self.port
        for attempt in range(10):
            try:
                server = await asyncio.start_server(self._handle_connection, self.host, port)
                break
            except OSError:
                if attempt == 9:
                    raise
                port += 1
        self.port = port
        async with server:
            self._ready_event.set()  # signal that port is bound
            logger.debug(f"Listening on {self.host}:{self.port}")
            consumer = asyncio.create_task(self._consume_queue())
            hb = asyncio.create_task(self._heartbeat())
            try:
                await asyncio.gather(consumer, hb)
            except (asyncio.CancelledError, RuntimeError):
                pass
            finally:
                try:
                    consumer.cancel()
                    hb.cancel()
                except RuntimeError:
                    pass  # Event loop already closed
````

## → Calls
- [[MonitorServer._consume_queue]]
- [[MonitorServer._handle_connection]]
- [[MonitorServer._heartbeat]]
- [[TaskPool.create_task]]
- [[TaskPool.gather]]

## ← Called by
- [[MonitorServer._run_loop]]
