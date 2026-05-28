---
name: ParadigmGenerator._build_prompt_opt_output_format_section
description: method in skydiscover/search/adaevolve/paradigm/generator.py (adaevolve)
metadata:
  type: project
---

# ParadigmGenerator._build_prompt_opt_output_format_section

**File:** `skydiscover/search/adaevolve/paradigm/generator.py:752`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _build_prompt_opt_output_format_section(self) -> str:
        """Build output format for prompt optimization paradigms."""
        return f"""## Output Format

Generate {self.num_paradigms} breakthrough prompt strategies of DIFFERENT types.

Each idea must be a JSON object with these fields:
- "idea": Clear description of the prompt strategy
- "description": Detailed guide on how to write the new prompt (5-10 sentences)
- "what_to_optimize": What aspect of LLM behavior this targets
- "cautions": What to watch out for when implementing this strategy
- "approach_type": Category of the technique (e.g., "chain-of-thought", "few-shot", "format-constraint")

**Diversity Requirement:** Each idea must use a DIFFERENT strategy type.
Do not generate variations of the same technique.

Return ONLY a JSON array with {self.num_paradigms} paradigm objects. No other text.

Example:
```json
[
  {{
    "idea": "Add step-by-step multi-hop reasoning instructions",
    "description": "Restructure the prompt to explicitly guide the LLM through multi-hop reasoning. First identify key entities in the question, then find relevant facts about each entity in the passages, then chain the facts together to arrive at the answer. Include explicit instructions like: Step 1: Identify what the question is asking. Step 2: Find passages mentioning the key entities. Step 3: Extract relevant facts. Step 4: Combine facts to answer.",
    "what_to_optimize": "multi-hop reasoning accuracy",
    "cautions": "Keep steps concise. Too many steps can confuse the model. Ensure the steps match the actual reasoning pattern needed.",
    "approach_type": "chain-of-thought"
  }}
]
```"""
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[ParadigmGenerator._build_prompt]]
