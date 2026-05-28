---
name: IO-code_utils.apply_diff
description: function in skydiscover/utils/code_utils.py (utils)
metadata:
  type: project
---

# code_utils.apply_diff

**File:** `skydiscover/utils/code_utils.py:11`  
**Kind:** function  
**Layer:** #utils

## Source
````python
def apply_diff(original_solution: str, diff_text: str) -> str:
    """
    Apply a diff to the original code

    Args:
        original_solution: Original source solution
        diff_text: Diff in the SEARCH/REPLACE format

    Returns:
        Modified solution
    """
    # Split into lines for easier processing
    original_lines = original_solution.split("\n")
    result_lines = original_lines.copy()

    # Extract diff blocks
    diff_blocks = extract_diffs(diff_text)

    # Apply each diff block
    for search_text, replace_text in diff_blocks:
        search_lines = search_text.split("\n")
        replace_lines = replace_text.split("\n")

        # Find where the search pattern starts in the original solution
        for i in range(len(result_lines) - len(search_lines) + 1):
            if result_lines[i : i + len(search_lines)] == search_lines:
                # Replace the matched section
                result_lines[i : i + len(search_lines)] = replace_lines
                break

    return "\n".join(result_lines)
````

## → Calls
- [[IO-code_utils.extract_diffs]]

## ← Called by
- [[IO-DiscoveryController._parse_llm_response]]
