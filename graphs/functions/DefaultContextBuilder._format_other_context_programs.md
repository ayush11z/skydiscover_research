---
name: DefaultContextBuilder._format_other_context_programs
description: method in skydiscover/context_builder/default/builder.py (context-builder)
metadata:
  type: project
---

# DefaultContextBuilder._format_other_context_programs

**File:** `skydiscover/context_builder/default/builder.py:314`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def _format_other_context_programs(
        self,
        other_context_programs: Union[List[Program], Dict[str, List[Program]]],
        language: str,
    ) -> str:
        """Format all context programs, grouped by key when dict-wrapped."""
        if not other_context_programs:
            return ""

        lines = []
        if isinstance(other_context_programs, dict):
            for label, programs in other_context_programs.items():
                if not programs:
                    continue
                lines.append(f"\n## {label or 'Other Context Solutions'}\n")
                lines.append(
                    "These programs represent diverse approaches and creative solutions that may be relevant to the current task:\n\n"
                )
                for i, program in enumerate(programs, start=1):
                    self._format_single_context_program(program, i, language, lines)
        else:
            lines.append(
                "These programs represent diverse approaches and creative solutions that may inspire new ideas:\n"
            )
            for i, program in enumerate(other_context_programs, start=1):
                self._format_single_context_program(program, i, language, lines)

        return "".join(lines)
````

## → Calls
- [[DefaultContextBuilder._format_single_context_program]]
- [[base_database.Program]]

## ← Called by
- [[DefaultContextBuilder.build_prompt]]
