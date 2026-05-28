---
name: _find_latest_checkpoint.parse_iteration
description: function in skydiscover/cli.py (cli)
metadata:
  type: project
---

# _find_latest_checkpoint.parse_iteration

**File:** `skydiscover/cli.py:304`  
**Kind:** function  
**Layer:** #cli

## Source
````python
    def parse_iteration(path: str) -> Optional[int]:
        try:
            return int(path.rsplit("_", 1)[-1])
        except (ValueError, IndexError):
            return None
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[cli._find_latest_checkpoint]]
