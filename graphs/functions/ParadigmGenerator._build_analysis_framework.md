---
name: ParadigmGenerator._build_analysis_framework
description: method in skydiscover/search/adaevolve/paradigm/generator.py (adaevolve)
metadata:
  type: project
---

# ParadigmGenerator._build_analysis_framework

**File:** `skydiscover/search/adaevolve/paradigm/generator.py:312`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _build_analysis_framework(self, best_score: float) -> str:
        """Build the 6-step analysis framework section."""
        if self._is_image_mode:
            return self._build_image_analysis_framework(best_score)
        return f"""## Analysis Framework - Complete Before Generating Ideas

**STEP 0: Understand the TASK (MOST IMPORTANT - DO THIS FIRST)**
- What is the problem asking you to do?
- What is the goal or objective? (maximize, minimize, optimize)
- What are the inputs and outputs?
- What needs to be improved? (variables/decisions that affect the goal)
- What constraints exist?

**STEP 1: Analyze the Evaluator Code**
- How are solutions scored?
- What metrics are computed?
- What causes failures or penalties?

**STEP 2: Identify Metrics**
- What is the primary metric or Pareto objective set?
- How is it calculated?
- What secondary metrics exist?
- If variance/std is penalized, the program needs consistency across scenarios

**STEP 3: Identify Constraints**
- What conditions must be satisfied?
- What validation happens?
- What causes score penalties?

**STEP 4: Identify Problem Structure**
- Is processing sequential or global?
- Are decision variables discrete or continuous?
- What dependencies exist between decisions?
- **CRITICAL:** What data does your program receive vs what the evaluator uses?
- **CRITICAL:** How are metrics computed across components? Independently then aggregated, or jointly?

**STEP 5: Determine Appropriate Approach**
- Match approach to problem structure
- Consider what has worked vs failed before
- Identify promising library/technique combinations

**STEP 6: Identify Improvement Opportunities**
- What would increase each metric?
- What would satisfy constraints better?
- What fundamentally different approaches could work?

Current best {self._score_label()} is {best_score:.6f}. Your ideas must improve the configured optimization targets and, in multiobjective mode, explicitly reason about objective trade-offs."""
````

## → Calls
- [[ParadigmGenerator._build_image_analysis_framework]]
- [[ParadigmGenerator._score_label]]

## ← Called by
- [[ParadigmGenerator._build_prompt]]
