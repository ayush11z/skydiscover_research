---
name: shinkaevolve_backend._to_skydiscover_program
description: function in skydiscover/extras/external/shinkaevolve_backend.py (external)
metadata:
  type: project
---

# shinkaevolve_backend._to_skydiscover_program

**File:** `skydiscover/extras/external/shinkaevolve_backend.py:127`  
**Kind:** function  
**Layer:** #external

## Source
````python
def _to_skydiscover_program(sp):
    """Convert a ShinkaEvolve Program to SkyDiscover's Program dataclass."""
    from skydiscover.search.base_database import Program

    metrics = dict(sp.public_metrics) if sp.public_metrics else {}
    metrics["combined_score"] = float(sp.combined_score or 0.0)
    metrics["correct"] = sp.correct

    return Program(
        id=sp.id,
        solution=sp.code,
        language=getattr(sp, "language", "python"),
        metrics=metrics,
        iteration_found=getattr(sp, "generation", 0),
        parent_id=getattr(sp, "parent_id", None),
        generation=getattr(sp, "generation", 0),
        timestamp=getattr(sp, "timestamp", 0.0),
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
- [[LogWindowScorer.__init__]]
- [[MetricDiversity.__init__]]
- [[MonitorServer.__init__]]
- [[OpenAILLM.__init__]]
- [[ParadigmGenerator.__init__]]
- [[Program.id]]
- [[ProgramDatabase.__init__]]
- [[Runner.__init__]]
- [[TaskPool.__init__]]
- [[TemplateManager.__init__]]
- [[UnifiedArchive.__init__]]
- [[_FinalResult.__init__]]
- [[base_database.Program]]

## ← Called by
- [[shinkaevolve_backend.run]]
- [[shinkaevolve_backend.run._poll_programs]]
