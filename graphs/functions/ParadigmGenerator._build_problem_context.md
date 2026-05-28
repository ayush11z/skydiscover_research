---
name: ParadigmGenerator._build_problem_context
description: method in skydiscover/search/adaevolve/paradigm/generator.py (adaevolve)
metadata:
  type: project
---

# ParadigmGenerator._build_problem_context

**File:** `skydiscover/search/adaevolve/paradigm/generator.py:264`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _build_problem_context(self, program_solution: str, best_score: float) -> str:
        """Build the problem context section."""
        if self._is_image_mode:
            return f"""## Problem Objective

{self.system_message}

## Optimization Targets

{self._optimization_targets_text()}

## Evaluator Code (shows how images are scored)

```python
{self.evaluator_code if self.evaluator_code else "N/A - evaluator code not provided"}
```

## Current Best Image Prompt ({self._score_label()}: {best_score:.6f})

{program_solution if program_solution else "N/A"}

**CRITICAL:** Analyze the current prompt first. What visual elements does it describe?
What details are present vs missing? Which rubric categories does it address well vs poorly?
How can the prompt be restructured to produce a better image?"""

        return f"""## Problem Objective

{self.system_message}

## Optimization Targets

{self._optimization_targets_text()}

## Evaluator Code (shows how solutions are scored)

```python
{self.evaluator_code if self.evaluator_code else "N/A - evaluator code not provided"}
```

## Current Best Program ({self._score_label()}: {best_score:.6f})

```python
{program_solution if program_solution else "N/A"}
```

**CRITICAL:** Analyze the current program first. What algorithm does it use?
What are its strengths and weaknesses? How can you improve upon it?"""
````

## → Calls
- [[ParadigmGenerator._optimization_targets_text]]
- [[ParadigmGenerator._score_label]]

## ← Called by
- [[ParadigmGenerator._build_prompt]]
