---
name: prepare.cleanup_temp
description: function in skydiscover/utils/prepare.py (utils)
metadata:
  type: project
---

# prepare.cleanup_temp

**File:** `skydiscover/utils/prepare.py:88`  
**Kind:** function  
**Layer:** #utils

## Source
````python
def cleanup_temp(temp_files: List[str], temp_dir: Optional[str]) -> None:
    """Best-effort removal of temporary files and directories."""
    for path in temp_files:
        try:
            os.unlink(path)
        except OSError as exc:
            logger.warning("Failed to delete temp file %s: %s", path, exc)
    if temp_dir and os.path.exists(temp_dir):
        try:
            shutil.rmtree(temp_dir)
        except OSError as exc:
            logger.warning("Failed to delete temp directory %s: %s", temp_dir, exc)
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[api._run_discovery_async]]
