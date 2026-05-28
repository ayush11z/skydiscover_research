---
name: IO-code_utils.build_repo_map
description: function in skydiscover/utils/code_utils.py (utils)
metadata:
  type: project
---

# code_utils.build_repo_map

**File:** `skydiscover/utils/code_utils.py:265`  
**Kind:** function  
**Layer:** #utils

## Source
````python
def build_repo_map(
    root: str,
    *,
    max_depth: int = 4,
    allowed_extensions: Tuple[str, ...] = (".py",),
    excluded_dirs: Tuple[str, ...] = (".git", "__pycache__"),
) -> str:
    """Return a depth-limited directory tree of *root* as a string.

    Only files whose extension is in *allowed_extensions* are included.
    Directories in *excluded_dirs* (and hidden directories) are skipped.
    Returns an empty string if *root* does not exist or is not a directory.
    """
    if not root or not os.path.isdir(root):
        return ""

    root_path = Path(root).resolve()
    excluded: Set[str] = set(excluded_dirs)
    allowed: Set[str] = set(allowed_extensions)
    lines: List[str] = []

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

    walk(root_path, "  ", 0)
    return "\n".join(lines)
````

## → Calls
- [[IO-build_repo_map.walk]]

## ← Called by
- [[IO-AgenticGenerator.generate]]
