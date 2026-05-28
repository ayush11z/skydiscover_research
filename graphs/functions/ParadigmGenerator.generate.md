---
name: ParadigmGenerator.generate
description: method in skydiscover/search/adaevolve/paradigm/generator.py (adaevolve)
metadata:
  type: project
---

# ParadigmGenerator.generate

**File:** `skydiscover/search/adaevolve/paradigm/generator.py:107`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    async def generate(
        self,
        current_program_solution: str,
        current_best_score: float,
        previously_tried_ideas: Optional[List[str]] = None,
        evaluator_feedback: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """
        Generate breakthrough paradigms with retry logic.

        Args:
            current_program_solution: Current best program solution
            current_best_score: Current best score
            previously_tried_ideas: List of previously tried approaches
            evaluator_feedback: Optional diagnostic feedback from evaluator artifacts

        Returns:
            List of paradigm dicts with keys:
            idea, description, what_to_optimize, cautions, approach_type
        """
        prompt = self._build_prompt(
            current_program_solution,
            current_best_score,
            previously_tried_ideas or [],
            evaluator_feedback=evaluator_feedback,
        )

        last_error = None
        backoff = INITIAL_BACKOFF_SECONDS

        for attempt in range(MAX_RETRIES):
            try:
                result = await self.llm_pool.generate(
                    system_message=self._get_system_message(),
                    messages=[{"role": "user", "content": prompt}],
                )
                response = result.text

                if not response:
                    logger.warning(f"Empty response from LLM (attempt {attempt + 1}/{MAX_RETRIES})")
                    last_error = "Empty response"
                    # Don't retry for empty response - likely a parsing issue
                    break

                paradigms = self._parse_response(response)

                if not paradigms:
                    logger.warning(
                        f"Failed to parse paradigms (attempt {attempt + 1}/{MAX_RETRIES})"
                    )
                    last_error = "Parse failure"
                    # Don't retry parse failures - the prompt needs fixing
                    break

                logger.info(f"Generated {len(paradigms)} paradigms:")
                for i, p in enumerate(paradigms):
                    logger.info(
                        f"  [{i+1}] {p.get('idea', 'N/A')} (approach: {p.get('approach_type', 'N/A')})"
                    )
                return paradigms

            except Exception as e:
                last_error = str(e)
                logger.warning(
                    f"Paradigm generation failed (attempt {attempt + 1}/{MAX_RETRIES}): {e}"
                )

                if attempt < MAX_RETRIES - 1:
                    logger.info(f"Retrying in {backoff:.1f}s...")
                    await asyncio.sleep(backoff)
                    backoff *= BACKOFF_MULTIPLIER

        logger.error(f"Paradigm generation failed after {MAX_RETRIES} attempts: {last_error}")
        return []
````

## → Calls
- [[AgenticGenerator.generate]]
- [[LLMInterface.generate]]
- [[LLMPool.generate]]
- [[ParadigmGenerator.__init__]]
- [[ParadigmGenerator._build_prompt]]
- [[ParadigmGenerator._get_system_message]]
- [[ParadigmGenerator._parse_response]]
- [[SerializableResult.error]]

## ← Called by
- [[AdaEvolveController._generate_paradigms_if_needed]]
- [[LLMPool.generate]]
- [[LLMPool.generate_all]]
- [[variation_operator_generator.generate_variation_operators]]
