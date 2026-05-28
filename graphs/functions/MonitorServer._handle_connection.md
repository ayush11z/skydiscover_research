---
name: MonitorServer._handle_connection
description: method in skydiscover/extras/monitor/server.py (monitor)
metadata:
  type: project
---

# MonitorServer._handle_connection

**File:** `skydiscover/extras/monitor/server.py:305`  
**Kind:** method  
**Layer:** #monitor

## Source
````python
    async def _handle_connection(
        self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter
    ) -> None:
        """Route an incoming connection to HTTP or WebSocket handler."""
        try:
            # Read HTTP request line + headers
            raw_headers: Dict[str, str] = {}
            request_line = (await reader.readline()).decode("utf-8", errors="replace").strip()
            if not request_line:
                writer.close()
                return

            while True:
                line = (await reader.readline()).decode("utf-8", errors="replace").strip()
                if not line:
                    break
                if ":" in line:
                    k, _, v = line.partition(":")
                    raw_headers[k.strip().lower()] = v.strip()

            is_ws = raw_headers.get("upgrade", "").lower() == "websocket"

            if is_ws:
                await self._handle_ws(reader, writer, raw_headers)
            else:
                await self._handle_http(writer)
        except Exception:
            logger.debug("Connection handler error", exc_info=True)
        finally:
            try:
                writer.close()
            except Exception:
                logger.debug("Error closing writer", exc_info=True)
````

## → Calls
- [[ContainerizedEvaluator.close]]
- [[DiscoveryController.close]]
- [[Evaluator.close]]
- [[MonitorServer._handle_http]]
- [[MonitorServer._handle_ws]]

## ← Called by
- [[MonitorServer._serve]]
