---
name: run_discovery._run_with_turn_limit
description: function in skydiscover/search/claude_code/controller.py (claude-code)
metadata:
  type: project
---

# run_discovery._run_with_turn_limit

**File:** `skydiscover/search/claude_code/controller.py:271`  
**Kind:** function  
**Layer:** #claude-code

## Source
````python
            def _run_with_turn_limit() -> None:
                nonlocal cumulative_turns, total_cost_usd, stream_turns
                start = time.monotonic()
                hard_stop_at = 0.0

                with open(log_path, "w") as log_file:
                    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=log_file)
                    try:
                        for raw_line in proc.stdout:
                            log_file.write(raw_line.decode("utf-8", errors="replace"))
                            log_file.flush()

                            try:
                                evt = json.loads(raw_line)
                            except (json.JSONDecodeError, ValueError):
                                continue

                            evt_type = evt.get("type")

                            if evt_type == "assistant":
                                tool_names = [
                                    c.get("name", "")
                                    for c in evt.get("message", {}).get("content", [])
                                    if c.get("type") == "tool_use"
                                ]
                                if tool_names:
                                    stream_turns += 1
                                    elapsed = time.monotonic() - start
                                    _write_progress(
                                        f"Active: {', '.join(tool_names)}"
                                        f" (elapsed {elapsed:.0f}s,"
                                        f" turn {stream_turns}/{max_turns})"
                                    )
                                    if stream_turns > max_turns and not hard_stop_at:
                                        hard_stop_at = time.monotonic()
                                        _write_progress(
                                            f"Hard stop: stream turn {stream_turns}"
                                            f" exceeded {max_turns} -- waiting for result"
                                        )

                            elif evt_type == "result":
                                seg_turns = evt.get("num_turns", 0)
                                cumulative_turns += seg_turns
                                seg_cost = evt.get("total_cost_usd", 0) or 0
                                if seg_cost > total_cost_usd:
                                    total_cost_usd = seg_cost
                                _write_progress(
                                    f"Segment done ({evt.get('subtype', '')}): "
                                    f"+{seg_turns} turns, "
                                    f"{cumulative_turns}/{max_turns} cumulative, "
                                    f"cost=${total_cost_usd:.4f}"
                                )
                                if cumulative_turns >= max_turns or hard_stop_at:
                                    _write_progress("Turn budget reached -- stopping")
                                    proc.kill()
                                    break

                            if hard_stop_at and time.monotonic() - hard_stop_at > 30:
                                _write_progress("Hard stop grace period elapsed -- force killing")
                                proc.kill()
                                break

                            if time.monotonic() - start > wall_timeout:
                                _write_progress(
                                    f"Wall timeout ({wall_timeout}s) exceeded -- stopping"
                                )
                                proc.kill()
                                break
                    finally:
                        proc.wait()
                        # Drain remaining stdout (e.g. result event emitted
                        # just as the hard stop fired).
                        try:
                            for remaining in proc.stdout:
                                log_file.write(remaining.decode("utf-8", errors="replace"))
                                log_file.flush()
                                try:
                                    evt = json.loads(remaining)
                                    if evt.get("type") == "result":
                                        cumulative_turns += evt.get("num_turns", 0)
                                        seg_cost = evt.get("total_cost_usd", 0) or 0
                                        if seg_cost > total_cost_usd:
                                            total_cost_usd = seg_cost
                                except (json.JSONDecodeError, ValueError):
                                    pass
                        except OSError:
                            pass
                        _write_progress(
                            f"Process exited (code {proc.returncode}),"
                            f" cumulative turns: {cumulative_turns}"
                        )
````

## → Calls
- [[ClaudeCodeController._build_docker_cmd]]
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]
- [[run_discovery._write_progress]]

## ← Called by
- [[ClaudeCodeController.run_discovery]]
