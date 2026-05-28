---
name: HarborEvaluator._read_reward
description: method in skydiscover/evaluation/harbor_evaluator.py (evaluation)
metadata:
  type: project
---

# HarborEvaluator._read_reward

**File:** `skydiscover/evaluation/harbor_evaluator.py:188`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    def _read_reward(self, test_stdout: str = "", test_stderr: str = "") -> EvaluationResult:
        """Read the reward from /logs/verifier/reward.txt or reward.json."""
        for path, is_json in [
            ("/logs/verifier/reward.json", True),
            ("/logs/verifier/reward.txt", False),
        ]:
            proc = subprocess.run(
                ["docker", "exec", self.container_id, "cat", path],
                capture_output=True,
                text=True,
            )
            if proc.returncode != 0 or not proc.stdout.strip():
                continue

            try:
                if is_json:
                    data = json.loads(proc.stdout.strip())
                    raw = data.get("reward", data.get("score"))
                    if raw is None:
                        logger.warning(
                            "No 'reward' or 'score' key in %s; defaulting to 0",
                            path,
                        )
                        raw = 0
                    reward = float(raw)
                    metrics = {"combined_score": reward}
                    for k, v in data.items():
                        if isinstance(v, (int, float)) and k not in (
                            "reward",
                            "score",
                        ):
                            metrics[k] = float(v)
                    return EvaluationResult(metrics=metrics)
                else:
                    reward = float(proc.stdout.strip())
                    return EvaluationResult(metrics={"combined_score": reward})
            except (ValueError, json.JSONDecodeError, StopIteration) as e:
                logger.warning(f"Failed to parse reward from {path}: {e}")
                continue

        logger.error("No reward file found in /logs/verifier/")
        return EvaluationResult(
            metrics={"combined_score": 0.0},
            artifacts={
                "error": "no reward file written by test.sh",
                "test_stdout": test_stdout,
                "test_stderr": test_stderr,
            },
        )
````

## → Calls
- [[AgenticGenerator.__init__]]
- [[CheckpointManager.__init__]]
- [[CodeDiversity.__init__]]
- [[ContainerizedEvaluator.__init__]]
- [[ContextBuilder.__init__]]
- [[DiscoveryController.__init__]]
- [[Evaluator.__init__]]
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
- [[ProgramDatabase.__init__]]
- [[ProgramDatabase.get]]
- [[Runner.__init__]]
- [[Runner.run]]
- [[SerializableResult.error]]
- [[TaskPool.__init__]]
- [[TaskPool.run]]
- [[TemplateManager.__init__]]
- [[UnifiedArchive.__init__]]
- [[UnifiedArchive.get]]
- [[_FinalResult.__init__]]
- [[container_evaluator.ContainerizedEvaluator]]
- [[evaluation_result.EvaluationResult]]
- [[gepa_backend.run]]
- [[openevolve_backend.run]]
- [[shinkaevolve_backend.run]]
- [[wrapper.run]]

## ← Called by
- [[HarborEvaluator._run_container]]
