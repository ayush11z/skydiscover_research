---
name: AdaEvolveContextBuilder._format_current_program
description: method in skydiscover/context_builder/adaevolve/builder.py (context-builder)
metadata:
  type: project
---

# AdaEvolveContextBuilder._format_current_program

**File:** `skydiscover/context_builder/adaevolve/builder.py:152`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def _format_current_program(
        self,
        current_program: Union[Program, Dict[str, Program]],
        language: str,
    ) -> str:
        """Override to suppress artifacts["feedback"] from {current_program}.

        AdaEvolve renders evaluator feedback explicitly via _build_search_guidance
        into {search_guidance}, so we strip it here to avoid duplication.
        """
        # Remove feedback from artifacts so parent renderer skips it (rendered via search_guidance instead)
        if isinstance(current_program, dict):
            program = list(current_program.values())[0]
        else:
            program = current_program

        artifacts = getattr(program, "artifacts", None)
        saved_feedback = None
        if isinstance(artifacts, dict) and "feedback" in artifacts:
            saved_feedback = artifacts.pop("feedback")

        try:
            return super()._format_current_program(current_program, language)
        finally:
            if saved_feedback is not None and isinstance(artifacts, dict):
                artifacts["feedback"] = saved_feedback
````

## → Calls
- [[DefaultContextBuilder._format_current_program]]
- [[base_database.Program]]

## ← Called by
_(entry point — nothing in this graph calls it)_
