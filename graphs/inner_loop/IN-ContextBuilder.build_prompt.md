---
name: IN-ContextBuilder.build_prompt
description: method in skydiscover/context_builder/base.py (context-builder)
metadata:
  type: project
---

# ContextBuilder.build_prompt

**File:** `skydiscover/context_builder/base.py:22`  
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
        """Build a prompt for the LLM.

        Args:
            current_program: Program or {info: Program} to evolve from.
                When a dict, the key is additional context about the program.
            context: optional dict with keys such as program_metrics,
                other_context_programs, etc.

        Returns:
            Dict with "system" and "user" keys containing prompt strings.
        """
        pass
````

## → Calls
- [[IN-base_database.Program]]

## ← Called by
_(entry point — nothing in this graph calls it)_
