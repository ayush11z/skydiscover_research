---
name: search_strategy_evaluator.evaluate_batch
description: function in skydiscover/search/evox/database/search_strategy_evaluator.py (evox)
metadata:
  type: project
---

# search_strategy_evaluator.evaluate_batch

**File:** `skydiscover/search/evox/database/search_strategy_evaluator.py:805`  
**Kind:** function  
**Layer:** #evox

## Source
````python
def evaluate_batch(
    program_paths: List[str],
    fast_mode: bool = True,
    max_workers: int = 4,
    timeout_per_file: float = 30.0,
) -> Dict[str, Dict[str, Any]]:
    """Evaluate multiple database implementations in parallel."""
    results = {}

    def eval_with_timeout(path: str) -> Tuple[str, Dict[str, Any]]:
        try:
            result = evaluate(path, fast_mode=fast_mode)
            return path, result
        except Exception as e:
            return path, _error_response(f"Evaluation failed: {str(e)}")

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_path = {executor.submit(eval_with_timeout, path): path for path in program_paths}

        for future in as_completed(future_to_path, timeout=timeout_per_file * len(program_paths)):
            try:
                path, result = future.result(timeout=timeout_per_file)
                results[path] = result
            except Exception as e:
                path = future_to_path[future]
                results[path] = _error_response(f"Evaluation timed out or failed: {str(e)}")

    return results
````

## → Calls
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]
- [[evaluate_batch.eval_with_timeout]]
- [[search_strategy_evaluator._error_response]]
- [[search_strategy_evaluator.result]]

## ← Called by
_(entry point — nothing in this graph calls it)_
