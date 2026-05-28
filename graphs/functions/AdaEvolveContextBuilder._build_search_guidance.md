---
name: AdaEvolveContextBuilder._build_search_guidance
description: method in skydiscover/context_builder/adaevolve/builder.py (context-builder)
metadata:
  type: project
---

# AdaEvolveContextBuilder._build_search_guidance

**File:** `skydiscover/context_builder/adaevolve/builder.py:183`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def _build_search_guidance(
        self,
        current_program: Union[Program, Dict[str, Program]],
        context: Dict[str, Any],
    ) -> str:
        """
        Assemble all AdaEvolve-specific guidance sections into one string.

        Sections are included in priority order:
        1. Evaluator feedback (highest value — shows why parent fails)
        2. Paradigm breakthrough guidance (when globally stagnating)
        3. Sibling context (previous mutations of this parent)
        4. Error retry context (when retrying after failure)
        """
        # Extract parent program from current_program dict
        if isinstance(current_program, dict):
            parent_program = list(current_program.values())[0]
        else:
            parent_program = current_program

        language = self.config.language or "python"
        paradigm = context.get("paradigm")
        siblings = context.get("siblings", [])
        error_context = context.get("error_context")

        sections: List[str] = []

        # 1. Evaluator feedback from parent artifacts
        feedback_section = self._format_evaluator_feedback(parent_program)
        if feedback_section:
            sections.append(feedback_section)

        # 2. Paradigm breakthrough guidance
        if paradigm:
            sections.append(self._format_paradigm_guidance(paradigm, language))

        # 3. Sibling context
        if siblings:
            sibling_section = self._format_sibling_context(siblings, parent_program)
            if sibling_section:
                sections.append(sibling_section)

        # 4. Error retry context
        if error_context:
            sections.append(self._format_error_context(error_context))

        if not sections:
            return ""

        return "\n\n".join(sections)
````

## → Calls
- [[AdaEvolveContextBuilder._format_error_context]]
- [[AdaEvolveContextBuilder._format_evaluator_feedback]]
- [[AdaEvolveContextBuilder._format_paradigm_guidance]]
- [[AdaEvolveContextBuilder._format_sibling_context]]
- [[DiscoveryControllerInput.config]]
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]
- [[base_database.Program]]

## ← Called by
- [[AdaEvolveContextBuilder.build_prompt]]
