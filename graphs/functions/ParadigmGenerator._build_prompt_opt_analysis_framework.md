---
name: ParadigmGenerator._build_prompt_opt_analysis_framework
description: method in skydiscover/search/adaevolve/paradigm/generator.py (adaevolve)
metadata:
  type: project
---

# ParadigmGenerator._build_prompt_opt_analysis_framework

**File:** `skydiscover/search/adaevolve/paradigm/generator.py:659`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _build_prompt_opt_analysis_framework(self, best_score: float) -> str:
        """Build analysis framework for prompt optimization."""
        return f"""## Analysis Framework - Complete Before Generating Ideas

**STEP 0: Understand the TASK (MOST IMPORTANT)**
- What task is the LLM being asked to perform?
- What inputs does the LLM receive? What output is expected?
- What makes this task hard? (reasoning steps, ambiguity, retrieval quality)

**STEP 1: Analyze the Evaluator Pipeline**
- How are prompts evaluated? (dataset, metric, scoring)
- What types of errors cause score loss? (wrong answer, wrong format, hallucination)
- How does retrieval interact with the prompt?

**STEP 2: Analyze Current Prompt Weaknesses**
- Is the instruction clear and unambiguous?
- Does it guide the LLM's reasoning process?
- Does it specify output format precisely?
- Does it handle edge cases (ambiguous questions, missing info)?

**STEP 3: Identify Improvement Dimensions**
- Instruction clarity and specificity
- Reasoning chain guidance (step-by-step, decomposition)
- Output format constraints
- Error prevention (hallucination guards, hedging strategies)
- Example inclusion (few-shot demonstrations)

**STEP 4: Design Breakthrough Strategies**
- What fundamentally different instruction approaches could work?
- What prompt engineering techniques haven't been tried?
- How can we better exploit the retrieval context?

Current best {self._score_label()} is {best_score:.6f}. Your ideas must improve the configured optimization targets and, in multiobjective mode, explicitly address evaluator trade-offs."""
````

## → Calls
- [[ParadigmGenerator._score_label]]

## ← Called by
- [[ParadigmGenerator._build_prompt]]
