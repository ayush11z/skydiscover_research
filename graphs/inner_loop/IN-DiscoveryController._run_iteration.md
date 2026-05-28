---
name: IN-DiscoveryController._run_iteration
description: method in skydiscover/search/default_discovery_controller.py (inner-loop)
metadata:
  type: project
---

# DiscoveryController._run_iteration

**File:** `skydiscover/search/default_discovery_controller.py:455`  
**Kind:** method  
**Layer:** #inner-loop

## What it does
One complete generate-evaluate cycle:
1. ProgramDatabase.sample — pick a parent and context programs
2. DiscoveryController._build_prompt — build system + user messages
3. DiscoveryController._call_llm → LLMPool.generate — call the inner LLM
4. DiscoveryController._parse_llm_response — extract child code (diff or full rewrite)
5. `evaluate_program` — run the evaluator subprocess
6. ProgramDatabase.add — store the child if valid

Sets `loop_type = "inner"` via `set_llm_context` so LangFuseTracer.log_generation tags the trace correctly.

## Source
````python
    async def _run_iteration(
        self,
        iteration: int,
        retry_times: int = 1,
    ) -> SerializableResult:
        """Run a single generate-evaluate iteration."""
        _ctx_token = set_llm_context("inner", iteration)
        try:
            if not self.database.programs:
                return await self._run_from_scratch_iteration(iteration)

            raw_parent, raw_context_programs = self.database.sample(
                num_context_programs=self.num_context_programs
            )

            # Normalize sample() result — databases may return plain or dict-wrapped
            if isinstance(raw_parent, dict):
                if len(raw_parent) != 1:
                    raise ValueError(
                        f"sample() must return exactly one parent, got {len(raw_parent)}"
                    )
                parent_info_key = list(raw_parent.keys())[0]
                parent = list(raw_parent.values())[0]
            else:
                parent_info_key = ""
                parent = raw_parent

            # Other context programs that are relevant
            if isinstance(raw_context_programs, dict):
                context_programs_dict = raw_context_programs
            else:
                context_programs_dict = {"": raw_context_programs}

            parent_info = (parent_info_key, parent.id)
            context_info = [
                (key, p.id) for key, programs in context_programs_dict.items() for p in programs
            ]
            context_program_ids = [
                p.id for programs in context_programs_dict.values() for p in programs
            ]

            logger.debug(
                f"Iteration {iteration}: parent {parent.id} ({parent_info_key}), "
                f"other_context_programs keys: {list(context_programs_dict.keys())}"
            )

            iteration_start = time.time()

            failed_attempts = []
            child_solution, child_id, child_metrics, llm_response, changes_summary = (
                None,
                None,
                None,
                None,
                None,
            )

            image_path = None  # set by image mode or evaluator
            eval_time = 0.0

            # Build prompt with parent and context programs
            for retry in range(retry_times):
                prompt = self._build_prompt(
                    current_program=raw_parent,
                    context_programs=context_programs_dict,
                    failed_attempts=failed_attempts,
                )

                if failed_attempts:
                    logger.info(
                        f"Retry {retry + 1}/{retry_times}: rebuilding prompt with {len(failed_attempts)} failed attempt(s)"
                    )

                # Apply human feedback (append or replace mode)
                if self.feedback_reader:
                    self.feedback_reader.set_current_prompt(prompt["system"])
                    feedback = self.feedback_reader.read()
                    if feedback:
                        prompt = self.feedback_reader.apply_feedback(prompt)
                        self.feedback_reader.log_usage(
                            iteration, feedback, self.feedback_reader.mode
                        )

                try:
                    llm_generation_time = 0.0
                    llm_start = time.time()
                    if self.config.language == "image":
                        child_id = str(uuid.uuid4())
                        user_content = build_image_content(
                            prompt["user"], parent, context_programs_dict
                        )
                        self._save_solution_prompt(prompt["system"], user_content, iteration)
                        result = await self._call_llm(
                            prompt["system"],
                            user_content,
                            image_output=True,
                            output_dir=self._get_image_output_dir(),
                            program_id=child_id,
                        )
                        llm_response = result.text or ""
                        image_path = result.image_path
                        if image_path:
                            child_solution = result.text or "(image generated)"
                            changes_summary = "Image generation"
                            parse_error = None
                        else:
                            child_solution = None
                            changes_summary = None
                            parse_error = "VLM did not generate an image"
                    else:
                        self._save_solution_prompt(prompt["system"], prompt["user"], iteration)
                        result = await self._call_llm(prompt["system"], prompt["user"])
                        llm_response = result.text
                    llm_generation_time = time.time() - llm_start
                except Exception as e:
                    logger.error(f"LLM generation failed: {e}")
                    return SerializableResult(
                        error=f"LLM generation failed: {str(e)}",
                        iteration=iteration,
                        attempts_used=retry + 1,
                    )

                if self.config.language != "image":
                    # Text/code mode: parse LLM response
                    if llm_response is None:
                        return SerializableResult(
                            error="LLM returned None response",
                            iteration=iteration,
                            attempts_used=retry + 1,
                        )

                    child_solution, changes_summary, parse_error = self._parse_llm_response(
                        llm_response, parent.solution, iteration, retry + 1, retry_times
                    )

                    if child_solution and len(child_solution) > self.config.max_solution_length:
                        logger.warning(
                            "Generated solution exceeds maximum length (iteration=%s, attempt %s/%s): %s > %s",
                            iteration,
                            retry + 1,
                            retry_times,
                            len(child_solution),
                            self.config.max_solution_length,
                        )
                        parse_error = f"Generated solution exceeds maximum length ({len(child_solution)} > {self.config.max_solution_length})"
                        child_solution = None

                if parse_error:
                    failed_attempts.append(
                        {
                            "solution": child_solution or "",
                            "llm_response": llm_response,
                            "metrics": {},
                            "metadata": {
                                "error": parse_error,
                                "attempt_number": retry + 1,
                            },
                        }
                    )
                    if retry < retry_times - 1:
                        continue
                    logger.error(
                        "All %s retry attempts failed due to parse/validation error: %s",
                        retry_times,
                        parse_error,
                    )
                    return SerializableResult(
                        error=f"{parse_error} (after {retry_times} attempts)",
                        iteration=iteration,
                        prompt=prompt,
                        llm_response=llm_response,
                        attempts_used=retry_times,
                    )

                if self.config.language != "image":
                    child_id = str(uuid.uuid4())

                eval_input = image_path if self.config.language == "image" else child_solution
                eval_start = time.time()
                child_eval_result = await self.evaluator.evaluate_program(eval_input, child_id)
                eval_time = time.time() - eval_start
                child_metrics = child_eval_result.metrics
                # Extract image_path from evaluator metrics (non-image mode fallback)
                if not image_path:
                    image_path = (
                        child_metrics.pop("image_path", None)
                        if isinstance(child_metrics.get("image_path"), str)
                        else None
                    )

                if (
                    child_metrics.get("validity") in (0, -1)
                    or (
                        child_metrics.get("timeout") is True
                        and child_metrics.get("validity") is None
                    )
                    or (
                        child_metrics.get("combined_score") == 0
                        and child_metrics.get("error") is not None
                    )
                ):
                    error_msg = (
                        (
                            child_metrics.get("error")
                            if isinstance(child_metrics.get("error"), str)
                            else None
                        )
                        or child_metrics.get("error_message")
                        or "Evaluation failed (validity=0)"
                    )

                    logger.warning(
                        "Evaluation failed (attempt %s/%s): validity=%s, error=%s",
                        retry + 1,
                        retry_times,
                        child_metrics.get("validity"),
                        error_msg,
                    )
                    logger.debug(
                        "Failed solution (attempt %s/%s):\n%s",
                        retry + 1,
                        retry_times,
                        child_solution,
                    )

                    failed_attempts.append(
                        {
                            "solution": child_solution,
                            "metrics": child_metrics,
                            "metadata": {
                                "changes": changes_summary,
                                "parent_metrics": parent.metrics,
                                "error": error_msg,
                                "attempt_number": retry + 1,
                            },
                        }
                    )

                    if retry < retry_times - 1:
                        continue
                    logger.error(
                        "All %s retry attempts failed. Final error: %s", retry_times, error_msg
                    )
                    iteration_time = time.time() - iteration_start
                    failed_extra = {"failed_attempts": failed_attempts}
                    if image_path:
                        failed_extra["image_path"] = image_path
                    failed_child_program = self._create_child_program(
                        child_id=child_id,
                        child_solution=child_solution,
                        parent=parent,
                        context_program_ids=context_program_ids,
                        parent_info=parent_info,
                        context_info=context_info,
                        child_metrics=child_metrics or {},
                        iteration=iteration,
                        changes_summary=changes_summary,
                        extra_metadata=failed_extra,
                        artifacts=child_eval_result.artifacts,
                    )
                    return SerializableResult(
                        error=f"Evaluator failed after {retry_times} attempts: {error_msg}",
                        iteration=iteration,
                        child_program_dict=failed_child_program.to_dict(),
                        parent_id=parent.id,
                        other_context_ids=context_program_ids,
                        iteration_time=iteration_time,
                        llm_generation_time=llm_generation_time,
                        eval_time=eval_time,
                        prompt=prompt,
                        llm_response=llm_response,
                        attempts_used=retry_times,
                    )
                break

            extra_meta = {}
            if image_path:
                extra_meta["image_path"] = image_path
            child_program = self._create_child_program(
                child_id=child_id,
                child_solution=child_solution,
                parent=parent,
                context_program_ids=context_program_ids,
                parent_info=parent_info,
                context_info=context_info,
                child_metrics=child_metrics,
                iteration=iteration,
                changes_summary=changes_summary,
                extra_metadata=extra_meta if extra_meta else None,
                artifacts=child_eval_result.artifacts,
            )
            iteration_time = time.time() - iteration_start

            return SerializableResult(
                child_program_dict=child_program.to_dict(),
                parent_id=parent.id,
                other_context_ids=context_program_ids,
                iteration_time=iteration_time,
                llm_generation_time=llm_generation_time,
                eval_time=eval_time,
                prompt=prompt,
                llm_response=llm_response,
                iteration=iteration,
                attempts_used=retry + 1,
            )
        except Exception as e:
            logger.exception(f"Error in iteration {iteration}")
            return SerializableResult(error=str(e), iteration=iteration, attempts_used=1)
        finally:
            reset_llm_context(_ctx_token)
````

## → Calls
- [[IN-DiscoveryController.__init__]]
- [[IN-DiscoveryController._build_prompt]]
- [[IN-DiscoveryController._call_llm]]
- [[IN-DiscoveryController._create_child_program]]
- [[IN-DiscoveryController._get_image_output_dir]]
- [[IN-DiscoveryController._parse_llm_response]]
- [[IN-DiscoveryController._run_from_scratch_iteration]]
- [[IN-DiscoveryController._save_solution_prompt]]
- [[IN-DiscoveryControllerInput.config]]
- [[IN-EvaluationResult.metrics]]
- [[IN-EvaluationResult.to_dict]]
- [[IN-Evaluator.evaluate_program]]
- [[IN-LangFuseTracer.get]]
- [[IN-Program.id]]
- [[IN-Program.language]]
- [[IN-Program.metrics]]
- [[IN-Program.solution]]
- [[IN-Program.to_dict]]
- [[IN-ProgramDatabase.get]]
- [[IN-ProgramDatabase.sample]]
- [[IN-langfuse_tracer.reset_llm_context]]
- [[IN-langfuse_tracer.set_llm_context]]

## ← Called by
- [[IN-DiscoveryController._run_discovery_sequential]]
- [[IN-_run_discovery_parallel._bounded_iteration]]
