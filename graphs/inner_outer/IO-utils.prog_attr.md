---
name: IO-utils.prog_attr
description: function in skydiscover/context_builder/utils.py (context-builder)
metadata:
  type: project
---

# utils.prog_attr

**File:** `skydiscover/context_builder/utils.py:38`  
**Kind:** function  
**Layer:** #context-builder

## Source
````python
def prog_attr(program: Any, key: str, default: Any = "") -> Any:
    """Read an attribute from a Program object or a plain dict."""
    if hasattr(program, key):
        return getattr(program, key)
    if isinstance(program, dict):
        return program.get(key, default)
    return default
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-EvoxContextBuilder.build_prompt]]
- [[IO-formatters.format_current_program]]
- [[IO-formatters.format_single_program_section]]
- [[IO-formatters.identify_search_improvement_areas]]
- [[IO-formatters.prepare_search_algorithms_data]]
- [[IO-utils.format_artifacts]]
