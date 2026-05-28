---
name: GEPANativeContextBuilder.build_prompt
description: method in skydiscover/context_builder/gepa_native/builder.py (context-builder)
metadata:
  type: project
---

# GEPANativeContextBuilder.build_prompt

**File:** `skydiscover/context_builder/gepa_native/builder.py:54`  
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
        Build prompt with GEPA reflective search guidance.

        Computes the ``search_guidance`` string from GEPA context keys,
        then delegates to the parent's ``build_prompt`` which fills the
        ``{search_guidance}`` placeholder in the template.
        """
        context = context or {}

        search_guidance = self._build_search_guidance(current_program, context)

        kwargs.pop("search_guidance", None)

        result = super().build_prompt(
            current_program,
            context,
            search_guidance=search_guidance,
            **kwargs,
        )

        # Collapse 3+ consecutive newlines to 2 (empty search_guidance leaves extra blank lines)
        if "user" in result:
            result["user"] = re.sub(r"\n{3,}", "\n\n", result["user"])

        return result
````

## → Calls
- [[DefaultContextBuilder.build_prompt]]
- [[GEPANativeContextBuilder._build_search_guidance]]
- [[base_database.Program]]

## ← Called by
- [[GEPANativeController._build_prompt]]
