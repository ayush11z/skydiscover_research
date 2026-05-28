---
name: builder.AdaEvolveContextBuilder
description: class in skydiscover/context_builder/adaevolve/builder.py (context-builder)
metadata:
  type: project
---

# builder.AdaEvolveContextBuilder

**File:** `skydiscover/context_builder/adaevolve/builder.py:28`  
**Kind:** class  
**Layer:** #context-builder

## Source
````python
class AdaEvolveContextBuilder(DefaultContextBuilder):
    """
    Context builder for AdaEvolve's adaptive evolutionary search.

    Adds a ``{search_guidance}`` section to the prompt containing:
    - Evaluator diagnostic feedback (from parent's artifacts)
    - Paradigm breakthrough guidance (when search is globally stagnating)
    - Sibling context (previous mutations of the same parent)
    - Error retry context (when retrying after a failed generation)

    The controller passes raw data via the ``context`` dict:
    - ``context["paradigm"]``: paradigm dict or None
    - ``context["siblings"]``: list of Program objects
    - ``context["error_context"]``: error string or None

    Evaluator feedback is extracted from the parent program's artifacts.
    """

````

## → Calls
- [[builder.DefaultContextBuilder]]

## ← Called by
- [[AdaEvolveController.__init__]]
