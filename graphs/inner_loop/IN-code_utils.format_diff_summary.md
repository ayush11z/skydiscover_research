---
name: IN-code_utils.format_diff_summary
description: function in skydiscover/utils/code_utils.py (utils)
metadata:
  type: project
---

# code_utils.format_diff_summary

**File:** `skydiscover/utils/code_utils.py:168`  
**Kind:** function  
**Layer:** #utils

## Source
````python
def format_diff_summary(diff_blocks: List[Tuple[str, str]]) -> str:
    """
    Create a human-readable summary of the diff.

    If docstrings are identical between old and new code, uses simpler format.
    If docstrings differ or function is renamed, shows the meaningful change.

    Args:
        diff_blocks: List of (search_text, replace_text) tuples

    Returns:
        Summary string
    """
    summary = []

    for i, (search_text, replace_text) in enumerate(diff_blocks):
        search_lines = search_text.strip().split("\n")
        replace_lines = replace_text.strip().split("\n")

        # Try to extract meaningful info from the solution
        old_info = _extract_def_info(search_text)
        new_info = _extract_def_info(replace_text)

        # Build a meaningful summary
        if old_info or new_info:
            info = new_info or old_info
            kind, name, docstring = info

            # Get docstrings from both to compare
            old_docstring = old_info[2] if old_info else None
            new_docstring = new_info[2] if new_info else None

            if old_info and new_info and old_info[1] != new_info[1]:
                # Renamed function/class - always show this
                desc = f"Renamed {old_info[0]} `{old_info[1]}` → `{new_info[1]}`"
            elif old_docstring and new_docstring and old_docstring != new_docstring:
                # Docstrings are DIFFERENT - show the new docstring
                desc = f"Modified {kind} `{name}`: {new_docstring}"
            elif old_docstring == new_docstring:
                # Docstrings are IDENTICAL - use simple format (just line counts)
                desc = f"Modified {kind} `{name}` ({len(search_lines)}→{len(replace_lines)} lines)"
            elif docstring:
                # Only one has docstring
                desc = f"Modified {kind} `{name}`: {docstring}"
            else:
                desc = f"Modified {kind} `{name}` ({len(search_lines)}→{len(replace_lines)} lines)"

            summary.append(f"Change {i+1}: {desc}")
        elif len(search_lines) == 1 and len(replace_lines) == 1:
            # Single line change - show the actual change
            summary.append(
                f"Change {i+1}: '{search_lines[0].strip()}' → '{replace_lines[0].strip()}'"
            )
        else:
            # Fallback: show first non-empty line as context
            first_old = next((l.strip() for l in search_lines if l.strip()), "")
            first_new = next((l.strip() for l in replace_lines if l.strip()), "")

            if first_old and first_new:
                summary.append(
                    f"Change {i+1}: Near `{first_old[:50]}...` ({len(search_lines)}→{len(replace_lines)} lines)"
                )
            else:
                summary.append(
                    f"Change {i+1}: Replace {len(search_lines)} lines with {len(replace_lines)} lines"
                )

    return "\n".join(summary)
````

## → Calls
- [[IN-code_utils._extract_def_info]]

## ← Called by
- [[IN-DiscoveryController._parse_llm_response]]
