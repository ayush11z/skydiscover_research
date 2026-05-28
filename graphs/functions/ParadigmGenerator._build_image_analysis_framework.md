---
name: ParadigmGenerator._build_image_analysis_framework
description: method in skydiscover/search/adaevolve/paradigm/generator.py (adaevolve)
metadata:
  type: project
---

# ParadigmGenerator._build_image_analysis_framework

**File:** `skydiscover/search/adaevolve/paradigm/generator.py:360`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _build_image_analysis_framework(self, best_score: float) -> str:
        """Build image-specific analysis framework."""
        return f"""## Analysis Framework (Image Mode) - Complete Before Generating Ideas

**STEP 0: Understand the VISUAL TASK (MOST IMPORTANT)**
- What scene/image is being requested?
- What specific visual elements are required? (objects, counts, arrangements)
- What text/labels must appear in the image?
- What spatial relationships are specified?

**STEP 1: Analyze the Evaluation Rubric**
- How is the image scored? (read the evaluator code)
- What categories/dimensions are evaluated?
- What specific counts, colors, positions does the judge look for?
- What causes low scores in each category?

**STEP 2: Identify Weakest Categories**
- Which rubric categories score lowest in the current best?
- Which elements are consistently missing or wrong?
- Which details does the image model struggle with most?

**STEP 3: Understand Image Model Limitations**
- Image models struggle with: exact counts, legible text, precise spatial layouts
- Image models are good at: mood, color, style, general composition, prominent objects
- Which required elements hit model limitations?

**STEP 4: Analyze Current Prompt Structure**
- How is the prompt organized? (single block vs sections vs enumerated)
- Does it emphasize the right things? (models weight early text more heavily)
- Are critical details buried or prominent?
- Is the prompt too long or too short?

**STEP 5: Identify Prompt Engineering Strategies**
- What structural changes could help? (reordering, sectioning, emphasis)
- What description strategies could improve counts? (explicit enumeration, spatial anchoring)
- What style/medium changes might help with specific elements?

**STEP 6: Prioritize Improvements**
- Which categories have the most room for improvement?
- Which improvements are achievable given model limitations?
- What prompt changes would have the highest impact?

Current best score is {best_score:.6f}. Your strategies must be capable of improving this."""
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[ParadigmGenerator._build_analysis_framework]]
