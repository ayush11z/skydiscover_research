---
name: search_strategy_evaluator._format_attribute_error
description: function in skydiscover/search/evox/database/search_strategy_evaluator.py (evox)
metadata:
  type: project
---

# search_strategy_evaluator._format_attribute_error

**File:** `skydiscover/search/evox/database/search_strategy_evaluator.py:74`  
**Kind:** function  
**Layer:** #evox

## Source
````python
def _format_attribute_error(e: AttributeError, context: str) -> str:
    """Format an AttributeError with actionable details about the likely cause."""
    attr_name = getattr(e, 'name', None)
    if attr_name:
        return (
            f"AttributeError in {context}: attribute '{attr_name}' does not exist. "
            f"Likely cause: accessing program.{attr_name} directly instead of "
            f"program.metrics.get('{attr_name}', 0.0), or using self.best_score/"
            f"self.best_program which do not exist on EvolvedProgramDatabase. "
            f"Full error: {e}"
        )
    return f"AttributeError in {context}: {e}"
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[search_strategy_evaluator.evaluate]]
