---
name: api.discover_solution
description: function in skydiscover/api.py (api)
metadata:
  type: project
---

# api.discover_solution

**File:** `skydiscover/api.py:277`  
**Kind:** function  
**Layer:** #api

## Source
````python
def discover_solution(
    evaluator: Callable[[str], Dict[str, Any]],
    initial_solution: Optional[str] = None,
    iterations: int = 100,
    search: Optional[str] = None,
    model: Optional[str] = None,
    **kwargs: Any,
) -> DiscoveryResult:
    """Convenience wrapper: evolve a string solution with a callable evaluator.

    Same as run_discovery but defaults to string input + callable evaluator.
    """
    return run_discovery(
        evaluator=evaluator,
        initial_program=initial_solution,
        iterations=iterations,
        search=search,
        model=model,
        **kwargs,
    )
````

## → Calls
- [[api.DiscoveryResult]]
- [[api.run_discovery]]

## ← Called by
_(entry point — nothing in this graph calls it)_
