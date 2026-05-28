---
name: IO-variation_operator_generator.load_initial_program
description: function in skydiscover/search/evox/utils/variation_operator_generator.py (evox)
metadata:
  type: project
---

# variation_operator_generator.load_initial_program

**File:** `skydiscover/search/evox/utils/variation_operator_generator.py:255`  
**Kind:** function  
**Layer:** #evox

## Source
````python
def load_initial_program(initial_program_path: str) -> str:
    """Load and return the initial_program.py contents."""
    with open(initial_program_path, "r") as f:
        return f.read()
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-variation_operator_generator.main]]
