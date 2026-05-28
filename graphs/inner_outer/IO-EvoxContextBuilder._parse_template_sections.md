---
name: IO-EvoxContextBuilder._parse_template_sections
description: staticmethod in skydiscover/context_builder/evox/builder.py (context-builder)
metadata:
  type: project
---

# EvoxContextBuilder._parse_template_sections

**File:** `skydiscover/context_builder/evox/builder.py:75`  
**Kind:** staticmethod  
**Layer:** #context-builder

## Source
````python
    def _parse_template_sections(text: str) -> Dict[str, str]:
        """Parse a template with ===SECTION=== markers into a dict of section_name -> content."""
        sections: Dict[str, str] = {}
        current_section = None
        current_lines: List[str] = []
        for line in text.splitlines():
            stripped = line.strip()
            if stripped.startswith("===") and stripped.endswith("===") and len(stripped) > 6:
                if current_section is not None:
                    sections[current_section] = "\n".join(current_lines).strip()
                current_section = stripped[3:-3]
                current_lines = []
            else:
                current_lines.append(line)
        if current_section is not None:
            sections[current_section] = "\n".join(current_lines).strip()
        return sections
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-EvoxContextBuilder.__init__]]
- [[IO-EvoxContextBuilder._generate_batch_summaries_async]]
- [[IO-EvoxContextBuilder.build_prompt]]
