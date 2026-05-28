---
name: openevolve_backend.run._poll_programs
description: function in skydiscover/extras/external/openevolve_backend.py (external)
metadata:
  type: project
---

# openevolve_backend.run._poll_programs

**File:** `skydiscover/extras/external/openevolve_backend.py:208`  
**Kind:** function  
**Layer:** #external

## Source
````python
        async def _poll_programs():
            _last_feedback = ""
            while True:
                await asyncio.sleep(2)
                # Poll new programs for monitor
                if monitor_callback:
                    try:
                        db = getattr(controller, "database", None)
                        if db is None:
                            continue
                        for pid, p in list(db.programs.items()):
                            if pid not in seen_ids:
                                seen_ids.add(pid)
                                sky_prog = _to_skydiscover_program(p)
                                monitor_callback(sky_prog, getattr(p, "iteration_found", 0))
                    except Exception:
                        logger.debug("Monitor poll error", exc_info=True)
                # Human feedback: inject feedback into OpenEvolve's config
                if feedback_reader:
                    try:
                        feedback = feedback_reader.read()
                        if feedback != _last_feedback:
                            _last_feedback = feedback
                            if feedback:
                                if feedback_reader.mode == "replace":
                                    new_prompt = feedback
                                else:
                                    new_prompt = (
                                        original_sys_prompt + "\n\n## Human Guidance\n" + feedback
                                    )
                            else:
                                new_prompt = original_sys_prompt
                            # Update OpenEvolve's prompt config and model configs
                            if hasattr(oe_config, "prompt"):
                                oe_config.prompt.system_message = new_prompt
                            for m in getattr(oe_config.llm, "models", []):
                                if hasattr(m, "system_message"):
                                    m.system_message = new_prompt
                            feedback_reader.set_current_prompt(new_prompt)
                            if feedback:
                                logger.info(
                                    f"Human feedback injected into OpenEvolve ({len(feedback)} chars, mode={feedback_reader.mode})"
                                )
                    except Exception:
                        logger.debug("Human feedback injection error", exc_info=True)
````

## → Calls
- [[Config.llm]]
- [[HumanFeedbackReader.read]]
- [[HumanFeedbackReader.set_current_prompt]]
- [[openevolve_backend._map_config]]
- [[openevolve_backend._to_skydiscover_program]]

## ← Called by
- [[openevolve_backend.run]]
