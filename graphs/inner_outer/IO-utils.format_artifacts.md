---
name: IO-utils.format_artifacts
description: function in skydiscover/context_builder/utils.py (context-builder)
metadata:
  type: project
---

# utils.format_artifacts

**File:** `skydiscover/context_builder/utils.py:47`  
**Kind:** function  
**Layer:** #context-builder

## Source
````python
def format_artifacts(program: Any, heading: str = "##", max_len: int = 2000) -> str:
    """Format evaluator artifacts (e.g. feedback) into markdown sections."""
    artifacts = prog_attr(program, "artifacts", None)
    if not artifacts:
        return ""
    sections = []
    for key, value in artifacts.items():
        if value is None:
            continue
        text = str(value)
        if len(text) > max_len:
            text = text[:max_len] + "\n... (truncated)"
        if key == "feedback":
            sections.append(f"{heading} Evaluator Feedback\n{text}")
        else:
            sections.append(f"{heading} {key}\n{text}")
    if not sections:
        return ""
    return "\n" + "\n\n".join(sections) + "\n"
````

## → Calls
- [[IO-utils.prog_attr]]

## ← Called by
- [[IO-formatters.format_current_program]]
- [[IO-formatters.format_single_program_section]]
