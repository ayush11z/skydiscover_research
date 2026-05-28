---
name: viewer.find_checkpoint_dir
description: function in skydiscover/extras/monitor/viewer.py (monitor)
metadata:
  type: project
---

# viewer.find_checkpoint_dir

**File:** `skydiscover/extras/monitor/viewer.py:39`  
**Kind:** function  
**Layer:** #monitor

## Source
````python
def find_checkpoint_dir(path: str) -> Optional[str]:
    """Auto-detect the best checkpoint directory from *path*."""
    p = Path(path)

    # 1. Direct checkpoint dir (metadata.json + programs/)
    if (p / "metadata.json").exists() and (p / "programs").is_dir():
        return str(p)

    # 2. programs/ subdir but no metadata
    if (p / "programs").is_dir() and list((p / "programs").glob("*.json")):
        return str(p)

    # 3. checkpoint_N dirs directly inside path
    ckpts = sorted(p.glob("checkpoint_*"), key=lambda x: _ckpt_num(x.name))
    if ckpts:
        return str(ckpts[-1])

    # 4. checkpoints/ subdir
    if (p / "checkpoints").is_dir():
        ckpts = sorted(
            (p / "checkpoints").glob("checkpoint_*"),
            key=lambda x: _ckpt_num(x.name),
        )
        if ckpts:
            return str(ckpts[-1])

    # 5. <subdir>/checkpoints/ (e.g. island/checkpoints/, sequential/checkpoints/)
    for subdir in sorted(p.iterdir()):
        if subdir.is_dir():
            ckpt_dir = subdir / "checkpoints"
            if ckpt_dir.is_dir():
                ckpts = sorted(
                    ckpt_dir.glob("checkpoint_*"),
                    key=lambda x: _ckpt_num(x.name),
                )
                if ckpts:
                    return str(ckpts[-1])

    # 6. Flat directory with JSON program files
    jsons = [j for j in p.glob("*.json") if j.name != "metadata.json"]
    if jsons:
        return str(p)

    return None
````

## → Calls
- [[BenchmarkConfig.name]]
- [[LLMModelConfig.name]]
- [[viewer._ckpt_num]]

## ← Called by
- [[viewer.main]]
