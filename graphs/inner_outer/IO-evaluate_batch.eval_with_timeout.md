---
name: IO-evaluate_batch.eval_with_timeout
description: function in skydiscover/search/evox/database/search_strategy_evaluator.py (evox)
metadata:
  type: project
---

# evaluate_batch.eval_with_timeout

**File:** `skydiscover/search/evox/database/search_strategy_evaluator.py:814`  
**Kind:** function  
**Layer:** #evox

## Source
````python
    def eval_with_timeout(path: str) -> Tuple[str, Dict[str, Any]]:
        try:
            result = evaluate(path, fast_mode=fast_mode)
            return path, result
        except Exception as e:
            return path, _error_response(f"Evaluation failed: {str(e)}")
````

## → Calls
- [[IO-search_strategy_evaluator._error_response]]
- [[IO-search_strategy_evaluator.evaluate]]

## ← Called by
- [[IO-search_strategy_evaluator.evaluate_batch]]
