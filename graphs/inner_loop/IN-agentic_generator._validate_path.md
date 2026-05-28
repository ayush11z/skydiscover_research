---
name: IN-agentic_generator._validate_path
description: function in skydiscover/llm/agentic_generator.py (llm)
metadata:
  type: project
---

# agentic_generator._validate_path

**File:** `skydiscover/llm/agentic_generator.py:434`  
**Kind:** function  
**Layer:** #llm

## Source
````python
def _validate_path(
    requested: str, root: str, allowed_ext: tuple, excluded_dirs: tuple
) -> Tuple[bool, str, str]:
    """Validate a file path. Returns (ok, resolved_path, error_message)."""
    try:
        resolved = os.path.realpath(requested)
    except (OSError, ValueError) as e:
        return False, "", f"Invalid path: {e}"

    root_abs = os.path.realpath(root)
    if not resolved.startswith(root_abs + os.sep) and resolved != root_abs:
        return False, "", "Path outside codebase root."

    try:
        rel = os.path.relpath(resolved, root_abs)
        for part in Path(rel).parts:
            if part in excluded_dirs:
                return False, "", f"Path in excluded directory '{part}'."
    except ValueError:
        pass

    basename = os.path.basename(resolved).lower()
    if basename in _SENSITIVE_FILENAMES:
        return False, "", f"Access denied: '{basename}' may contain secrets."

    if not os.path.isfile(resolved):
        parent_dir = os.path.dirname(resolved)
        if os.path.isdir(parent_dir):
            try:
                siblings = sorted(os.listdir(parent_dir))[:15]
                rel_dir = os.path.relpath(parent_dir, root_abs)
                return (
                    False,
                    "",
                    f"Not found: '{os.path.basename(resolved)}'. '{rel_dir}/' contains: {siblings}",
                )
            except OSError:
                pass
        return False, "", f"File not found: '{requested}'."

    ext = os.path.splitext(resolved)[1].lower()
    if ext not in allowed_ext:
        return False, "", f"Extension '{ext}' not allowed."

    return True, resolved, ""
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IN-AgenticGenerator._tool_read_file]]
