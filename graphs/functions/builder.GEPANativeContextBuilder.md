---
name: builder.GEPANativeContextBuilder
description: class in skydiscover/context_builder/gepa_native/builder.py (context-builder)
metadata:
  type: project
---

# builder.GEPANativeContextBuilder

**File:** `skydiscover/context_builder/gepa_native/builder.py:30`  
**Kind:** class  
**Layer:** #context-builder

## Source
````python
class GEPANativeContextBuilder(DefaultContextBuilder):
    """
    Context builder for GEPA Native's reflective evolutionary search.

    Adds a ``{search_guidance}`` section to the prompt containing:
    - Reflective analysis framing (tells the LLM to reason about failures)
    - Recent rejected programs (code that didn't improve on the parent)

    The controller passes raw data via the ``context`` dict:
    - ``context["rejection_history"]``: list of rejected Program objects
    - ``context["rejection_parent_scores"]``: dict mapping parent_id -> float score

    Metrics and evaluator diagnostics are already in {current_program}
    via the default template, so they are not repeated here.
    """

````

## → Calls
- [[builder.DefaultContextBuilder]]

## ← Called by
- [[GEPANativeController.__init__]]
