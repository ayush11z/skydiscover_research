---
name: IO-CoEvolutionController._generate_and_validate_search_algorithm
description: method in skydiscover/search/evox/controller.py (outer-loop)
metadata:
  type: project
---

# CoEvolutionController._generate_and_validate_search_algorithm

**File:** `skydiscover/search/evox/controller.py:347`  
**Kind:** method  
**Layer:** #outer-loop

## What it does
Asks the outer LLM (qwen2.5-coder:14b) to write a new `EvolvedProgramDatabase` subclass in Python, then validates it by attempting to instantiate it. If valid, calls CoEvolutionController._switch_to_new_search_algorithm.

The LLM receives population statistics (scores, diversity, stagnation window) so it can reason about what sampling strategy to use next.

Sets `loop_type = "outer"` via LangFuseTracer.log_generation through the context var.

## Source
````python
    async def _generate_and_validate_search_algorithm(self, solution_iter: int) -> None:
        """Generate a new search algorithm and switch to it if valid."""
        iteration = self._num_search_evolutions
        search_stats = self._build_search_stats(solution_iter)

        self.search_controller._prompt_context = {
            "search_stats": search_stats["search_algorithm_stats"],
            "db_stats": search_stats["db_stats"],
        }
        _ctx_token = set_llm_context("outer", solution_iter)
        try:
            result = await self.search_controller.run_discovery(
                start_iteration=iteration,
                max_iterations=1,
                post_process_result=False,
            )
        finally:
            reset_llm_context(_ctx_token)

        if not result or result.error:
            await handle_generation_failure(
                self.search_outputs_dir,
                self._active_search_algorithm_code,
                iteration,
                result,
                solution_iter,
            )
            self._num_search_evolutions += 1
            return

        result.child_program_dict.setdefault("metadata", {})["start_db_stats"] = (
            make_json_serializable(search_stats["db_stats"])
        )
        await log_search_algorithm_generated(
            self.search_outputs_dir,
            result,
            iteration,
            diverge_label=self._diverge_label,
            refine_label=self._refine_label,
        )

        if not self._switch_to_new_search_algorithm(result):
            await handle_generation_failure(
                self.search_outputs_dir,
                self._active_search_algorithm_code,
                iteration,
                result,
                solution_iter,
                "validation",
            )
            self._num_search_evolutions += 1
            return

        self._pending_search_result = result
        self._reset_search_window(start_iteration=solution_iter)
````

## → Calls
- [[IO-CoEvolutionController._build_search_stats]]
- [[IO-CoEvolutionController._reset_search_window]]
- [[IO-CoEvolutionController._switch_to_new_search_algorithm]]
- [[IO-DiscoveryController.run_discovery]]
- [[IO-coevolve_logging.handle_generation_failure]]
- [[IO-coevolve_logging.log_search_algorithm_generated]]
- [[IO-coevolve_logging.make_json_serializable]]
- [[IO-default_discovery_controller.DiscoveryController]]
- [[IO-langfuse_tracer.reset_llm_context]]
- [[IO-langfuse_tracer.set_llm_context]]

## ← Called by
- [[IO-CoEvolutionController._evolve_search]]
- [[IO-CoEvolutionController._initialize_first_search_program]]
