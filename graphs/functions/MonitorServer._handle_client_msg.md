---
name: MonitorServer._handle_client_msg
description: method in skydiscover/extras/monitor/server.py (monitor)
metadata:
  type: project
---

# MonitorServer._handle_client_msg

**File:** `skydiscover/extras/monitor/server.py:387`  
**Kind:** method  
**Layer:** #monitor

## Source
````python
    async def _handle_client_msg(self, writer: asyncio.StreamWriter, raw: str) -> None:
        """Dispatch an incoming WebSocket JSON message from a dashboard client."""
        try:
            msg = json.loads(raw)
        except Exception:
            return
        t = msg.get("type")
        if t == "request_full_state":
            await self._ws_send(writer, json.dumps(self._build_init_state()))
        elif t == "request_program_solution":
            pid = msg.get("program_id", "")
            await self._ws_send(
                writer,
                json.dumps(
                    {
                        "type": "program_solution",
                        "program_id": pid,
                        "solution": self._program_solutions.get(pid, "")[
                            : self.max_solution_length
                        ],
                        "parent_solution": self._parent_solutions.get(pid, "")[
                            : self.max_solution_length
                        ],
                    }
                ),
            )
        elif t == "set_feedback":
            text = msg.get("text", "").strip()
            if self._feedback_reader:
                self._feedback_reader.write_from_dashboard(text)
                ack = {
                    "type": "feedback_ack",
                    "feedback_text": text,
                    "feedback_active": bool(text),
                    "human_feedback_mode": self._feedback_reader.mode,
                }
                await self._broadcast(json.dumps(ack))
                logger.info(f"Human feedback set from dashboard ({len(text)} chars)")
            else:
                await self._ws_send(
                    writer,
                    json.dumps(
                        {
                            "type": "feedback_ack",
                            "feedback_text": "",
                            "feedback_active": False,
                            "error": "Human feedback not enabled",
                        }
                    ),
                )
        elif t == "clear_feedback":
            if self._feedback_reader:
                self._feedback_reader.write_from_dashboard("")
                ack = {
                    "type": "feedback_ack",
                    "feedback_text": "",
                    "feedback_active": False,
                    "human_feedback_mode": self._feedback_reader.mode,
                }
                await self._broadcast(json.dumps(ack))
                logger.info("Human feedback cleared from dashboard")
        elif t == "request_feedback_state":
            await self._ws_send(
                writer,
                json.dumps(
                    {
                        "type": "feedback_ack",
                        **self._get_feedback_state(),
                    }
                ),
            )
        elif t == "set_human_feedback_mode":
            mode = msg.get("mode", "append")
            if self._feedback_reader:
                self._feedback_reader.set_mode(mode)
                ack = {
                    "type": "human_feedback_mode_ack",
                    "human_feedback_mode": mode,
                }
                await self._broadcast(json.dumps(ack))
                logger.info(f"Human feedback mode set to: {mode}")
        elif t == "request_system_prompt":
            prompt_text = ""
            if self._feedback_reader:
                prompt_text = self._feedback_reader.get_current_prompt()
            await self._ws_send(
                writer,
                json.dumps(
                    {
                        "type": "system_prompt",
                        "prompt_text": prompt_text,
                    }
                ),
            )
        elif t == "request_human_feedback_history":
            history = []
            if self._feedback_reader:
                history = self._feedback_reader.get_history()
            await self._ws_send(
                writer,
                json.dumps(
                    {
                        "type": "human_feedback_history",
                        "history": history,
                    }
                ),
            )
        elif t == "request_image":
            image_path = msg.get("image_path", "")
            program_id = msg.get("program_id", "")
            if image_path and os.path.exists(image_path):
                try:
                    import base64 as _b64

                    with open(image_path, "rb") as _f:
                        img_data = _b64.b64encode(_f.read()).decode()
                    ext = os.path.splitext(image_path)[1].lstrip(".").lower()
                    mime = {
                        "png": "image/png",
                        "jpg": "image/jpeg",
                        "jpeg": "image/jpeg",
                        "webp": "image/webp",
                        "gif": "image/gif",
                    }.get(ext, "image/png")
                    await self._ws_send(
                        writer,
                        json.dumps(
                            {
                                "type": "image_data",
                                "program_id": program_id,
                                "data_url": f"data:{mime};base64,{img_data}",
                            }
                        ),
                    )
                except Exception as e:
                    logger.warning(f"Failed to serve image {image_path}: {e}")
        elif t == "request_program_summary":
            pid = msg.get("program_id", "")
            await self._generate_program_summary(writer, pid)
        elif t == "request_summary":
            await self._trigger_summary()
````

## → Calls
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]
- [[HumanFeedbackReader.get_current_prompt]]
- [[HumanFeedbackReader.get_history]]
- [[HumanFeedbackReader.set_mode]]
- [[HumanFeedbackReader.write_from_dashboard]]
- [[LangFuseTracer.get]]
- [[MonitorServer.__init__]]
- [[MonitorServer._broadcast]]
- [[MonitorServer._build_init_state]]
- [[MonitorServer._generate_program_summary]]
- [[MonitorServer._get_feedback_state]]
- [[MonitorServer._trigger_summary]]
- [[MonitorServer._ws_send]]
- [[MonitorServer.set_feedback_reader]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]

## ← Called by
- [[MonitorServer._handle_ws]]
