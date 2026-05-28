---
name: ParadigmGenerator._build_prompt_opt_context
description: method in skydiscover/search/adaevolve/paradigm/generator.py (adaevolve)
metadata:
  type: project
---

# ParadigmGenerator._build_prompt_opt_context

**File:** `skydiscover/search/adaevolve/paradigm/generator.py:622`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _build_prompt_opt_context(self, prompt_text: str, best_score: float) -> str:
        """Build problem context for prompt optimization."""
        return f"""## Problem Objective

{self.system_message}

## Optimization Targets

{self._optimization_targets_text()}

## Evaluator Code (shows how prompts are scored)

```python
{self.evaluator_code if self.evaluator_code else "N/A - evaluator code not provided"}
```

## Current Best Prompt ({self._score_label()}: {best_score:.6f})

```text
{prompt_text if prompt_text else "N/A"}
```

**CRITICAL:** Analyze the current prompt first. What instruction strategy does it use?
What are its strengths and weaknesses? How can you improve upon it?"""
````

## → Calls
- [[ParadigmGenerator._optimization_targets_text]]
- [[ParadigmGenerator._score_label]]

## ← Called by
- [[ParadigmGenerator._build_prompt]]
