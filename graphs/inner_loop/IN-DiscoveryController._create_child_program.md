---
name: IN-DiscoveryController._create_child_program
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
- [[IN-DiscoveryController.__init__]]
- [[IN-EvaluationResult.metrics]]
- [[IN-Evaluator.__init__]]
- [[IN-EvoxContextBuilder.__init__]]
- [[IN-LLMPool.__init__]]
- [[IN-LangFuseTracer.__init__]]
- [[IN-Program.id]]
- [[IN-Program.language]]
- [[IN-Program.metrics]]
- [[IN-ProgramDatabase.__init__]]
- [[IN-base_database.Program]]

## ← Called by
- [[IN-DiscoveryController._run_iteration]]
