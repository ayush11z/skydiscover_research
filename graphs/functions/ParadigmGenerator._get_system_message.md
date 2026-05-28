---
name: ParadigmGenerator._get_system_message
description: method in skydiscover/search/adaevolve/paradigm/generator.py (adaevolve)
metadata:
  type: project
---

# ParadigmGenerator._get_system_message

**File:** `skydiscover/search/adaevolve/paradigm/generator.py:182`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _get_system_message(self) -> str:
        """Get system message for paradigm generation."""
        if self._is_image_mode:
            return (
                "You are an expert visual artist and image prompt engineer. "
                "Think carefully and deeply about visual composition, spatial layout, "
                "and how image generation models interpret text prompts. "
                "Analyze the evaluation rubric thoroughly and suggest breakthrough "
                "prompt strategies that will actually improve the generated images. "
                "Focus on strategies that are fundamentally different from what has been tried."
            )
        elif self._is_prompt_optimization:
            return (
                "You are an expert prompt engineer and LLM researcher. Think carefully "
                "and deeply. Analyze the current prompt, understand the evaluation "
                "pipeline by reading the evaluator code, and suggest breakthrough "
                "prompt strategies that are actionable and will improve accuracy. "
                "Focus on strategies that are fundamentally different from what has "
                "been tried."
            )
        return (
            "You are an expert algorithm researcher. Think carefully and deeply. "
            "Analyze the problem thoroughly, understand the evaluation metric "
            "by reading the evaluator code, and suggest breakthrough ideas that are "
            "correct, actionable, and will actually help improve the solution. "
            "Focus on ideas that are fundamentally different from what has been tried."
        )
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[EvoxContextBuilder.build_prompt]]
- [[ParadigmGenerator.generate]]
