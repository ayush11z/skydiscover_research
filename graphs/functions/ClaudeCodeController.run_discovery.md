---
name: ClaudeCodeController.run_discovery
description: method in skydiscover/search/claude_code/controller.py (claude-code)
metadata:
  type: project
---

# ClaudeCodeController.run_discovery

**File:** `skydiscover/search/claude_code/controller.py:153`  
**Kind:** method  
**Layer:** #claude-code

## Source
````python
    async def run_discovery(
        self,
        start_iteration: int,
        max_iterations: int,
        checkpoint_callback: Optional[Callable] = None,
        **kwargs,
    ) -> Optional[Program]:
        db_config = self.database.config
        image_name = getattr(db_config, "docker_image", "skydiscover-claude-code:latest")
        max_turns = max_iterations

        model = self.config.llm.models[0].name if self.config.llm.models else None
        if model and not any(model.startswith(p) for p in _CLAUDE_MODEL_PREFIXES):
            raise ValueError(
                f"claude_code only supports Claude models, got: {model!r}. "
                f"Use a claude-* model name (e.g. claude-sonnet-4-6)."
            )

        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError(
                "ANTHROPIC_API_KEY environment variable is not set. "
                "Export it before running: export ANTHROPIC_API_KEY=sk-ant-..."
            )

        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, self._ensure_image_built, image_name)

        initial = self.database.get_best_program()
        initial_code = initial.solution if initial else ""

        tmp_base = os.path.expanduser("~/.tmp")
        os.makedirs(tmp_base, exist_ok=True)
        workspace = Path(tempfile.mkdtemp(dir=tmp_base))
        container_name = f"skydiscover-cc-{uuid.uuid4().hex[:12]}"

        try:
            suffix = self.file_suffix
            solution_path = workspace / f"solution{suffix}"
            solution_path.write_text(initial_code)

            eval_path = Path(self.evaluation_file)
            is_docker_eval = eval_path.is_dir()
            eval_timeout = self.config.evaluator.timeout

            if is_docker_eval:
                self._write_eval_script(workspace, "docker", timeout=eval_timeout)
                await loop.run_in_executor(
                    None, self._save_evaluator_image, workspace, self.evaluator.image_tag
                )
            else:
                shutil.copy(eval_path, workspace / "evaluator.py")
                self._write_eval_script(workspace, "python", timeout=eval_timeout)
                req = eval_path.parent / "requirements.txt"
                if req.exists():
                    shutil.copy(req, workspace / "requirements.txt")

            task_content = self._write_task_prompt(workspace, suffix, max_turns)

            # Prompt file -- avoids shell quoting issues with backticks in task.
            (workspace / ".prompt.txt").write_text(task_content)

            model_flag = f"--model {shlex.quote(model)} " if model else ""

            script_lines = ["#!/bin/bash"]
            if (workspace / "requirements.txt").exists():
                script_lines.append(
                    "pip install -q --no-warn-script-location"
                    " -r /workspace/requirements.txt >/dev/null 2>&1 || true"
                )
            script_lines.append(
                f"exec claude -p - "
                f"--max-turns {max_turns} "
                f"--dangerously-skip-permissions "
                f"--output-format stream-json "
                f"--verbose "
                f"{model_flag}"
                f"< /workspace/.prompt.txt"
            )
            run_script = workspace / ".run.sh"
            run_script.write_text("\n".join(script_lines) + "\n")
            run_script.chmod(0o755)

            cmd = self._build_docker_cmd(
                image_name, container_name, workspace, api_key, is_docker_eval
            )

            # Wall-clock safety net: full eval timeout + 2 min thinking per turn.
            wall_timeout = max(max_turns * (120 + eval_timeout), 600)

            out = Path(self.output_dir) if self.output_dir else None
            progress_log = (out / "progress.log") if out else None
            if out:
                out.mkdir(parents=True, exist_ok=True)

            log_path = workspace / "claude.log"
            _progress_lock = threading.Lock()

            def _write_progress(line: str) -> None:
                ts = time.strftime("%H:%M:%S")
                entry = f"[{ts}] {line}"
                logger.info(entry)
                if progress_log:
                    with _progress_lock:
                        with open(progress_log, "a") as f:
                            f.write(entry + "\n")

            _write_progress(
                f"Run started -- model={model or 'default'}, "
                f"max_turns={max_turns}, wall_timeout={wall_timeout}s"
            )

            # Shared state, modified only from the executor thread.
            cumulative_turns = 0
            total_cost_usd = 0.0
            stream_turns = 0
            run_start = time.monotonic()

            def _run_with_turn_limit() -> None:
                nonlocal cumulative_turns, total_cost_usd, stream_turns
                start = time.monotonic()
                hard_stop_at = 0.0

                with open(log_path, "w") as log_file:
                    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=log_file)
                    try:
                        for raw_line in proc.stdout:
                            log_file.write(raw_line.decode("utf-8", errors="replace"))
                            log_file.flush()

                            try:
                                evt = json.loads(raw_line)
                            except (json.JSONDecodeError, ValueError):
                                continue

                            evt_type = evt.get("type")

                            if evt_type == "assistant":
                                tool_names = [
                                    c.get("name", "")
                                    for c in evt.get("message", {}).get("content", [])
                                    if c.get("type") == "tool_use"
                                ]
                                if tool_names:
                                    stream_turns += 1
                                    elapsed = time.monotonic() - start
                                    _write_progress(
                                        f"Active: {', '.join(tool_names)}"
                                        f" (elapsed {elapsed:.0f}s,"
                                        f" turn {stream_turns}/{max_turns})"
                                    )
                                    if stream_turns > max_turns and not hard_stop_at:
                                        hard_stop_at = time.monotonic()
                                        _write_progress(
                                            f"Hard stop: stream turn {stream_turns}"
                                            f" exceeded {max_turns} -- waiting for result"
                                        )

                            elif evt_type == "result":
                                seg_turns = evt.get("num_turns", 0)
                                cumulative_turns += seg_turns
                                seg_cost = evt.get("total_cost_usd", 0) or 0
                                if seg_cost > total_cost_usd:
                                    total_cost_usd = seg_cost
                                _write_progress(
                                    f"Segment done ({evt.get('subtype', '')}): "
                                    f"+{seg_turns} turns, "
                                    f"{cumulative_turns}/{max_turns} cumulative, "
                                    f"cost=${total_cost_usd:.4f}"
                                )
                                if cumulative_turns >= max_turns or hard_stop_at:
                                    _write_progress("Turn budget reached -- stopping")
                                    proc.kill()
                                    break

                            if hard_stop_at and time.monotonic() - hard_stop_at > 30:
                                _write_progress("Hard stop grace period elapsed -- force killing")
                                proc.kill()
                                break

                            if time.monotonic() - start > wall_timeout:
                                _write_progress(
                                    f"Wall timeout ({wall_timeout}s) exceeded -- stopping"
                                )
                                proc.kill()
                                break
                    finally:
                        proc.wait()
                        # Drain remaining stdout (e.g. result event emitted
                        # just as the hard stop fired).
                        try:
                            for remaining in proc.stdout:
                                log_file.write(remaining.decode("utf-8", errors="replace"))
                                log_file.flush()
                                try:
                                    evt = json.loads(remaining)
                                    if evt.get("type") == "result":
                                        cumulative_turns += evt.get("num_turns", 0)
                                        seg_cost = evt.get("total_cost_usd", 0) or 0
                                        if seg_cost > total_cost_usd:
                                            total_cost_usd = seg_cost
                                except (json.JSONDecodeError, ValueError):
                                    pass
                        except OSError:
                            pass
                        _write_progress(
                            f"Process exited (code {proc.returncode}),"
                            f" cumulative turns: {cumulative_turns}"
                        )

            # Run process in a thread; poll solution file for checkpoints.
            run_future = loop.run_in_executor(None, _run_with_turn_limit)
            last_ckpt_content = initial_code
            ckpt_count = 0
            ckpt_interval = self.config.checkpoint_interval

            while not run_future.done():
                if self.shutdown_event.is_set():
                    logger.info("Shutdown requested -- stopping Claude Code container")
                    subprocess.run(
                        ["docker", "stop", "-t", "5", container_name],
                        capture_output=True,
                    )
                    break
                await asyncio.sleep(10)
                try:
                    cur = solution_path.read_text()
                except OSError:
                    continue
                if cur == last_ckpt_content or not cur.strip():
                    continue
                last_ckpt_content = cur
                ckpt_count += 1
                iteration = max(cumulative_turns, ckpt_count)
                try:
                    pid = str(uuid.uuid4())
                    er = await self.evaluator.evaluate_program(cur, pid)
                    prog = Program(
                        id=pid,
                        solution=cur,
                        language=self.config.language or "python",
                        metrics=er.metrics,
                        iteration_found=iteration,
                        parent_id=initial.id if initial else None,
                        other_context_ids=[],
                        metadata={"claude_code_checkpoint_turn": cumulative_turns},
                        artifacts=er.artifacts,
                    )
                    self.database.add(prog, iteration=iteration)
                    score = er.metrics.get("combined_score", "?")
                    _write_progress(f"[CHECKPOINT] turn ~{cumulative_turns}, score={score}")
                    if checkpoint_callback and ckpt_count % ckpt_interval == 0:
                        checkpoint_callback(iteration)
                except Exception:
                    logger.debug("Checkpoint eval failed", exc_info=True)

            await run_future

            actual_turns = cumulative_turns if cumulative_turns > 0 else stream_turns

            # Fallback: scan log for result events we might have missed.
            if total_cost_usd == 0.0:
                try:
                    for line in log_path.read_text(errors="replace").splitlines():
                        try:
                            evt = json.loads(line)
                            if evt.get("type") != "result":
                                continue
                            c = evt.get("total_cost_usd", 0) or 0
                            if c > total_cost_usd:
                                total_cost_usd = c
                            if cumulative_turns == 0:
                                actual_turns = max(actual_turns, evt.get("num_turns", 0))
                        except (json.JSONDecodeError, ValueError):
                            continue
                except OSError:
                    pass

            eval_result = await self._final_evaluation(solution_path, initial_code, initial)
            final_iter = max(actual_turns, 1)

            program = Program(
                id=str(uuid.uuid4()),
                solution=eval_result.solution,
                language=self.config.language or "python",
                metrics=eval_result.er.metrics,
                iteration_found=final_iter,
                parent_id=initial.id if initial else None,
                other_context_ids=[],
                metadata={
                    "claude_code_max_turns": max_turns,
                    "actual_turns": actual_turns,
                    "final_score_source": eval_result.source,
                },
                artifacts=eval_result.er.artifacts,
            )
            self.database.add(program, iteration=final_iter)

            if checkpoint_callback:
                checkpoint_callback(final_iter)

            run_elapsed = time.monotonic() - run_start
            if out:
                try:
                    shutil.copy(log_path, out / "claude.log")
                except OSError:
                    pass
                summary = {
                    "model": model,
                    "max_turns": max_turns,
                    "actual_turns": actual_turns,
                    "cost_usd": round(total_cost_usd, 4),
                    "wall_seconds": round(run_elapsed, 1),
                    "baseline_score": (
                        initial.metrics.get("combined_score")
                        if initial and initial.metrics
                        else None
                    ),
                    "final_score": eval_result.er.metrics.get("combined_score"),
                    "final_score_source": eval_result.source,
                }
                (out / "run_summary.json").write_text(
                    json.dumps(summary, indent=2, default=str) + "\n"
                )
                _write_progress(
                    f"Run complete: turns={actual_turns}/{max_turns}, "
                    f"cost=${total_cost_usd:.4f}, "
                    f"time={run_elapsed:.0f}s, "
                    f"score={eval_result.er.metrics.get('combined_score', '?')}"
                    f" (source={eval_result.source})"
                )

        finally:
            subprocess.run(
                ["docker", "rm", "-f", container_name],
                capture_output=True,
            )
            shutil.rmtree(workspace, ignore_errors=True)

        return self.database.get_best_program()
````

## → Calls
- [[AgenticGenerator.__init__]]
- [[CheckpointManager.__init__]]
- [[ClaudeCodeController._build_docker_cmd]]
- [[ClaudeCodeController._ensure_image_built]]
- [[ClaudeCodeController._final_evaluation]]
- [[ClaudeCodeController._save_evaluator_image]]
- [[ClaudeCodeController._write_eval_script]]
- [[ClaudeCodeController._write_task_prompt]]
- [[CodeDiversity.__init__]]
- [[Config.checkpoint_interval]]
- [[Config.evaluator]]
- [[Config.language]]
- [[Config.llm]]
- [[ContainerizedEvaluator.__init__]]
- [[ContainerizedEvaluator.evaluate_program]]
- [[ContextBuilder.__init__]]
- [[DiscoveryController.__init__]]
- [[DiscoveryControllerInput.config]]
- [[DiscoveryControllerInput.evaluation_file]]
- [[DiscoveryControllerInput.output_dir]]
- [[DiscoveryResult.output_dir]]
- [[EvaluationResult.metrics]]
- [[Evaluator.__init__]]
- [[Evaluator.evaluate_program]]
- [[EvaluatorConfig.evaluation_file]]
- [[EvaluatorConfig.file_suffix]]
- [[EvoxDatabaseConfig.evaluation_file]]
- [[HumanFeedbackReader.__init__]]
- [[HybridDiversity.__init__]]
- [[LLMJudge.__init__]]
- [[LLMPool.__init__]]
- [[LangFuseTracer.__init__]]
- [[LangFuseTracer.get]]
- [[LogWindowScorer.__init__]]
- [[MetricDiversity.__init__]]
- [[MonitorServer.__init__]]
- [[OpenAILLM.__init__]]
- [[ParadigmGenerator.__init__]]
- [[Program.id]]
- [[Program.language]]
- [[Program.metrics]]
- [[Program.solution]]
- [[ProgramDatabase.__init__]]
- [[ProgramDatabase.add]]
- [[ProgramDatabase.get]]
- [[ProgramDatabase.get_best_program]]
- [[Runner.__init__]]
- [[Runner.run]]
- [[SearchConfig.output_dir]]
- [[TaskPool.__init__]]
- [[TaskPool.run]]
- [[TemplateManager.__init__]]
- [[UnifiedArchive.__init__]]
- [[UnifiedArchive.add]]
- [[UnifiedArchive.get]]
- [[_FinalResult.__init__]]
- [[base_database.Program]]
- [[evaluation.create_evaluator]]
- [[gepa_backend.run]]
- [[openevolve_backend.run]]
- [[run_discovery._run_with_turn_limit]]
- [[run_discovery._write_progress]]
- [[shinkaevolve_backend.run]]
- [[wrapper.run]]

## ← Called by
_(entry point — nothing in this graph calls it)_
