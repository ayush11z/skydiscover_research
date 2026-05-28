---
name: code_utils._extract_def_info
description: function in skydiscover/utils/code_utils.py (utils)
metadata:
  type: project
---

# code_utils._extract_def_info

**File:** `skydiscover/utils/code_utils.py:87`  
**Kind:** function  
**Layer:** #utils

## Source
````python
def _extract_def_info(solution: str) -> Optional[Tuple[str, str, Optional[str]]]:
    """
    Extract function/class name and docstring (or first comment as fallback) from solution block.

    Returns:
        Tuple of (kind, name, docstring_first_line) or None if not found
    """
    # Look for function definition
    func_match = re.search(r"^\s*def\s+(\w+)\s*\(", solution, re.MULTILINE)
    if func_match:
        name = func_match.group(1)
        # Try to extract docstring, fallback to first comment
        docstring = _extract_docstring(solution, func_match.end())
        if not docstring:
            docstring = _extract_first_comment(solution, func_match.start())
        return ("function", name, docstring)

    # Look for class definition
    class_match = re.search(r"^\s*class\s+(\w+)", solution, re.MULTILINE)
    if class_match:
        name = class_match.group(1)
        docstring = _extract_docstring(solution, class_match.end())
        if not docstring:
            docstring = _extract_first_comment(solution, class_match.start())
        return ("class", name, docstring)

    return None
````

## → Calls
- [[Config.search]]
- [[MonitorServer.start]]
- [[code_utils._extract_docstring]]
- [[code_utils._extract_first_comment]]
- [[search_strategy_evaluator.start]]

## ← Called by
- [[code_utils.format_diff_summary]]
