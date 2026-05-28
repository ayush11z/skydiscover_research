---
name: ParadigmGenerator._build_output_format_section
description: method in skydiscover/search/adaevolve/paradigm/generator.py (adaevolve)
metadata:
  type: project
---

# ParadigmGenerator._build_output_format_section

**File:** `skydiscover/search/adaevolve/paradigm/generator.py:554`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _build_output_format_section(self) -> str:
        """Build the output format section."""
        if self._is_image_mode:
            return self._build_image_output_format_section()
        return f"""## Output Format

Generate {self.num_paradigms} breakthrough ideas of DIFFERENT types.

Each idea must be a JSON object with these fields:
- "idea": Clear, direct description with library/technique name
- "description": Detailed implementation guide (5-10 sentences)
- "what_to_optimize": What metrics/areas to focus on
- "cautions": Important implementation details to watch for
- "approach_type": Exact "library.function" format (e.g., "scipy.optimize.minimize")

**Diversity Requirement:** Each idea must use a DIFFERENT approach type.
Do not generate variations of the same technique.

Return ONLY a JSON array with {self.num_paradigms} paradigm objects. No other text.

Example:
```json
[
  {{
    "idea": "Use scipy.optimize.minimize with SLSQP",
    "description": "Apply scipy.optimize.minimize directly to optimize all variables together...",
    "what_to_optimize": "{', '.join(self.objective_names) if self.objective_names else 'primary evaluator score'}",
    "cautions": "Ensure constraints are properly formulated, use multiple starting points",
    "approach_type": "scipy.optimize.minimize"
  }}
]
```"""
````

## → Calls
- [[ParadigmGenerator._build_image_output_format_section]]

## ← Called by
- [[ParadigmGenerator._build_prompt]]
