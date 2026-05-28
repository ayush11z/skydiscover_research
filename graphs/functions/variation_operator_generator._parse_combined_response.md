---
name: variation_operator_generator._parse_combined_response
description: function in skydiscover/search/evox/utils/variation_operator_generator.py (evox)
metadata:
  type: project
---

# variation_operator_generator._parse_combined_response

**File:** `skydiscover/search/evox/utils/variation_operator_generator.py:355`  
**Kind:** function  
**Layer:** #evox

## Source
````python
def _parse_combined_response(response: str) -> Tuple[str, str]:
    """Parse the combined LLM response to extract structural variation (explore broadly) and local refinement (exploit within current approach) sections."""
    exploration = ""
    exploitation = ""

    lines = response.split("\n")
    current_section = None
    current_lines = []

    for line in lines:
        line_upper = line.upper().strip()
        if "### EXPLORATION" in line_upper or "EXPLORATION (DIVERGE" in line_upper:
            if current_section == "exploitation":
                exploitation = "\n".join(current_lines)
            current_section = "exploration"
            current_lines = []
        elif "### EXPLOITATION" in line_upper or "EXPLOITATION (REFINE" in line_upper:
            if current_section == "exploration":
                exploration = "\n".join(current_lines)
            current_section = "exploitation"
            current_lines = []
        elif current_section:
            current_lines.append(line)

    if current_section == "exploration":
        exploration = "\n".join(current_lines)
    elif current_section == "exploitation":
        exploitation = "\n".join(current_lines)

    exploration = _extract_examples(exploration, is_diverge=True)
    exploitation = _extract_examples(exploitation, is_diverge=False)

    return exploration, exploitation
````

## → Calls
- [[variation_operator_generator._extract_examples]]

## ← Called by
- [[variation_operator_generator._operators_from_response]]
