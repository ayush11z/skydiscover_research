---
name: shinkaevolve_backend.run._poll_programs
description: function in skydiscover/extras/external/shinkaevolve_backend.py (external)
metadata:
  type: project
---

# shinkaevolve_backend.run._poll_programs

**File:** `skydiscover/extras/external/shinkaevolve_backend.py:220`  
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
                        all_progs = runner.db.get_all_programs()
                        for p in all_progs:
                            if p.id not in seen_ids:
                                seen_ids.add(p.id)
                                sky_prog = _to_skydiscover_program(p)
                                monitor_callback(sky_prog, getattr(p, "generation", 0))
                    except Exception:
                        logger.debug("Monitor poll error", exc_info=True)
                # Human feedback: inject feedback into ShinkaEvolve's prompt sampler
                if feedback_reader:
                    try:
                        feedback = feedback_reader.read()
                        if feedback != _last_feedback:
                            _last_feedback = feedback
                            sampler = getattr(runner, "prompt_sampler", None)
                            original_prompt = evo_config.task_sys_msg or ""
                            if feedback and sampler:
                                if feedback_reader.mode == "replace":
                                    sampler.task_sys_msg = feedback
                                else:
                                    sampler.task_sys_msg = (
                                        original_prompt + "\n\n## Human Guidance\n" + feedback
                                    )
                                feedback_reader.set_current_prompt(sampler.task_sys_msg)
                                logger.info(
                                    f"Human feedback injected into ShinkaEvolve ({len(feedback)} chars, mode={feedback_reader.mode})"
                                )
                            elif sampler and not feedback:
                                # Feedback cleared — revert to original
                                sampler.task_sys_msg = original_prompt
                                feedback_reader.set_current_prompt(original_prompt)
                    except Exception:
                        logger.debug("Human feedback injection error", exc_info=True)
````

## → Calls
- [[HumanFeedbackReader.read]]
- [[HumanFeedbackReader.set_current_prompt]]
- [[Program.id]]
- [[shinkaevolve_backend._map_config]]
- [[shinkaevolve_backend._to_skydiscover_program]]

## ← Called by
- [[shinkaevolve_backend.run]]
