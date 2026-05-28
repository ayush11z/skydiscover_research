---
name: IO-DiscoveryController._build_prompt
description: method in skydiscover/search/default_discovery_controller.py (inner-loop)
metadata:
  type: project
---

# DiscoveryController._build_prompt

**File:** `skydiscover/search/default_discovery_controller.py:770`  
**Kind:** method  
**Layer:** #inner-loop

## What it does
Assembles the `{"system": ..., "user": ...}` dict that gets sent to the LLM. Passes the parent program, context programs (for few-shot examples), database stats, and any failed previous attempts to the `ContextBuilder`.

## Source
````python
    def _build_prompt(
        self,
        current_program: Union[Program, Dict[str, Program]],
        context_programs: Union[List[Program], Dict[str, List[Program]]],
        failed_attempts: list,
    ) -> Dict[str, str]:
        """Build the prompt for LLM generation."""
        parent = (
            list(current_program.values())[0]
            if isinstance(current_program, dict)
            else current_program
        )
        db_stats = self._prompt_context.get("db_stats") or self.database.get_statistics()

        # Build context with parent program and any other relevant information
        context = {
            "program_metrics": parent.metrics,
            "other_context_programs": context_programs,
            "previous_programs": db_stats.get("previous_programs", []),
            "db_stats": db_stats,
        }
        for k, v in self._prompt_context.items():
            if k not in context:
                context[k] = v

        if failed_attempts:
            context["errors"] = failed_attempts

        return self.context_builder.build_prompt(current_program=current_program, context=context)
````

## → Calls
- [[IO-DiscoveryController.__init__]]
- [[IO-EvoxContextBuilder.build_prompt]]
- [[IO-ProgramDatabase.get_statistics]]
- [[IO-base_database.Program]]

## ← Called by
- [[IO-DiscoveryController._run_iteration]]
