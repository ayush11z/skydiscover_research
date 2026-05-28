---
name: GEPANativeController._attempt_merge
description: method in skydiscover/search/gepa_native/controller.py (gepa)
metadata:
  type: project
---

# GEPANativeController._attempt_merge

**File:** `skydiscover/search/gepa_native/controller.py:282`  
**Kind:** method  
**Layer:** #gepa

## Source
````python
    async def _attempt_merge(self, iteration: int) -> None:
        """Attempt an LLM-mediated merge of two complementary programs.

        Guards against budget exhaustion, self-merges, and duplicate pairs.
        On success the merged program is added to the database and stagnation
        is reset.  On failure (LLM error, parse error, eval error, or
        rejected merge) the stagnation counter is left unchanged.
        """
        if self._merge_attempts_used >= self.max_merge_attempts:
            return

        if len(self.database.programs) < 2:
            logger.debug("Not enough programs for merge, skipping")
            return

        prog_a, prog_b = self.database.get_merge_candidates()

        # Skip self-merge (happens when pool has < 2 distinct programs)
        if prog_a.id == prog_b.id:
            logger.debug(f"Iteration {iteration}: Only one program available, skipping merge")
            return

        # Deduplication: skip if this pair was already tried
        pair_key = tuple(sorted([prog_a.id, prog_b.id]))
        if pair_key in self._merge_pairs_tried:
            logger.debug(f"Iteration {iteration}: Merge pair already tried, skipping")
            return
        self._merge_pairs_tried.add(pair_key)
        self._merge_attempts_used += 1

        score_a = get_score(prog_a.metrics)
        score_b = get_score(prog_b.metrics)

        logger.info(
            f"Iteration {iteration}: Attempting merge "
            f"(stagnation={self._iterations_without_improvement}, "
            f"attempt={self._merge_attempts_used}/{self.max_merge_attempts}, "
            f"scores: {score_a:.4f}, {score_b:.4f})"
        )

        merge_prompt = self._build_merge_prompt(prog_a, prog_b)

        try:
            llm_start = time.time()
            llm_result = await self.llms.generate(
                system_message=merge_prompt["system"],
                messages=[{"role": "user", "content": merge_prompt["user"]}],
            )
            llm_generation_time = time.time() - llm_start
        except Exception as e:
            logger.warning(f"Merge LLM call failed: {e}")
            return

        llm_response = llm_result.text if llm_result else ""
        if not llm_response:
            logger.warning("Merge LLM returned empty response")
            return

        # Always parse as full rewrite (merge prompt asks for complete program)
        child_solution = parse_full_rewrite(llm_response, self.config.language)
        if not child_solution:
            logger.warning("Merge parse failed: no valid solution in response")
            return

        # Evaluate the merged solution
        child_id = str(uuid.uuid4())
        try:
            eval_start = time.time()
            eval_result = await self.evaluator.evaluate_program(child_solution, child_id)
            eval_time = time.time() - eval_start
        except Exception as e:
            logger.warning(f"Merge evaluation failed: {e}")
            return

        merged_score = get_score(eval_result.metrics)
        logger.info(
            f"Iteration {iteration}: Merge completed"
            f" (llm: {llm_generation_time:.2f}s,"
            f" eval: {eval_time:.2f}s)"
        )

        # GEPA acceptance criterion for merges: must meet or exceed both parents
        if merged_score >= max(score_a, score_b):
            merged_program = Program(
                id=child_id,
                solution=child_solution,
                language=self.config.language,
                metrics=eval_result.metrics,
                iteration_found=iteration,
                parent_id=prog_a.id,
                other_context_ids=[prog_b.id],
                parent_info=("Merge Parent A", prog_a.id),
                context_info=[("Merge Parent B", prog_b.id)],
                metadata={
                    "changes": "LLM-mediated merge",
                    "merge_score_a": score_a,
                    "merge_score_b": score_b,
                    "parent_metrics": prog_a.metrics,
                },
                artifacts=eval_result.artifacts or {},
            )
            self.database.add(merged_program, iteration=iteration)

            self.database.log_prompt(
                template_key="merge",
                program_id=child_id,
                prompt=merge_prompt,
                responses=[llm_response],  # already str via .text extraction above
            )

            logger.info(
                f"Merge ACCEPTED: score={merged_score:.4f} "
                f"(>= max({score_a:.4f}, {score_b:.4f}))"
            )

            if merged_score > self._best_score_seen:
                self._best_score_seen = merged_score

            # Reset stagnation only on successful merge
            self._iterations_without_improvement = 0

            # Fire monitor callback
            if self.monitor_callback:
                try:
                    self.monitor_callback(merged_program, iteration)
                except Exception as e:
                    logger.warning(
                        f"Monitor callback failed: {e}"
                    )  # Never crash discovery due to monitor
        else:
            logger.info(
                f"Merge REJECTED: score={merged_score:.4f} " f"< max({score_a:.4f}, {score_b:.4f})"
            )
````

## → Calls
- [[AgenticGenerator.__init__]]
- [[CheckpointManager.__init__]]
- [[CodeDiversity.__init__]]
- [[Config.evaluator]]
- [[ContainerizedEvaluator.__init__]]
- [[ContextBuilder.__init__]]
- [[DiscoveryController.__init__]]
- [[DiscoveryControllerInput.config]]
- [[DiscoveryControllerInput.database]]
- [[EvaluationResult.metrics]]
- [[Evaluator.__init__]]
- [[GEPANativeController._build_merge_prompt]]
- [[HumanFeedbackReader.__init__]]
- [[HybridDiversity.__init__]]
- [[LLMJudge.__init__]]
- [[LLMPool.__init__]]
- [[LangFuseTracer.__init__]]
- [[LogWindowScorer.__init__]]
- [[MetricDiversity.__init__]]
- [[MonitorServer.__init__]]
- [[OpenAILLM.__init__]]
- [[ParadigmGenerator.__init__]]
- [[Program.id]]
- [[Program.metrics]]
- [[ProgramDatabase.__init__]]
- [[Runner.__init__]]
- [[SearchConfig.database]]
- [[TaskPool.__init__]]
- [[TemplateManager.__init__]]
- [[UnifiedArchive.__init__]]
- [[_FinalResult.__init__]]
- [[base_database.Program]]
- [[code_utils.parse_full_rewrite]]
- [[default_discovery_controller.DiscoveryController]]
- [[evaluation.create_evaluator]]
- [[llm_pool.LLMPool]]
- [[metrics.get_score]]

## ← Called by
- [[GEPANativeController.run_discovery]]
