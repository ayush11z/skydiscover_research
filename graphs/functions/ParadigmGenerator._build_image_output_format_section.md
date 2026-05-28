---
name: ParadigmGenerator._build_image_output_format_section
description: method in skydiscover/search/adaevolve/paradigm/generator.py (adaevolve)
metadata:
  type: project
---

# ParadigmGenerator._build_image_output_format_section

**File:** `skydiscover/search/adaevolve/paradigm/generator.py:587`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _build_image_output_format_section(self) -> str:
        """Build image-specific output format section."""
        return f"""## Output Format

Generate {self.num_paradigms} breakthrough prompt strategies of DIFFERENT types.

Each strategy must be a JSON object with these fields:
- "idea": Clear description of the prompt engineering strategy
- "description": Detailed guide on how to restructure/rewrite the prompt (5-10 sentences)
- "what_to_optimize": Which rubric categories/visual elements to focus on
- "cautions": What to watch out for (e.g., don't lose existing good elements)
- "approach_type": Strategy category in "prompt.strategy_name" format

**Diversity Requirement:** Each strategy must use a FUNDAMENTALLY DIFFERENT approach.
Do not generate variations of the same technique.

Return ONLY a JSON array with {self.num_paradigms} strategy objects. No other text.

Example:
```json
[
  {{
    "idea": "Use explicit spatial anchoring with grid-based layout",
    "description": "Divide the scene into a 3x3 grid and assign each required element to a specific grid cell. Describe the contents of each cell in order (top-left to bottom-right). This helps the image model place objects precisely. For example: top-left contains 3 shaped clouds, top-center contains the banner, top-right contains 3 more clouds...",
    "what_to_optimize": "cloud_shapes, floating_island, spatial arrangement",
    "cautions": "Grid descriptions can feel rigid - add natural transitions between cells to maintain visual coherence",
    "approach_type": "prompt.spatial_grid"
  }}
]
```"""
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[ParadigmGenerator._build_output_format_section]]
