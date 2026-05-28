---
name: _make_gepa_evaluator.gepa_evaluator
description: function in skydiscover/extras/external/gepa_backend.py (external)
metadata:
  type: project
---

# _make_gepa_evaluator.gepa_evaluator

**File:** `skydiscover/extras/external/gepa_backend.py:46`  
**Kind:** function  
**Layer:** #external

## Source
````python
    def gepa_evaluator(candidate: str, **kwargs) -> tuple[float, dict]:
        # Write candidate code to a temp file so the SkyDiscover evaluator can load it.
        # Reconstruct the full file if prefix/suffix exist (code outside EVOLVE block).
        full_solution = solution_prefix + candidate + solution_suffix
        tmp = tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".py",
            prefix="gepa_candidate_",
            delete=False,
        )
        try:
            tmp.write(full_solution)
            tmp.flush()
            tmp.close()

            metrics = user_evaluate(tmp.name)

            # Normalise to (score, side_info)
            if isinstance(metrics, (int, float)):
                score = float(metrics)
                metrics = {"combined_score": score}
            else:
                score = metrics.get("combined_score")
                if score is None:
                    nums = [
                        float(v)
                        for v in metrics.values()
                        if isinstance(v, (int, float)) and not isinstance(v, bool)
                    ]
                    score = sum(nums) / len(nums) if nums else 0.0

            eval_counter[0] += 1

            # Push to monitor if callback provided
            if monitor_callback and score > 0:
                try:
                    from skydiscover.search.base_database import Program

                    prog = Program(
                        id=str(uuid.uuid4()),
                        solution=candidate,
                        language="python",
                        metrics={
                            "combined_score": float(score),
                            **(metrics if isinstance(metrics, dict) else {}),
                        },
                        iteration_found=eval_counter[0],
                        generation=eval_counter[0],
                    )
                    monitor_callback(prog, eval_counter[0])
                except Exception:
                    logger.debug("Monitor callback error", exc_info=True)

            return float(score), metrics
        except Exception as e:
            logger.warning("GEPA evaluator error: %s", e)
            return 0.0, {"error": str(e)}
        finally:
            try:
                os.unlink(tmp.name)
            except OSError:
                pass
````

## → Calls
- [[AgenticGenerator.__init__]]
- [[BenchmarkConfig.name]]
- [[CheckpointManager.__init__]]
- [[CodeDiversity.__init__]]
- [[ContainerizedEvaluator.__init__]]
- [[ContainerizedEvaluator.close]]
- [[ContextBuilder.__init__]]
- [[DiscoveryController.__init__]]
- [[DiscoveryController.close]]
- [[Evaluator.__init__]]
- [[Evaluator.close]]
- [[HumanFeedbackReader.__init__]]
- [[HybridDiversity.__init__]]
- [[LLMJudge.__init__]]
- [[LLMModelConfig.name]]
- [[LLMPool.__init__]]
- [[LangFuseTracer.__init__]]
- [[LogWindowScorer.__init__]]
- [[MetricDiversity.__init__]]
- [[MonitorServer.__init__]]
- [[OpenAILLM.__init__]]
- [[ParadigmGenerator.__init__]]
- [[ProgramDatabase.__init__]]
- [[Runner.__init__]]
- [[TaskPool.__init__]]
- [[TemplateManager.__init__]]
- [[UnifiedArchive.__init__]]
- [[_FinalResult.__init__]]
- [[base_database.Program]]

## ← Called by
- [[gepa_backend._make_gepa_evaluator]]
