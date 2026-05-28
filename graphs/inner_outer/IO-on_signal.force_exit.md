---
name: IO-on_signal.force_exit
description: function in skydiscover/runner.py (runner)
metadata:
  type: project
---

# on_signal.force_exit

**File:** `skydiscover/runner.py:367`  
**Kind:** function  
**Layer:** #runner

## Source
````python
            def force_exit(signum, frame):
                sys.exit(128 + signum)
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-_install_signal_handlers.on_signal]]
