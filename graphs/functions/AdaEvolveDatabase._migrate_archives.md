---
name: AdaEvolveDatabase._migrate_archives
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase._migrate_archives

**File:** `skydiscover/search/adaevolve/database.py:808`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _migrate_archives(self) -> None:
        """Migrate top programs between archives."""
        for src_island in range(self.num_islands):
            dest_island = (src_island + 1) % self.num_islands

            # Get top programs from source
            top_programs = self.archives[src_island].get_top_programs(self.migration_count)

            if not top_programs:
                continue

            for program in top_programs:
                # Skip if already in destination
                if self._has_duplicate_solution(dest_island, program.solution):
                    continue

                # Create migrant copy
                migrant = Program(
                    id=str(uuid.uuid4()),
                    solution=program.solution,
                    language=program.language,
                    metrics=program.metrics.copy() if program.metrics else {},
                    iteration_found=program.iteration_found,
                    parent_id=program.id,
                    generation=program.generation,
                    metadata={"migrated_from": src_island, "migrated_to": dest_island},
                )

                self.add(migrant, parent_id=None, target_island=dest_island)

            if top_programs:
                logger.debug(
                    f"Migrated {len(top_programs)} programs from island {src_island} "
                    f"to island {dest_island}"
                )
````

## → Calls
- [[AdaEvolveDatabase._has_duplicate_solution]]
- [[AdaEvolveDatabase.add]]
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
- [[ProgramDatabase.__init__]]
- [[Runner.__init__]]
- [[TaskPool.__init__]]
- [[TemplateManager.__init__]]
- [[UnifiedArchive.__init__]]
- [[_FinalResult.__init__]]
- [[base_database.Program]]

## ← Called by
- [[AdaEvolveDatabase._migrate]]
