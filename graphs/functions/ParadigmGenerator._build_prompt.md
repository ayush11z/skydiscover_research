---
name: ParadigmGenerator._build_prompt
description: method in skydiscover/search/adaevolve/paradigm/generator.py (adaevolve)
metadata:
  type: project
---

# ParadigmGenerator._build_prompt

**File:** `skydiscover/search/adaevolve/paradigm/generator.py:210`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _build_prompt(
        self,
        program_solution: str,
        best_score: float,
        previously_tried: List[str],
        evaluator_feedback: Optional[str] = None,
    ) -> str:
        """Build the full prompt for paradigm generation."""
        if self._is_prompt_optimization:
            sections = [
                self._build_prompt_opt_context(program_solution, best_score),
                self._build_prompt_opt_analysis(best_score),
                self._build_prompt_opt_analysis_framework(best_score),
                self._build_previously_tried_section(previously_tried),
                self._build_prompt_opt_techniques_section(),
                self._build_prompt_opt_output_format_section(),
            ]
        else:
            sections = [
                self._build_problem_context(program_solution, best_score),
                self._build_current_program_analysis(best_score),
                self._build_analysis_framework(best_score),
                self._build_previously_tried_section(previously_tried),
                self._build_techniques_section(),
                self._build_output_format_section(),
            ]

        # Inject evaluator feedback so paradigm ideas are informed by
        # specific failure modes identified by the evaluator.
        if evaluator_feedback:
            max_len = 2000
            if len(evaluator_feedback) > max_len:
                evaluator_feedback = evaluator_feedback[:max_len] + "\n... (truncated)"
            sections.insert(
                -1,  # before the output format section
                f"## Evaluator Feedback on Current Best Program\n"
                f"The evaluator analyzed cases where the current program fails. "
                f"Use this to inform your breakthrough ideas:\n\n"
                f"{evaluator_feedback}",
            )

        return "\n\n".join(sections)
````

## → Calls
- [[ParadigmGenerator._build_analysis_framework]]
- [[ParadigmGenerator._build_current_program_analysis]]
- [[ParadigmGenerator._build_output_format_section]]
- [[ParadigmGenerator._build_previously_tried_section]]
- [[ParadigmGenerator._build_problem_context]]
- [[ParadigmGenerator._build_prompt_opt_analysis]]
- [[ParadigmGenerator._build_prompt_opt_analysis_framework]]
- [[ParadigmGenerator._build_prompt_opt_context]]
- [[ParadigmGenerator._build_prompt_opt_output_format_section]]
- [[ParadigmGenerator._build_prompt_opt_techniques_section]]
- [[ParadigmGenerator._build_techniques_section]]

## ← Called by
- [[ParadigmGenerator.generate]]
