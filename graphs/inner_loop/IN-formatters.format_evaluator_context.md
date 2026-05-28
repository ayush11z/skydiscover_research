---
name: IN-formatters.format_evaluator_context
description: function in skydiscover/context_builder/evox/formatters.py (context-builder)
metadata:
  type: project
---

# formatters.format_evaluator_context

**File:** `skydiscover/context_builder/evox/formatters.py:469`  
**Kind:** function  
**Layer:** #context-builder

## Source
````python
def format_evaluator_context(evaluator_path: Any) -> str:
    """Format the evaluator context by reading the evaluator file."""
    if evaluator_path is None:
        return "(No evaluator context provided)"

    if isinstance(evaluator_path, str):
        if not evaluator_path.endswith(".py"):
            if evaluator_path.strip().startswith("```"):
                return evaluator_path
            return f"```python\n{evaluator_path}\n```"
        try:
            if os.path.isfile(evaluator_path):
                with open(evaluator_path, "r") as f:
                    return f"```python\n{f.read()}\n```"
        except Exception as e:
            logger.warning(f"Failed to read evaluator file {evaluator_path}: {e}")

    return f"Evaluator file: {evaluator_path}"
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IN-EvoxContextBuilder.build_prompt]]
- [[IN-build_prompt.gather_llm_calls]]
