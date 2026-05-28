---
name: DiscoveryController._create_child_program
description: method in skydiscover/search/default_discovery_controller.py (inner-loop)
metadata:
  type: project
---

# DiscoveryController._create_child_program

**File:** `skydiscover/search/default_discovery_controller.py:859`  
**Kind:** method  
**Layer:** #inner-loop

## Source
````python
    def _create_child_program(
        self,
        child_id: str,
        child_solution: str,
        parent: Program,
        context_program_ids: list,
        parent_info: tuple,
        context_info: list,
        child_metrics: Dict[str, Any],
        iteration: int,
        changes_summary: Optional[str],
        extra_metadata: Optional[Dict[str, Any]] = None,
        artifacts: Optional[Dict[str, Any]] = None,
    ) -> Program:
        """Create a child program with the given attributes."""
        metadata = {
            "changes": changes_summary,
            "parent_metrics": parent.metrics,
        }
        if extra_metadata:
            metadata.update(extra_metadata)

        return Program(
            id=child_id,
            solution=child_solution,
            language=self.config.language,
            parent_id=parent.id,
            other_context_ids=context_program_ids,
            parent_info=parent_info,
            context_info=context_info,
            metrics=child_metrics,
            iteration_found=iteration,
            metadata=metadata,
            artifacts=artifacts or {},
        )
````

## → Calls
- [[AgenticGenerator.__init__]]
- [[CheckpointManager.__init__]]
- [[CodeDiversity.__init__]]
- [[Config.language]]
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
- [[Program.language]]
- [[Program.metrics]]
- [[ProgramDatabase.__init__]]
- [[Runner.__init__]]
- [[TaskPool.__init__]]
- [[TemplateManager.__init__]]
- [[UnifiedArchive.__init__]]
- [[_FinalResult.__init__]]
- [[base_database.Program]]

## ← Called by
- [[DiscoveryController._run_iteration]]
