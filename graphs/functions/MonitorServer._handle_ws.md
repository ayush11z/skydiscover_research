---
name: MonitorServer._handle_ws
description: method in skydiscover/extras/monitor/server.py (monitor)
metadata:
  type: project
---

# MonitorServer._handle_ws

**File:** `skydiscover/extras/monitor/server.py:352`  
**Kind:** method  
**Layer:** #monitor

## Source
````python
    async def _handle_ws(
        self,
        reader: asyncio.StreamReader,
        writer: asyncio.StreamWriter,
        headers: Dict[str, str],
    ) -> None:
        """Complete the WebSocket handshake and enter the read loop."""
        key = headers.get("sec-websocket-key", "")
        accept = _ws_accept_key(key)
        handshake = (
            "HTTP/1.1 101 Switching Protocols\r\n"
            "Upgrade: websocket\r\n"
            "Connection: Upgrade\r\n"
            f"Sec-WebSocket-Accept: {accept}\r\n"
            "\r\n"
        ).encode()
        writer.write(handshake)
        await writer.drain()

        self._clients.add(writer)
        logger.debug(f"WS client connected ({len(self._clients)} total)")
        try:
            await self._ws_send(writer, json.dumps(self._build_init_state()))
            # Read loop
            while True:
                text = await _ws_read_frame(reader)
                if text is None:
                    break
                await self._handle_client_msg(writer, text)
        except Exception:
            logger.debug("WebSocket handler error", exc_info=True)
        finally:
            self._clients.discard(writer)
            logger.debug(f"WS client disconnected ({len(self._clients)} total)")
````

## → Calls
- [[LangFuseTracer.get]]
- [[MonitorServer._build_init_state]]
- [[MonitorServer._handle_client_msg]]
- [[MonitorServer._ws_send]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]
- [[server._ws_accept_key]]
- [[server._ws_read_frame]]

## ← Called by
- [[MonitorServer._handle_connection]]
