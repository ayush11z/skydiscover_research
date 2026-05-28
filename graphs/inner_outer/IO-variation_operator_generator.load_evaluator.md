---
name: IO-variation_operator_generator.load_evaluator
description: function in skydiscover/search/evox/utils/variation_operator_generator.py (evox)
metadata:
  type: project
---

# variation_operator_generator.load_evaluator

**File:** `skydiscover/search/evox/utils/variation_operator_generator.py:249`  
**Kind:** function  
**Layer:** #evox

## Source
````python
def load_evaluator(evaluator_path: str) -> str:
    """Load and return the evaluator.py contents."""
    with open(evaluator_path, "r") as f:
        return f.read()
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-variation_operator_generator.main]]
