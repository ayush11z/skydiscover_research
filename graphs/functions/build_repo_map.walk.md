---
name: build_repo_map.walk
description: function in skydiscover/utils/code_utils.py (utils)
metadata:
  type: project
---

# build_repo_map.walk

**File:** `skydiscover/utils/code_utils.py:286`  
**Kind:** function  
**Layer:** #utils

## Source
````python
    def walk(directory: Path, prefix: str, depth: int) -> None:
        if depth > max_depth:
            return
        try:
            entries = sorted(directory.iterdir(), key=lambda p: (p.is_file(), p.name))
        except PermissionError:
            return
        for entry in entries:
            if entry.name.startswith(".") or entry.name in excluded:
                continue
            if entry.is_dir():
                lines.append(f"{prefix}{entry.name}/")
                walk(entry, prefix + "  ", depth + 1)
            elif entry.suffix in allowed:
                lines.append(f"{prefix}{entry.name}")
````

## → Calls
- [[BenchmarkConfig.name]]
- [[LLMModelConfig.name]]

## ← Called by
- [[AgenticGenerator._tool_search]]
- [[code_utils.build_repo_map]]
