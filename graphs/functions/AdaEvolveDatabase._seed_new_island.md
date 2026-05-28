---
name: AdaEvolveDatabase._seed_new_island
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase._seed_new_island

**File:** `skydiscover/search/adaevolve/database.py:2126`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _seed_new_island(self, island_idx: int) -> None:
        """Seed a new island with top programs from existing islands."""
        # Gather top programs from all existing islands
        all_programs = []
        for i in range(island_idx):  # Don't include the new island
            all_programs.extend(self.archives[i].get_all())

        if not all_programs:
            return

        # Get top programs to seed
        sorted_programs = sorted(all_programs, key=self._get_fitness, reverse=True)
        seed_count = min(5, len(sorted_programs))

        for program in sorted_programs[:seed_count]:
            # Create copy for new island
            copy = Program(
                id=str(uuid.uuid4()),
                solution=program.solution,
                language=program.language,
                metrics=program.metrics.copy() if program.metrics else {},
                iteration_found=self._iteration_count,
                parent_id=program.id,
                generation=program.generation,
                metadata={"seeded_to_spawned_island": island_idx},
            )
            self.archives[island_idx].add(copy)
            self.programs[copy.id] = copy

        self._invalidate_global_pareto_cache()
````

## → Calls
- [[AdaEvolveDatabase._get_fitness]]
- [[AdaEvolveDatabase._invalidate_global_pareto_cache]]
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
- [[TaskPool.__init__]]
- [[TemplateManager.__init__]]
- [[UnifiedArchive.__init__]]
- [[UnifiedArchive.get]]
- [[_FinalResult.__init__]]
- [[base_database.Program]]

## ← Called by
- [[AdaEvolveDatabase._spawn_island]]
