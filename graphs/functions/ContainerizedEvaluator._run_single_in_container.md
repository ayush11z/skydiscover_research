---
name: ContainerizedEvaluator._run_single_in_container
description: method in skydiscover/evaluation/container_evaluator.py (evaluation)
metadata:
  type: project
---

# ContainerizedEvaluator._run_single_in_container

**File:** `skydiscover/evaluation/container_evaluator.py:215`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    def _run_single_in_container(self, candidate_path: str, mode: str) -> EvaluationResult:
        """Execute evaluate.sh inside the container and parse its JSON output."""
        try:
            # Build docker exec command with environment variables
            cmd = ["docker", "exec"]
            for key, value in self.env_vars.items():
                cmd.extend(["-e", f"{key}={value}"])
            cmd.extend(
                [
                    self.container_id,
                    "/benchmark/evaluate.sh",
                    candidate_path,
                    mode,
                ]
            )

            proc = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=self.config.timeout,
            )
        except subprocess.TimeoutExpired:
            logger.error(f"docker exec timed out after {self.config.timeout}s")
            return EvaluationResult(
                metrics={"error": 0.0, "timeout": True},
                artifacts={"error": f"docker exec timed out after {self.config.timeout}s"},
            )
        if proc.returncode != 0:
            logger.error(f"Evaluator exited with code {proc.returncode}:\n{proc.stderr}")
            return EvaluationResult(
                metrics={"error": 0.0},
                artifacts={"stderr": proc.stderr, "exit_code": str(proc.returncode)},
            )

        result = self._parse_output(proc.stdout)
        # Always surface stderr (e.g. warnings, partial tracebacks) even on
        # successful exit — the evaluator may have caught the error internally
        # and returned valid JSON, but stderr still has useful context.
        if proc.stderr.strip():
            result.artifacts.setdefault("stderr", proc.stderr)
        return result
````

## → Calls
- [[AgenticGenerator.__init__]]
- [[CheckpointManager.__init__]]
- [[CodeDiversity.__init__]]
- [[ContainerizedEvaluator.__init__]]
- [[ContainerizedEvaluator._parse_output]]
- [[ContextBuilder.__init__]]
- [[DiscoveryController.__init__]]
- [[EvaluationResult.artifacts]]
- [[Evaluator.__init__]]
- [[EvaluatorConfig.timeout]]
- [[HumanFeedbackReader.__init__]]
- [[HybridDiversity.__init__]]
- [[LLMJudge.__init__]]
- [[LLMModelConfig.timeout]]
- [[LLMPool.__init__]]
- [[LangFuseTracer.__init__]]
- [[LogWindowScorer.__init__]]
- [[MetricDiversity.__init__]]
- [[MonitorServer.__init__]]
- [[OpenAILLM.__init__]]
- [[ParadigmGenerator.__init__]]
- [[Program.artifacts]]
- [[ProgramDatabase.__init__]]
- [[Runner.__init__]]
- [[Runner.run]]
- [[SerializableResult.error]]
- [[TaskPool.__init__]]
- [[TaskPool.run]]
- [[TemplateManager.__init__]]
- [[UnifiedArchive.__init__]]
- [[_FinalResult.__init__]]
- [[evaluation_result.EvaluationResult]]
- [[gepa_backend.run]]
- [[openevolve_backend.run]]
- [[shinkaevolve_backend.run]]
- [[wrapper.run]]

## ← Called by
- [[ContainerizedEvaluator._run_container]]
