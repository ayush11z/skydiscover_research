---
name: variation_operator_generator._extract_examples
description: function in skydiscover/search/evox/utils/variation_operator_generator.py (evox)
metadata:
  type: project
---

# variation_operator_generator._extract_examples

**File:** `skydiscover/search/evox/utils/variation_operator_generator.py:390`  
**Kind:** function  
**Layer:** #evox

## Source
````python
def _extract_examples(response: str, is_diverge: bool = True) -> str:
    """Extract the examples section from LLM response."""
    lines = response.strip().split("\n")
    examples_lines = []
    in_examples = False

    for line in lines:
        if is_diverge and "EXAMPLES OF DIFFERENT" in line.upper():
            in_examples = True
            examples_lines.append(line)
        elif not is_diverge and "EXAMPLES OF REFINEMENT" in line.upper():
            in_examples = True
            examples_lines.append(line)
        elif in_examples:
            if line.strip().startswith("Format:") or line.strip().startswith("Your solution"):
                break
            if line.strip() in ("```", "```\n"):
                continue
            examples_lines.append(line)

    if examples_lines:
        while examples_lines and not examples_lines[-1].strip():
            examples_lines.pop()
        return "\n".join(examples_lines)

    return response.strip()
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[variation_operator_generator._parse_combined_response]]
