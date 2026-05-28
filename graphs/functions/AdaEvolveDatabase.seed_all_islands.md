---
name: AdaEvolveDatabase.seed_all_islands
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase.seed_all_islands

**File:** `skydiscover/search/adaevolve/database.py:374`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def seed_all_islands(self, program: Program, iteration: Optional[int] = None) -> None:
        """
        Seed all islands with copies of the initial program.

        Args:
            program: The initial/seed program to copy to all islands
            iteration: Current iteration (for tracking)
        """
        logger.info(f"Seeding all {self.num_islands} islands with initial program")

        for island_idx in range(self.num_islands):
            if island_idx == 0:
                # Add original program to island 0
                self.add(program, iteration=iteration, target_island=0)
            else:
                # Create a copy with new ID for other islands
                copy = Program(
                    id=str(uuid.uuid4()),
                    solution=program.solution,
                    language=program.language,
                    metrics=program.metrics.copy() if program.metrics else {},
                    iteration_found=iteration or 0,
                    parent_id=None,
                    generation=0,
                    metadata={"seeded_to_island": island_idx},
                )
                self.add(copy, iteration=iteration, target_island=island_idx)

        logger.info(
            f"All islands seeded. Island sizes: "
            f"{[self.get_island_size(i) for i in range(self.num_islands)]}"
        )
````

## → Calls
- [[AdaEvolveDatabase.add]]
- [[AdaEvolveDatabase.get_island_size]]
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
- [[Program.language]]
- [[Program.metrics]]
- [[Program.solution]]
- [[ProgramDatabase.__init__]]
- [[Runner.__init__]]
- [[TaskPool.__init__]]
- [[TemplateManager.__init__]]
- [[UnifiedArchive.__init__]]
- [[_FinalResult.__init__]]
- [[base_database.Program]]

## ← Called by
_(entry point — nothing in this graph calls it)_
