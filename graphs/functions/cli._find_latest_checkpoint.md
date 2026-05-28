---
name: cli._find_latest_checkpoint
description: function in skydiscover/cli.py (cli)
metadata:
  type: project
---

# cli._find_latest_checkpoint

**File:** `skydiscover/cli.py:299`  
**Kind:** function  
**Layer:** #cli

## Source
````python
def _find_latest_checkpoint(checkpoint_dir: str) -> Optional[str]:
    """Return the path of the latest checkpoint directory named like ``checkpoint_<n>``."""
    if not os.path.isdir(checkpoint_dir):
        return None

    def parse_iteration(path: str) -> Optional[int]:
        try:
            return int(path.rsplit("_", 1)[-1])
        except (ValueError, IndexError):
            return None

    candidates = []
    for name in os.listdir(checkpoint_dir):
        full_path = os.path.join(checkpoint_dir, name)
        if not os.path.isdir(full_path):
            continue
        iteration = parse_iteration(name)
        if iteration is None:
            continue
        candidates.append((iteration, full_path))

    if not candidates:
        return None

    return max(candidates, key=lambda item: item[0])[1]
````

## → Calls
- [[_find_latest_checkpoint.parse_iteration]]

## ← Called by
- [[cli.main_async]]
