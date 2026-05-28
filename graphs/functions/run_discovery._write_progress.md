---
name: run_discovery._write_progress
description: function in skydiscover/search/claude_code/controller.py (claude-code)
metadata:
  type: project
---

# run_discovery._write_progress

**File:** `skydiscover/search/claude_code/controller.py:251`  
**Kind:** function  
**Layer:** #claude-code

## Source
````python
            def _write_progress(line: str) -> None:
                ts = time.strftime("%H:%M:%S")
                entry = f"[{ts}] {line}"
                logger.info(entry)
                if progress_log:
                    with _progress_lock:
                        with open(progress_log, "a") as f:
                            f.write(entry + "\n")
````

## → Calls
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]

## ← Called by
- [[ClaudeCodeController.run_discovery]]
- [[run_discovery._run_with_turn_limit]]
