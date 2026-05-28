---
name: OpenEvolveNativeDatabase._migrate_programs
description: method in skydiscover/search/openevolve_native/database.py (openevolve)
metadata:
  type: project
---

# OpenEvolveNativeDatabase._migrate_programs

**File:** `skydiscover/search/openevolve_native/database.py:750`  
**Kind:** method  
**Layer:** #openevolve

## Source
````python
    def _migrate_programs(self) -> None:
        if self.num_islands < 2:
            return
        logger.info("Performing migration between islands")

        for i, island in enumerate(self.islands):
            if not island:
                continue
            island_progs = [self.programs[pid] for pid in island if pid in self.programs]
            if not island_progs:
                continue

            island_progs.sort(
                key=lambda p: _get_fitness(p.metrics, self.feature_dimensions),
                reverse=True,
            )
            num_migrants = max(1, int(len(island_progs) * self.migration_rate))
            migrants = island_progs[:num_migrants]

            targets = [
                (i + 1) % self.num_islands,
                (i - 1) % self.num_islands,
            ]

            for migrant in migrants:
                # Skip already-migrated programs to prevent exponential
                # duplication (all copies map to same MAP-Elites cell).
                if migrant.metadata.get("migrant", False):
                    continue

                for target in targets:
                    # Skip if target island already has identical solution
                    target_progs = [
                        self.programs[pid] for pid in self.islands[target] if pid in self.programs
                    ]
                    if any(p.solution == migrant.solution for p in target_progs):
                        continue

                    copy = Program(
                        id=str(uuid.uuid4()),
                        solution=migrant.solution,
                        language=migrant.language,
                        parent_id=migrant.id,
                        generation=migrant.generation,
                        metrics=migrant.metrics.copy(),
                        metadata={
                            **migrant.metadata,
                            "island": target,
                            "migrant": True,
                        },
                    )
                    self.add(
                        copy,
                        target_island=target,
                        _is_migration=True,
                    )

        self.last_migration_generation = max(self.island_generations)
        logger.info(
            "Migration completed at generation %d",
            self.last_migration_generation,
        )
````

## → Calls
- [[AgenticGenerator.__init__]]
- [[CheckpointManager.__init__]]
- [[CheckpointManager.load]]
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
- [[LangFuseTracer.get]]
- [[LogWindowScorer.__init__]]
- [[MetricDiversity.__init__]]
- [[MonitorServer.__init__]]
- [[OpenAILLM.__init__]]
- [[OpenEvolveNativeDatabase.add]]
- [[ParadigmGenerator.__init__]]
- [[Program.metrics]]
- [[Program.solution]]
- [[ProgramDatabase.__init__]]
- [[ProgramDatabase.get]]
- [[Runner.__init__]]
- [[TaskPool.__init__]]
- [[TemplateManager.__init__]]
- [[UnifiedArchive.__init__]]
- [[UnifiedArchive.get]]
- [[_FinalResult.__init__]]
- [[base_database.Program]]
- [[database._get_fitness]]

## ← Called by
- [[OpenEvolveNativeDatabase.add]]
