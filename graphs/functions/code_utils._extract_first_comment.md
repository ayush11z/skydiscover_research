---
name: code_utils._extract_first_comment
description: function in skydiscover/utils/code_utils.py (utils)
metadata:
  type: project
---

# code_utils._extract_first_comment

**File:** `skydiscover/utils/code_utils.py:116`  
**Kind:** function  
**Layer:** #utils

## Source
````python
def _extract_first_comment(solution: str, func_start: int) -> Optional[str]:
    """
    Extract consecutive comment lines inside a function/class body.
    Used as fallback when no docstring is available.
    Returns up to 5 lines of comments joined together.
    """
    remaining = solution[func_start:]
    colon_match = re.search(r"(?:\)|[^:]+):\s*\n", remaining)
    if not colon_match:
        return None

    # Get the body after the colon
    body_start = colon_match.end()
    body = remaining[body_start:]

    # Collect consecutive comment lines
    comment_lines = []
    lines = body.split("\n")
    for line in lines[:10]:  # Check first 10 lines for comments
        stripped = line.strip()
        if stripped.startswith("#"):
            # Remove the # and leading space
            comment_text = stripped[1:].strip()
            if comment_text:
                comment_lines.append(comment_text)
            if len(comment_lines) >= 5:  # Max 5 lines
                break
        elif stripped and not stripped.startswith("#"):
            # Hit actual code, stop collecting
            break

    return "\n".join(comment_lines) if comment_lines else None
````

## → Calls
- [[Config.search]]

## ← Called by
- [[code_utils._extract_def_info]]
