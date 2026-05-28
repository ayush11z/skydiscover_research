---
name: ParadigmGenerator._score_label
description: method in skydiscover/search/adaevolve/paradigm/generator.py (adaevolve)
metadata:
  type: project
---

# ParadigmGenerator._score_label

**File:** `skydiscover/search/adaevolve/paradigm/generator.py:85`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _score_label(self) -> str:
        """Label for the numeric score shown in prompts."""
        return "proxy score" if self._is_multiobjective() else "score"
````

## → Calls
- [[ParadigmGenerator._is_multiobjective]]

## ← Called by
- [[ParadigmGenerator._build_analysis_framework]]
- [[ParadigmGenerator._build_current_program_analysis]]
- [[ParadigmGenerator._build_problem_context]]
- [[ParadigmGenerator._build_prompt_opt_analysis]]
- [[ParadigmGenerator._build_prompt_opt_analysis_framework]]
- [[ParadigmGenerator._build_prompt_opt_context]]
