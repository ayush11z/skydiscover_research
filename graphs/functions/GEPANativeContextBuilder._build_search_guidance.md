---
name: GEPANativeContextBuilder._build_search_guidance
description: method in skydiscover/context_builder/gepa_native/builder.py (context-builder)
metadata:
  type: project
---

# GEPANativeContextBuilder._build_search_guidance

**File:** `skydiscover/context_builder/gepa_native/builder.py:90`  
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
        Assemble GEPA-specific reflective guidance into one string.

        Sections:
        1. Reflective analysis framing (always present when there's content)
        2. Rejection history (recently rejected programs)
        """
        rejection_history = context.get("rejection_history", [])
        rejection_parent_scores = context.get("rejection_parent_scores", {})

        sections: List[str] = []

        # Rejection history
        if rejection_history:
            rejection_section = self._format_rejection_history(
                rejection_history, rejection_parent_scores
            )
            if rejection_section:
                sections.append(rejection_section)

        if not sections:
            return ""

        # Prepend reflective framing header
        header = (
            "## Reflective Analysis\n"
            "Review the evaluation results and diagnostics in the program "
            "information above. Identify root causes and domain-specific "
            "insights. Address these failure modes in your solution."
        )

        return header + "\n\n" + "\n\n".join(sections)
````

## → Calls
- [[GEPANativeContextBuilder._format_rejection_history]]
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]
- [[base_database.Program]]

## ← Called by
- [[GEPANativeContextBuilder.build_prompt]]
