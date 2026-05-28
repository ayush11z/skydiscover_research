---
name: AdaEvolveContextBuilder._format_evaluator_feedback
description: staticmethod in skydiscover/context_builder/adaevolve/builder.py (context-builder)
metadata:
  type: project
---

# AdaEvolveContextBuilder._format_evaluator_feedback

**File:** `skydiscover/context_builder/adaevolve/builder.py:281`  
**Kind:** staticmethod  
**Layer:** #context-builder

## Source
````python
    def _format_evaluator_feedback(parent_program: Program) -> Optional[str]:
        """
        Format evaluator feedback from parent's artifacts.

        The evaluator may return diagnostic feedback (e.g. analysis of failed
        examples) in artifacts["feedback"]. This is injected into the prompt
        so the LLM can make targeted improvements instead of guessing.
        """
        artifacts = getattr(parent_program, "artifacts", None)
        if not artifacts:
            return None

        feedback = artifacts.get("feedback")
        if not feedback or not isinstance(feedback, str):
            return None

        # Truncate very long feedback to keep prompt focused
        max_len = 2000
        if len(feedback) > max_len:
            feedback = feedback[:max_len] + "\n... (truncated)"

        return (
            "## EVALUATOR FEEDBACK ON CURRENT PROGRAM\n"
            "The evaluator analyzed cases where the current program failed "
            "and produced the following diagnostic feedback. "
            "Use this to make targeted improvements:\n\n"
            f"{feedback}"
        )
````

## → Calls
- [[base_database.Program]]

## ← Called by
- [[AdaEvolveContextBuilder._build_search_guidance]]
