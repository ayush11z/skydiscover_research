---
name: utils.prog_attr
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
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]

## ← Called by
- [[AdaEvolveContextBuilder._format_previous_attempts]]
- [[AdaEvolveContextBuilder._identify_improvement_areas]]
- [[DefaultContextBuilder._format_current_program]]
- [[DefaultContextBuilder._format_previous_attempts]]
- [[DefaultContextBuilder._format_single_context_program]]
- [[DefaultContextBuilder._identify_improvement_areas]]
- [[DefaultContextBuilder.build_prompt]]
- [[EvoxContextBuilder.build_prompt]]
- [[formatters.format_current_program]]
- [[formatters.format_single_program_section]]
- [[formatters.identify_search_improvement_areas]]
- [[formatters.prepare_search_algorithms_data]]
- [[utils.format_artifacts]]
