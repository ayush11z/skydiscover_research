---
name: OpenEvolveNativeDatabase._seed_empty_island
description: method in skydiscover/search/openevolve_native/database.py (openevolve)
metadata:
  type: project
---

# OpenEvolveNativeDatabase._seed_empty_island

**File:** `skydiscover/search/openevolve_native/database.py:344`  
**Kind:** method  
**Layer:** #openevolve

## Source
````python
    def _seed_empty_island(self, island_idx: int) -> Program:
        """Seed an empty island with a copy of the best program."""
        if self.best_program_id and self.best_program_id in self.programs:
            best = self.programs[self.best_program_id]
            copy = Program(
                id=str(uuid.uuid4()),
                solution=best.solution,
                language=best.language,
                parent_id=best.id,
                generation=best.generation,
                metrics=best.metrics.copy(),
                metadata={"island": island_idx},
                iteration_found=self.last_iteration,
            )
            self.programs[copy.id] = copy
            self.islands[island_idx].add(copy.id)
            return copy
        return next(iter(self.programs.values()))
````

## → Calls
- [[AgenticGenerator.__init__]]
- [[CheckpointManager.__init__]]
- [[CheckpointManager.load]]
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
- [[OpenEvolveNativeDatabase._sample_exploration_parent]]
