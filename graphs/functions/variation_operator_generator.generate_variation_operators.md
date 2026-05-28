---
name: variation_operator_generator.generate_variation_operators
description: function in skydiscover/search/evox/utils/variation_operator_generator.py (evox)
metadata:
  type: project
---

# variation_operator_generator.generate_variation_operators

**File:** `skydiscover/search/evox/utils/variation_operator_generator.py:479`  
**Kind:** function  
**Layer:** #evox

## Source
````python
async def generate_variation_operators(
    system_message: str,
    evaluator_code: str,
    problem_dir: Optional[str] = None,
    initial_program_solution: Optional[str] = None,
    llm_pool: Optional[LLMPool] = None,
) -> Tuple[str, str]:
    """Generate problem-specific variation operators (e.g. structural variation or local refinement).

    Args:
        system_message: Problem description (from config).
        evaluator_code: The evaluator.py source code.
        problem_dir: Optional path to problem directory (for requirements.txt).
        initial_program_solution: Optional initial program source code for additional context.
        llm_pool: LLMPool to use for generation.

    Returns:
        (structural_variation_label, local_refinement_label)
    """
    user_prompt = _build_operator_prompt(
        system_message,
        evaluator_code,
        problem_dir,
        initial_program_solution,
    )

    result = await llm_pool.generate(
        system_message=COMBINED_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_prompt}],
    )

    return _operators_from_response(result.text)
````

## → Calls
- [[AgenticGenerator.generate]]
- [[LLMInterface.generate]]
- [[LLMPool.generate]]
- [[ParadigmGenerator.generate]]
- [[llm_pool.LLMPool]]
- [[variation_operator_generator.COMBINED_SYSTEM_PROMPT]]
- [[variation_operator_generator._build_operator_prompt]]
- [[variation_operator_generator._operators_from_response]]

## ← Called by
- [[CoEvolutionController._generate_variation_operators]]
- [[variation_operator_generator.main]]
