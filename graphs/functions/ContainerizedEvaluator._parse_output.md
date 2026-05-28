---
name: ContainerizedEvaluator._parse_output
description: method in skydiscover/evaluation/container_evaluator.py (evaluation)
metadata:
  type: project
---

# ContainerizedEvaluator._parse_output

**File:** `skydiscover/evaluation/container_evaluator.py:281`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    def _parse_output(self, stdout: str) -> EvaluationResult:
        try:
            data = json.loads(stdout.strip())
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse evaluator JSON: {e}\nOutput: {stdout!r}")
            return EvaluationResult(
                metrics={"error": 0.0},
                artifacts={"raw_output": stdout},
            )

        status = data.get("status", "error")
        combined_score = float(data.get("combined_score", 0.0))
        metrics = {
            k: float(v) for k, v in data.get("metrics", {}).items() if isinstance(v, (int, float))
        }
        if "combined_score" not in metrics:
            metrics["combined_score"] = combined_score

        artifacts = {k: str(v) for k, v in data.get("artifacts", {}).items()}
        if status != "success":
            artifacts.setdefault("status", status)

        return EvaluationResult(metrics=metrics, artifacts=artifacts)
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
- [[SerializableResult.error]]
- [[TaskPool.__init__]]
- [[TemplateManager.__init__]]
- [[UnifiedArchive.__init__]]
- [[UnifiedArchive.get]]
- [[_FinalResult.__init__]]
- [[evaluation_result.EvaluationResult]]

## ← Called by
- [[ContainerizedEvaluator._run_single_in_container]]
