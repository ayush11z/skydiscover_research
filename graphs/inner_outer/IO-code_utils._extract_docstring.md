---
name: IO-code_utils._extract_docstring
description: function in skydiscover/utils/code_utils.py (utils)
metadata:
  type: project
---

# code_utils._extract_docstring

**File:** `skydiscover/utils/code_utils.py:150`  
**Kind:** function  
**Layer:** #utils

## Source
````python
def _extract_docstring(solution: str, start_pos: int) -> Optional[str]:
    """
    Extract first line of docstring after a given position.

    Args:
        solution: Source code
        start_pos: Position to start searching from
    """
    remaining = solution[start_pos:]
    docstring_match = re.search(r':\s*\n\s*("""|\'\'\')(.*?)("""|\'\'\')', remaining, re.DOTALL)

    if docstring_match:
        docstring_content = docstring_match.group(2).strip()
        return docstring_content.split("\n")[0].strip()

    return None
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-code_utils._extract_def_info]]
