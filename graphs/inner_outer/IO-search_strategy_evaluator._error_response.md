---
name: IO-search_strategy_evaluator._error_response
description: function in skydiscover/search/evox/database/search_strategy_evaluator.py (evox)
metadata:
  type: project
---

# search_strategy_evaluator._error_response

**File:** `skydiscover/search/evox/database/search_strategy_evaluator.py:12`  
**Kind:** function  
**Layer:** #evox

## Source
````python
def _error_response(error_message: str) -> Dict[str, Any]:
    """Create a standardized error response dictionary."""
    return {"validity": 0, "error": error_message, "combined_score": None}
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-evaluate_batch.eval_with_timeout]]
- [[IO-search_strategy_evaluator.evaluate]]
- [[IO-search_strategy_evaluator.evaluate_batch]]
