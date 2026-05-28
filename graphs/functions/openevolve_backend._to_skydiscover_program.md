---
name: openevolve_backend._to_skydiscover_program
description: function in skydiscover/extras/external/openevolve_backend.py (external)
metadata:
  type: project
---

# openevolve_backend._to_skydiscover_program

**File:** `skydiscover/extras/external/openevolve_backend.py:149`  
**Kind:** function  
**Layer:** #external

## Source
````python
def _to_skydiscover_program(oe_prog):
    from skydiscover.search.base_database import Program

    return Program(
        id=oe_prog.id,
        solution=oe_prog.code,
        language=getattr(oe_prog, "language", "python"),
        metrics=oe_prog.metrics or {},
        iteration_found=getattr(oe_prog, "iteration_found", 0),
        parent_id=getattr(oe_prog, "parent_id", None),
        generation=getattr(oe_prog, "generation", 0),
        timestamp=getattr(oe_prog, "timestamp", 0.0),
    )
````

## → Calls
- [[AgenticGenerator.__init__]]
- [[CheckpointManager.__init__]]
- [[CodeDiversity.__init__]]
- [[ContainerizedEvaluator.__init__]]
- [[ContextBuilder.__init__]]
- [[DiscoveryController.__init__]]
- [[EvaluationResult.metrics]]
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
- [[Program.metrics]]
- [[ProgramDatabase.__init__]]
- [[Runner.__init__]]
- [[TaskPool.__init__]]
- [[TemplateManager.__init__]]
- [[UnifiedArchive.__init__]]
- [[_FinalResult.__init__]]
- [[base_database.Program]]

## ← Called by
- [[openevolve_backend.run]]
- [[openevolve_backend.run._poll_programs]]
