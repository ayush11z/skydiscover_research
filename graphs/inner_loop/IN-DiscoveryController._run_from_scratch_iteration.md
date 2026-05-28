---
name: IN-DiscoveryController._run_from_scratch_iteration
description: method in skydiscover/search/default_discovery_controller.py (inner-loop)
metadata:
  type: project
---

# DiscoveryController._run_from_scratch_iteration

**File:** `skydiscover/search/default_discovery_controller.py:393`  
**Kind:** method  
**Layer:** #inner-loop

## Source
````python
    async def _run_from_scratch_iteration(self, iteration: int) -> SerializableResult:
        """Generate a first solution from scratch when the database is empty."""
        try:
            iteration_start = time.time()

            prompt = self.context_builder.build_prompt(current_program=None, context={})

            if self.feedback_reader:
                self.feedback_reader.set_current_prompt(prompt["system"])
                feedback = self.feedback_reader.read()
                if feedback:
                    prompt = self.feedback_reader.apply_feedback(prompt)

            llm_generation_time = 0.0
            llm_start = time.time()
            self._save_solution_prompt(prompt["system"], prompt["user"], iteration)
            result = await self._call_llm(prompt["system"], prompt["user"])
            llm_generation_time = time.time() - llm_start
            llm_response = result.text
            if not llm_response:
                return SerializableResult(error="Empty LLM response", iteration=iteration)

            child_solution = parse_full_rewrite(llm_response, self.config.language)
            if not child_solution:
                return SerializableResult(
                    error="No valid solution in response",
                    iteration=iteration,
                    prompt=prompt,
                    llm_response=llm_response,
                )

            child_id = str(uuid.uuid4())
            eval_start = time.time()
            eval_result = await self.evaluator.evaluate_program(child_solution, child_id)
            eval_time = time.time() - eval_start

            child = Program(
                id=child_id,
                solution=child_solution,
                language=self.config.language,
                parent_id=None,
                metrics=eval_result.metrics,
                iteration_found=iteration,
                metadata={"changes": "Generated from scratch"},
                artifacts=eval_result.artifacts or {},
            )

            return SerializableResult(
                child_program_dict=child.to_dict(),
                parent_id=None,
                other_context_ids=[],
                iteration_time=time.time() - iteration_start,
                llm_generation_time=llm_generation_time,
                eval_time=eval_time,
                prompt=prompt,
                llm_response=llm_response,
                iteration=iteration,
            )
        except Exception as e:
            logger.exception(f"From-scratch generation failed: {e}")
            return SerializableResult(error=str(e), iteration=iteration)
````

## → Calls
- [[IN-DiscoveryController.__init__]]
- [[IN-DiscoveryController._call_llm]]
- [[IN-DiscoveryController._save_solution_prompt]]
- [[IN-Evaluator.__init__]]
- [[IN-Evaluator.evaluate_program]]
- [[IN-EvoxContextBuilder.__init__]]
- [[IN-EvoxContextBuilder.build_prompt]]
- [[IN-LLMPool.__init__]]
- [[IN-LangFuseTracer.__init__]]
- [[IN-Program.language]]
- [[IN-Program.to_dict]]
- [[IN-ProgramDatabase.__init__]]
- [[IN-base_database.Program]]
- [[IN-code_utils.parse_full_rewrite]]

## ← Called by
- [[IN-DiscoveryController._run_iteration]]
