---
name: generator.ParadigmGenerator
description: class in skydiscover/search/adaevolve/paradigm/generator.py (adaevolve)
metadata:
  type: project
---

# generator.ParadigmGenerator

**File:** `skydiscover/search/adaevolve/paradigm/generator.py:24`  
**Kind:** class  
**Layer:** #adaevolve

## Source
````python
class ParadigmGenerator:
    """
    Generates breakthrough paradigms using LLM analysis.

    Uses a structured 6-step analysis framework:
    1. Understand the task
    2. Analyze the evaluator code
    3. Identify metrics
    4. Identify constraints
    5. Identify problem structure
    6. Identify improvement opportunities

    Output format per paradigm:
    {
        "idea": "Short description of the breakthrough idea",
        "description": "Detailed implementation guide",
        "what_to_optimize": "Target metric from evaluator",
        "cautions": "Important implementation details",
        "approach_type": "library.function format"
    }
    """

````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[AdaEvolveController.__init__]]
