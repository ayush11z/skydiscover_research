---
name: MonitorServer._trigger_summary
description: method in skydiscover/extras/monitor/server.py (monitor)
metadata:
  type: project
---

# MonitorServer._trigger_summary

**File:** `skydiscover/extras/monitor/server.py:741`  
**Kind:** method  
**Layer:** #monitor

## Source
````python
    async def _trigger_summary(self) -> None:
        """Trigger async AI summary generation."""
        if not self._summary_model:
            await self._broadcast(
                json.dumps(
                    {
                        "type": "summary_update",
                        "summary_text": "AI summary not configured (no model set).",
                        "summary_generating": False,
                        "summary_enabled": False,
                    }
                )
            )
            return
        if not self._summary_api_key:
            await self._broadcast(
                json.dumps(
                    {
                        "type": "summary_update",
                        "summary_text": "AI summary not configured. Set OPENAI_API_KEY environment variable or summary_api_key in config.",
                        "summary_generating": False,
                        "summary_enabled": False,
                    }
                )
            )
            return
        if self._summary_generating:
            return  # Already in progress

        # Ensure executor exists
        if not self._summary_executor:
            self._summary_executor = ThreadPoolExecutor(max_workers=1, thread_name_prefix="summary")

        self._summary_generating = True
        self._summary_last_program_count = len(self._programs)

        # Notify clients that generation started
        await self._broadcast(
            json.dumps(
                {
                    "type": "summary_update",
                    "summary_text": self._summary_text,
                    "summary_generating": True,
                    "summary_enabled": True,
                }
            )
        )

        try:
            # Build the prompt data from current programs
            top_programs = self._get_top_k_programs()
            if not top_programs:
                self._summary_text = "No scored programs yet. Run some iterations first."
                logger.info("AI summary skipped: no scored programs")
            else:
                prompt_data = self._build_summary_prompt(top_programs)
                logger.info(
                    f"AI summary: calling {self._summary_model} with {len(top_programs)} "
                    f"top programs, api_base={self._summary_api_base}"
                )

                # Run the blocking API call in a thread
                loop = asyncio.get_running_loop()
                result = await loop.run_in_executor(
                    self._summary_executor,
                    self._call_llm_api,
                    prompt_data,
                )
                self._summary_text = result or "AI returned empty response."
                logger.info(f"AI summary generated ({len(self._summary_text)} chars)")
        except Exception as e:
            logger.warning(f"AI summary generation failed: {e}", exc_info=True)
            self._summary_text = f"Summary generation failed: {e}"
        finally:
            self._summary_generating = False

        # Broadcast the result
        await self._broadcast(
            json.dumps(
                {
                    "type": "summary_update",
                    "summary_text": self._summary_text,
                    "summary_generating": False,
                    "summary_enabled": True,
                }
            )
        )
````

## → Calls
- [[MonitorServer._broadcast]]
- [[MonitorServer._build_summary_prompt]]
- [[MonitorServer._call_llm_api]]
- [[MonitorServer._get_top_k_programs]]

## ← Called by
- [[MonitorServer._consume_queue]]
- [[MonitorServer._handle_client_msg]]
