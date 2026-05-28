---
name: HarborEvaluator._run_container
description: method in skydiscover/evaluation/harbor_evaluator.py (evaluation)
metadata:
  type: project
---

# HarborEvaluator._run_container

**File:** `skydiscover/evaluation/harbor_evaluator.py:83`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    def _run_container(self, program_solution: str, mode: str) -> EvaluationResult:
        """Inject solution, run tests, read reward."""
        # Clear stale reward files from previous evaluations.
        self._exec("rm -f /logs/verifier/reward.txt /logs/verifier/reward.json")

        # Ensure parent directory exists and inject solution.
        parent_dir = os.path.dirname(self.solution_path)
        if parent_dir:
            self._exec(f"mkdir -p '{parent_dir}'")
        inject = subprocess.run(
            [
                "docker",
                "exec",
                "-i",
                self.container_id,
                "/bin/sh",
                "-c",
                f"cat > '{self.solution_path}'",
            ],
            input=program_solution.encode(),
            capture_output=True,
        )
        if inject.returncode != 0:
            logger.error(f"Failed to inject solution: {inject.stderr.decode()}")
            return EvaluationResult(
                metrics={"combined_score": 0.0},
                artifacts={"error": f"injection failed: {inject.stderr.decode()}"},
            )

        try:
            # Run tests.
            proc = subprocess.run(
                [
                    "docker",
                    "exec",
                    self.container_id,
                    "bash",
                    "-c",
                    "chmod +x /tests/test.sh && /tests/test.sh",
                ],
                capture_output=True,
                text=True,
                timeout=self.config.timeout,
            )

            # Read reward regardless of exit code — test.sh may exit non-zero
            # but still write a reward (e.g. partial credit).
            result = self._read_reward(proc.stdout, proc.stderr)

            if proc.returncode != 0:
                result.artifacts.setdefault("test_exit_code", str(proc.returncode))
            if proc.stderr.strip():
                result.artifacts.setdefault("stderr", proc.stderr)
            if proc.stdout.strip():
                result.artifacts.setdefault("stdout", proc.stdout)

            return result
        except subprocess.TimeoutExpired:
            logger.error(f"docker exec timed out after {self.config.timeout}s")
            return EvaluationResult(
                metrics={"combined_score": 0.0},
                artifacts={"error": f"docker exec timed out after {self.config.timeout}s"},
            )

        finally:
            # Clean up solution so the container is fresh for next evaluation.
            self._exec(f"rm -f '{self.solution_path}'")
````

## → Calls
- [[AgenticGenerator.__init__]]
- [[CheckpointManager.__init__]]
- [[CodeDiversity.__init__]]
- [[ContainerizedEvaluator.__init__]]
- [[ContextBuilder.__init__]]
- [[DiscoveryController.__init__]]
- [[DiscoveryControllerInput.config]]
- [[EvaluationResult.artifacts]]
- [[Evaluator.__init__]]
- [[HarborEvaluator._exec]]
- [[HarborEvaluator._extract_solution_path]]
- [[HarborEvaluator._read_reward]]
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
- [[container_evaluator.ContainerizedEvaluator]]
- [[evaluation_result.EvaluationResult]]
- [[gepa_backend.run]]
- [[openevolve_backend.run]]
- [[shinkaevolve_backend.run]]
- [[wrapper.run]]

## ← Called by
_(entry point — nothing in this graph calls it)_
