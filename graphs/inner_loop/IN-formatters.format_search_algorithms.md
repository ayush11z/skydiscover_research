---
name: IN-formatters.format_search_algorithms
description: function in skydiscover/context_builder/evox/formatters.py (context-builder)
metadata:
  type: project
---

# formatters.format_search_algorithms

**File:** `skydiscover/context_builder/evox/formatters.py:571`  
**Kind:** function  
**Layer:** #context-builder

## Source
````python
def format_search_algorithms(
    other_context_programs: Union[List[Program], Dict[str, List[Program]]],
    language: str,
    summaries_by_num: Optional[Dict[int, str]] = None,
) -> str:
    """Format previous search algorithms with window context."""
    if not other_context_programs:
        return ""

    summaries_by_num = summaries_by_num or {}
    lines = []

    if isinstance(other_context_programs, dict):
        global_idx = 0
        for label, programs in other_context_programs.items():
            display_label = label or "Other Reference Programs"
            lines.extend(
                [f"\n## {display_label}\n", "Diverse search programs that may inspire new ideas:\n"]
            )
            for program in programs or []:
                global_idx += 1
                lines.extend(
                    format_single_program_section(program, global_idx, language, summaries_by_num)
                )
    else:
        lines.append("## Other Reference Programs\n")
        for idx, program in enumerate(other_context_programs, start=1):
            lines.extend(format_single_program_section(program, idx, language, summaries_by_num))

    return "\n".join(lines)
````

## → Calls
- [[IN-base_database.Program]]
- [[IN-formatters.format_single_program_section]]

## ← Called by
- [[IN-EvoxContextBuilder.build_prompt]]
