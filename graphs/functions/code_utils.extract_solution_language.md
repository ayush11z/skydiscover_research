---
name: code_utils.extract_solution_language
description: function in skydiscover/utils/code_utils.py (utils)
metadata:
  type: project
---

# code_utils.extract_solution_language

**File:** `skydiscover/utils/code_utils.py:238`  
**Kind:** function  
**Layer:** #utils

## Source
````python
def extract_solution_language(solution: str) -> str:
    """
    Try to determine the language of a solution snippet in string format

    Args:
        solution: Solution snippet

    Returns:
        Detected language or "text" by default if no language is detected
    """
    # Look for common language signatures
    if re.search(r"^(import|from|def|class)\s", solution, re.MULTILINE):
        return "python"
    elif re.search(r"^(package|import java|public class)", solution, re.MULTILINE):
        return "java"
    elif re.search(r"^(#include|int main|void main)", solution, re.MULTILINE):
        return "cpp"
    elif re.search(r"^(function|var|let|const|console\.log)", solution, re.MULTILINE):
        return "javascript"
    elif re.search(r"^(module|fn|let mut|impl)", solution, re.MULTILINE):
        return "rust"
    elif re.search(r"^(SELECT|CREATE TABLE|INSERT INTO)", solution, re.MULTILINE):
        return "sql"

    return "text"
````

## → Calls
- [[Config.search]]

## ← Called by
- [[Runner.__init__]]
- [[registry.setup_search]]
