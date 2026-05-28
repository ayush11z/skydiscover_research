---
name: ParadigmGenerator._build_prompt_opt_analysis
description: method in skydiscover/search/adaevolve/paradigm/generator.py (adaevolve)
metadata:
  type: project
---

# ParadigmGenerator._build_prompt_opt_analysis

**File:** `skydiscover/search/adaevolve/paradigm/generator.py:647`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _build_prompt_opt_analysis(self, best_score: float) -> str:
        """Build analysis directive for prompt optimization."""
        return f"""**CRITICAL: ANALYZE THE CURRENT PROMPT FIRST**
Before suggesting new strategies, carefully analyze the current prompt above:
- What instruction approach does it use? (This is what's WORKING - {self._score_label()} {best_score:.6f})
- What are its strengths? (Clarity? Structure? Examples? Reasoning guidance?)
- What are its weaknesses? (Vague? Missing constraints? No examples? Poor format spec?)
- What would make the LLM perform better on this task?

**IMPORTANT:** The prompt above is the CURRENT prompt that needs improvement.
Understand what works, then suggest fundamentally different prompt strategies."""
````

## → Calls
- [[ParadigmGenerator._score_label]]

## ← Called by
- [[ParadigmGenerator._build_prompt]]
