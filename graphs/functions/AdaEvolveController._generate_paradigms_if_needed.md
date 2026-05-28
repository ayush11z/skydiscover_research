---
name: AdaEvolveController._generate_paradigms_if_needed
description: method in skydiscover/search/adaevolve/controller.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveController._generate_paradigms_if_needed

**File:** `skydiscover/search/adaevolve/controller.py:340`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    async def _generate_paradigms_if_needed(self) -> None:
        """Generate new paradigms if stagnating and none active."""
        if self.paradigm_generator is None:
            return

        if self.database.has_active_paradigm():
            return  # Already have paradigms to use

        logger.info("Global paradigm stagnation detected, generating breakthrough ideas...")

        # Get current best program for context
        best_program = self.database.get_best_program()
        best_solution = best_program.solution if best_program else ""
        best_score = self.database.get_program_proxy_score(best_program)

        # Extract evaluator feedback from the best program's artifacts
        evaluator_feedback = None
        if best_program and best_program.artifacts:
            fb = best_program.artifacts.get("feedback")
            if fb and isinstance(fb, str):
                evaluator_feedback = fb

        # Get previously tried ideas for feedback
        previously_tried = self.database.get_previously_tried_ideas()

        # Generate new paradigms
        paradigms = await self.paradigm_generator.generate(
            current_program_solution=best_solution,
            current_best_score=best_score,
            previously_tried_ideas=previously_tried,
            evaluator_feedback=evaluator_feedback,
        )

        if paradigms:
            self.database.set_paradigms(paradigms)
            logger.info(f"Generated {len(paradigms)} breakthrough paradigms")
        else:
            logger.warning("Failed to generate paradigms")
````

## → Calls
- [[AdaEvolveController.__init__]]
- [[AgenticGenerator.generate]]
- [[DiscoveryControllerInput.database]]
- [[EvaluationResult.artifacts]]
- [[LLMInterface.generate]]
- [[LLMPool.generate]]
- [[ParadigmGenerator.generate]]
- [[Program.artifacts]]
- [[Program.solution]]
- [[SearchConfig.database]]
- [[default_discovery_controller.DiscoveryController]]

## ← Called by
- [[AdaEvolveController._run_iteration]]
