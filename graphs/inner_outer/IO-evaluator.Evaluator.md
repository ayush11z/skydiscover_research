---
name: IO-evaluator.Evaluator
description: class in skydiscover/evaluation/evaluator.py (evaluation)
metadata:
  type: project
---

# evaluator.Evaluator

**File:** `skydiscover/evaluation/evaluator.py:25`  
**Kind:** class  
**Layer:** #evaluation

## Source
````python
class Evaluator:
    """
    Runs the user-provided evaluation function on candidate programs.

    Writes the candidate to a temp file, calls evaluate(program_path), and
    returns an EvaluationResult. Supports optional cascade (multi-stage)
    evaluation and LLM-as-a-judge feedback.
    """

````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
_(entry point — nothing in this graph calls it)_
