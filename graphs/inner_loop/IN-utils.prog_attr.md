---
name: IN-utils.prog_attr
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
- [[IN-EvoxContextBuilder.build_prompt]]
- [[IN-formatters.format_current_program]]
- [[IN-formatters.format_single_program_section]]
- [[IN-formatters.identify_search_improvement_areas]]
- [[IN-formatters.prepare_search_algorithms_data]]
- [[IN-utils.format_artifacts]]
