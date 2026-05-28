---
name: ParadigmGenerator._build_image_techniques_section
description: method in skydiscover/search/adaevolve/paradigm/generator.py (adaevolve)
metadata:
  type: project
---

# ParadigmGenerator._build_image_techniques_section

**File:** `skydiscover/search/adaevolve/paradigm/generator.py:509`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _build_image_techniques_section(self) -> str:
        """Build image-specific techniques guidance section."""
        return """## Prompt Engineering Techniques for Image Generation

**For Improving Object Counts & Specificity:**
- Explicit enumeration: number and describe each instance ("the first balloon is red with stripes, the second balloon is blue with dots, the third...")
- Spatial anchoring: place objects at specific locations ("in the top-left corner", "at the center")
- Grid/layout descriptions: describe the scene as zones or a grid
- Repetition emphasis: mention critical counts multiple times

**For Improving Spatial Arrangement:**
- Layered composition: describe background, midground, foreground separately
- Directional flow: describe the scene left-to-right or top-to-bottom
- Relative positioning: define objects in relation to each other ("to the right of X, below Y")
- Scene sectioning: divide the image into named regions and populate each

**For Improving Text/Labels in Images:**
- Prominent placement: make text elements the primary focus of a region
- Sign/banner framing: describe text on clear, high-contrast surfaces
- Simplify text: shorter text is more reliably rendered
- Style emphasis: "clearly legible text reading exactly..."

**For Improving Detail Accuracy:**
- Category isolation: dedicate a paragraph to each evaluation category
- Attribute chaining: attach all required attributes directly to each object
- Checklist-style: explicitly list each required detail as a bullet

**For Changing Overall Approach:**
- Art style shifts: try different mediums (digital painting, 3D render, illustration, watercolor)
- Perspective changes: bird's eye view, isometric, close-up vs wide shot
- Simplification: reduce scene complexity to improve accuracy on key elements
- Narrative framing: describe the scene as a story moment for better coherence

**ANTI-PATTERNS - What NOT to suggest:**
1. Do NOT suggest code/algorithmic approaches (scipy, numpy, ML training) - this is prompt engineering
2. Do NOT suggest using different image models - work with the current model
3. Do NOT suggest post-processing or image editing - only prompt changes
4. Do NOT suggest vague ideas like "make it better" - be specific about prompt structure changes

**General Principles:**
- Image models weight text at the beginning of prompts more heavily
- Fewer, more specific constraints are better than many vague ones
- Concrete visual descriptions beat abstract concepts
- Structural prompt changes (reordering, sectioning) often help more than adding words"""
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[ParadigmGenerator._build_techniques_section]]
