---
name: IN-AgenticGenerator.generate
description: method in skydiscover/llm/agentic_generator.py (llm)
metadata:
  type: project
---

# AgenticGenerator.generate

**File:** `skydiscover/llm/agentic_generator.py:62`  
**Kind:** method  
**Layer:** #llm

## Source
````python
    async def generate(self, system_message: str, user_message: str) -> Optional[str]:
        """Run the agent loop. Returns generated text, or None on failure."""
        cfg = self.config
        files_read: set = set()
        conversation: List[Dict[str, Any]] = []
        t0 = time.time()

        sys_prompt = f"{system_message}\n\n{_AGENTIC_SYSTEM_PROMPT}"
        repo_map = build_repo_map(
            cfg.codebase_root,
            max_depth=cfg.repo_map_max_depth,
            allowed_extensions=cfg.allowed_extensions,
            excluded_dirs=cfg.excluded_dirs,
        )

        user_parts = [user_message]
        if repo_map:
            user_parts.append(f"\n## Project structure\n```\n{repo_map}\n```")
        conversation.append({"role": "user", "content": "\n".join(user_parts)})

        for step in range(cfg.max_steps):
            if time.time() - t0 > cfg.overall_timeout:
                logger.warning("Agent timed out at step %d", step)
                break

            if _context_chars(sys_prompt, conversation) > cfg.max_context_chars:
                conversation.append(
                    {
                        "role": "user",
                        "content": "Context limit reached. Output your improved program now.",
                    }
                )

            try:
                assistant_msg = await asyncio.wait_for(
                    self._call_llm(sys_prompt, conversation),
                    timeout=cfg.per_step_timeout,
                )
            except asyncio.TimeoutError:
                logger.warning("Step %d: LLM timed out", step)
                conversation.append(
                    {
                        "role": "user",
                        "content": "Timed out. Output your solution or try a simpler action.",
                    }
                )
                continue
            except Exception as e:
                logger.error("Step %d: LLM error: %s", step, e)
                break

            tool_calls = assistant_msg.get("tool_calls", [])
            text_content = assistant_msg.get("content", "").strip()
            conversation.append(assistant_msg)

            if not tool_calls:
                if text_content:
                    logger.info(
                        "Agent produced text at step %d (%d files read)", step, len(files_read)
                    )
                    return text_content
                conversation.append(
                    {
                        "role": "user",
                        "content": "Use a tool to explore, or output your improved program.",
                    }
                )
                continue

            for tc in tool_calls:
                fn = tc.get("function", {})
                name, raw, tc_id = fn.get("name", ""), fn.get("arguments", "{}"), tc.get("id", "")

                try:
                    args = json.loads(raw)
                except (json.JSONDecodeError, TypeError) as e:
                    conversation.append(
                        {"role": "tool", "tool_call_id": tc_id, "content": f"Bad JSON: {e}"}
                    )
                    continue

                logger.info(
                    "Step %d: tool=%s args=%s",
                    step,
                    name,
                    {
                        k: (v[:80] + "...") if isinstance(v, str) and len(v) > 80 else v
                        for k, v in args.items()
                    },
                )

                result = self._run_tool(name, args, files_read)
                conversation.append(
                    {"role": "tool", "tool_call_id": tc_id, "content": result["content"]}
                )

        logger.warning("Agent loop ended without producing code")
        return None
````

## → Calls
- [[IN-AgenticGenerator.__init__]]
- [[IN-AgenticGenerator._call_llm]]
- [[IN-AgenticGenerator._run_tool]]
- [[IN-agentic_generator._context_chars]]
- [[IN-code_utils.build_repo_map]]

## ← Called by
- [[IN-DiscoveryController._call_llm]]
