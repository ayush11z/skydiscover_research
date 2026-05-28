---
name: ParadigmGenerator._build_prompt_opt_techniques_section
description: method in skydiscover/search/adaevolve/paradigm/generator.py (adaevolve)
metadata:
  type: project
---

# ParadigmGenerator._build_prompt_opt_techniques_section

**File:** `skydiscover/search/adaevolve/paradigm/generator.py:693`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _build_prompt_opt_techniques_section(self) -> str:
        """Build techniques guidance for prompt optimization."""
        return """## Prompt Engineering Techniques

**Reasoning & Decomposition:**
- Chain-of-thought: "Think step by step before answering"
- Multi-hop decomposition: "First identify relevant facts, then reason across them"
- Self-verification: "Check your answer against the passages before responding"
- Contrastive reasoning: "Consider why other answers might be wrong"

**Instruction Structure:**
- Role assignment: Give the LLM a specific expert persona
- Task decomposition: Break complex tasks into sub-steps within the prompt
- Explicit constraints: "Answer ONLY based on provided passages"
- Output format specification: "Respond with just the answer, no explanation"

**Few-Shot & Examples:**
- Include 1-3 worked examples showing input->reasoning->output
- Show examples of common error patterns and correct handling
- Demonstrate edge cases (unanswerable, ambiguous)

**Retrieval-Augmented Strategies:**
- Passage prioritization: "Focus on passages most relevant to the question"
- Evidence extraction: "Quote the specific evidence before answering"
- Multi-passage synthesis: "Combine information from multiple passages"

**Error Prevention:**
- Hallucination guards: "Only use information from the given passages"
- Confidence calibration: "If unsure, state the most likely answer"
- Format enforcement: "Your answer must be a short phrase, not a sentence"

**General Principles:**
- Be specific over generic — vague prompts lead to vague answers
- Structure matters — numbered steps outperform wall-of-text instructions
- Constraints prevent errors — explicit "do not" rules reduce hallucination
- Less can be more — overly long prompts can confuse the LLM

## ANTI-PATTERNS for Prompt Optimization

1. **Do NOT just rephrase the same instruction** — changing words without changing strategy is not a breakthrough
2. **Do NOT add irrelevant constraints** — constraints should target observed failure modes
3. **Do NOT make the prompt excessively long** — diminishing returns after a certain length
4. **Do NOT add examples that don't match the task** — misleading examples hurt performance

## DIVERSITY REQUIREMENTS

Before generating ideas, explicitly think:
- Idea 1: [Strategy A - e.g., reasoning structure change]
- Idea 2: [Strategy B - e.g., output format / constraint change - DIFFERENT from A]
- Idea 3: [Strategy C - e.g., few-shot / example-based - DIFFERENT from A and B]

**Verify:** Are these DIFFERENT strategy types? NOT variations of the same approach.

Each idea must:
- Use a DIFFERENT prompt engineering technique
- Target DIFFERENT aspects of LLM behavior
- Be independently implementable as a complete prompt
- Be specific and actionable (not just "improve clarity")"""
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[ParadigmGenerator._build_prompt]]
