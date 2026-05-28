---
name: AdaEvolveContextBuilder.build_prompt
description: method in skydiscover/context_builder/adaevolve/builder.py (context-builder)
metadata:
  type: project
---

# AdaEvolveContextBuilder.build_prompt

**File:** `skydiscover/context_builder/adaevolve/builder.py:114`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def build_prompt(
        self,
        current_program: Union[Program, Dict[str, Program]],
        context: Dict[str, Any] = None,
        **kwargs: Any,
    ) -> Dict[str, str]:
        """
        Build prompt with AdaEvolve-specific search guidance.

        Computes the ``search_guidance`` string from AdaEvolve context keys,
        then delegates to the parent's ``build_prompt`` which fills the
        ``{search_guidance}`` placeholder in AdaEvolve templates.
        """
        context = context or {}

        # Build the search guidance from AdaEvolve-specific context
        search_guidance = self._build_search_guidance(current_program, context)

        # Override any caller-supplied search_guidance with our computed one
        kwargs.pop("search_guidance", None)

        # Pass search_guidance through **kwargs to template.format()
        result = super().build_prompt(
            current_program,
            context,
            search_guidance=search_guidance,
            task_objective=self._task_objective_text(),
            diversity_dimensions=self._diversity_dimensions_text(),
            diversity_note=self._diversity_note_text(),
            **kwargs,
        )

        return result
````

## → Calls
- [[AdaEvolveContextBuilder._build_search_guidance]]
- [[AdaEvolveContextBuilder._diversity_dimensions_text]]
- [[AdaEvolveContextBuilder._diversity_note_text]]
- [[AdaEvolveContextBuilder._task_objective_text]]
- [[DefaultContextBuilder.build_prompt]]
- [[base_database.Program]]

## ← Called by
- [[AdaEvolveController._generate_child]]
