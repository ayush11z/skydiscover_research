---
name: viewer._ckpt_num
description: function in skydiscover/extras/monitor/viewer.py (monitor)
metadata:
  type: project
---

# viewer._ckpt_num

**File:** `skydiscover/extras/monitor/viewer.py:32`  
**Kind:** function  
**Layer:** #monitor

## Source
````python
def _ckpt_num(name: str) -> int:
    try:
        return int(name.split("_")[-1])
    except (ValueError, IndexError):
        return 0
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[viewer.find_checkpoint_dir]]
