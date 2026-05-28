---
name: MonitorServer._generate_program_summary
description: method in skydiscover/extras/monitor/server.py (monitor)
metadata:
  type: project
---

# MonitorServer._generate_program_summary

**File:** `skydiscover/extras/monitor/server.py:611`  
**Kind:** method  
**Layer:** #monitor

## Source
````python
    async def _generate_program_summary(self, writer: asyncio.StreamWriter, pid: str) -> None:
        """Generate a crisp LLM summary of what changed in a single program."""
        # Return cached if available
        if pid in self._program_summary_cache:
            await self._ws_send(
                writer,
                json.dumps(
                    {
                        "type": "program_summary",
                        "program_id": pid,
                        "summary": self._program_summary_cache[pid],
                    }
                ),
            )
            return

        # Need API key + model
        if not self._summary_model or not self._summary_api_key:
            await self._ws_send(
                writer,
                json.dumps(
                    {
                        "type": "program_summary",
                        "program_id": pid,
                        "summary": "AI summary not configured.",
                    }
                ),
            )
            return

        # Find program data
        prog = None
        for p in self._programs:
            if p.get("id") == pid:
                prog = p
                break
        if not prog:
            return

        # Build prompt
        code = self._program_solutions.get(pid, prog.get("solution_snippet", ""))
        parent_solution = self._parent_solutions.get(pid, "")
        score = prog.get("score", "?")
        parent_score = prog.get("parent_score")
        label = prog.get("label_type", "unknown")

        delta_str = ""
        if isinstance(score, (int, float)) and isinstance(parent_score, (int, float)):
            d = score - parent_score
            delta_str = f" (delta: {'+' if d >= 0 else ''}{d:.4f})"

        # Truncate code for prompt efficiency
        if len(code) > 2000:
            code = code[:2000] + "\n... (truncated)"
        if len(parent_solution) > 2000:
            parent_solution = parent_solution[:2000] + "\n... (truncated)"

        is_image_mode = prog.get("image_path") is not None

        if is_image_mode:
            system = (
                "You are analyzing one step in an image generation run. "
                "Given the parent generation prompt and the child generation prompt, describe in 1-2 concise bullet points "
                "what specifically changed in the prompt.\n\n"
                "Rules:\n"
                "- Be specific: name style changes, subject modifications, added details\n"
                "- Each bullet under 25 words\n"
                "- Start each bullet with `- `\n"
                "- No headers, no sections — just 1-2 bullets"
            )
        else:
            system = (
                "You are analyzing one step in a solution discovery run. "
                "Given the parent code and the child code, describe in 1-2 concise bullet points "
                "what specifically changed.\n\n"
                "Rules:\n"
                "- Be specific: name algorithms, parameters, structural changes\n"
                "- Each bullet under 25 words\n"
                "- Start each bullet with `- `\n"
                "- No headers, no sections — just 1-2 bullets\n"
                "- Consider the evolution label: exploration = trying new ideas, "
                "exploitation = refining current best, diverge = deliberately different strategy"
            )

        content_label = "prompt" if is_image_mode else "code"
        user_parts = [f"Label: {label}{delta_str}"]
        if parent_score is not None:
            user_parts.append(f"Score: {parent_score} -> {score}")
        else:
            user_parts.append(f"Score: {score} (no parent)")

        if parent_solution:
            user_parts.append(f"\nParent {content_label}:\n```\n{parent_solution}\n```")
        user_parts.append(f"\nNew {content_label}:\n```\n{code}\n```")

        prompt_data = {"system": system, "user": "\n".join(user_parts)}

        # Ensure executor exists
        if not self._summary_executor:
            self._summary_executor = ThreadPoolExecutor(max_workers=1, thread_name_prefix="summary")

        # Run LLM call in executor
        result = ""
        loop = asyncio.get_running_loop()
        try:
            result = await loop.run_in_executor(
                self._summary_executor,
                self._call_program_summary_api,
                prompt_data,
            )
            self._program_summary_cache[pid] = result
        except Exception as e:
            logger.warning(f"Program summary failed for {pid[:8]}: {e}", exc_info=True)
            result = f"Summary unavailable: {e}"

        await self._ws_send(
            writer,
            json.dumps(
                {
                    "type": "program_summary",
                    "program_id": pid,
                    "summary": result or "Summary unavailable (empty response).",
                }
            ),
        )
````

## → Calls
- [[LangFuseTracer.get]]
- [[MonitorServer.__init__]]
- [[MonitorServer._call_program_summary_api]]
- [[MonitorServer._ws_send]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]

## ← Called by
- [[MonitorServer._handle_client_msg]]
