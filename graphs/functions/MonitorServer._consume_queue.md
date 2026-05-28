---
name: MonitorServer._consume_queue
description: method in skydiscover/extras/monitor/server.py (monitor)
metadata:
  type: project
---

# MonitorServer._consume_queue

**File:** `skydiscover/extras/monitor/server.py:531`  
**Kind:** method  
**Layer:** #monitor

## Source
````python
    async def _consume_queue(self) -> None:
        while not self._stop_event.is_set():
            try:
                event = self._queue.get_nowait()
            except queue.Empty:
                await asyncio.sleep(0.05)
                continue

            etype = event.get("type")
            if etype == "new_program":
                p = event.get("program", {})
                # Annotate with human feedback state for replay on reconnect
                if self._feedback_reader:
                    fb = self._feedback_reader.read()
                    p["human_feedback_active"] = bool(fb)
                else:
                    p["human_feedback_active"] = False
                self._programs.append(p)
                pid = p.get("id", "")
                if "full_solution" in event:
                    self._program_solutions[pid] = event["full_solution"]
                if "parent_full_solution" in event:
                    self._parent_solutions[pid] = event["parent_full_solution"]
                # Independent best tracking: compare scores directly
                new_score = p.get("score", 0)
                if not isinstance(new_score, (int, float)):
                    new_score = 0
                if new_score > self._best_score:
                    self._best_score = new_score
                    self._best_program_id = pid
                    event["is_best"] = True
                elif event.get("is_best"):
                    self._best_program_id = pid
                    self._best_score = max(self._best_score, new_score)
                self._stats = event.get("stats", self._stats)

            # Strip full_solution from broadcast (clients request on demand)
            broadcast = {
                k: v for k, v in event.items() if k not in ("full_solution", "parent_full_solution")
            }
            # Include current human feedback status in program events
            if etype == "new_program" and self._feedback_reader:
                fb = self._feedback_reader.read()
                broadcast["feedback_active"] = bool(fb)
                broadcast["feedback_text"] = fb if fb else ""
                broadcast["human_feedback_mode"] = self._feedback_reader.mode
            await self._broadcast(json.dumps(broadcast))

            # Auto-trigger AI summary every N new programs
            if (
                etype == "new_program"
                and self._summary_interval > 0
                and self._summary_model
                and not self._summary_generating
            ):
                count = len(self._programs)
                if count - self._summary_last_program_count >= self._summary_interval:
                    await self._trigger_summary()
````

## → Calls
- [[HumanFeedbackReader.read]]
- [[LangFuseTracer.get]]
- [[MonitorServer.__init__]]
- [[MonitorServer._broadcast]]
- [[MonitorServer._trigger_summary]]
- [[MonitorServer.set_feedback_reader]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]

## ← Called by
- [[MonitorServer._serve]]
