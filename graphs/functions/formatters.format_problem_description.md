---
name: formatters.format_problem_description
description: function in skydiscover/context_builder/evox/formatters.py (context-builder)
metadata:
  type: project
---

# formatters.format_problem_description

**File:** `skydiscover/context_builder/evox/formatters.py:458`  
**Kind:** function  
**Layer:** #context-builder

## Source
````python
def format_problem_description(problem_config: Any) -> str:
    """Format the problem description from the prompt config."""
    if problem_config is None:
        return "(No problem description provided)"
    if isinstance(problem_config, str):
        return problem_config
    if hasattr(problem_config, "system_message") and problem_config.system_message:
        return str(problem_config.system_message)
    return str(problem_config) if problem_config else "(No problem description provided)"
````

## → Calls
- [[ContextBuilderConfig.system_message]]
- [[LLMModelConfig.system_message]]

## ← Called by
- [[EvoxContextBuilder.build_prompt]]
- [[build_prompt.gather_llm_calls]]
