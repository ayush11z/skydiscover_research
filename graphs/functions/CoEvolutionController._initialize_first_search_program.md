---
name: CoEvolutionController._initialize_first_search_program
description: method in skydiscover/search/evox/controller.py (outer-loop)
metadata:
  type: project
---

# CoEvolutionController._initialize_first_search_program

**File:** `skydiscover/search/evox/controller.py:247`  
**Kind:** method  
**Layer:** #outer-loop

## Source
````python
    async def _initialize_first_search_program(self, solution_iter: int) -> None:
        """Initialize and score the first (file-based) search program."""
        start_score = (
            self.search_scorer.get_start_score()
            or getattr(self.database, "initial_program_score", None)
            or 0.0
        )
        metrics = self._compute_search_metrics(
            start_score=start_score,
            best_scores=None,
            horizon=self._switch_interval,
            start_iteration=0,
        )
        search_score = float(metrics.get("combined_score", 0.0) or 0.0)

        initial_program = get_program(
            self.search_controller.config,
            self._search_initial_code,
            str(uuid.uuid4()),
            metrics,
            self._num_search_evolutions,
        )
        initial_program.metadata = initial_program.metadata or {}
        initial_program.metadata["start_db_stats"] = make_json_serializable(self.start_db_stats)
        initial_program.metadata["end_db_stats"] = make_json_serializable(
            self.database.get_statistics(improvement_threshold=self.DEFAULT_IMPROVEMENT_THRESHOLD)
        )

        initial_result = SerializableResult(
            child_program_dict=initial_program.to_dict(), iteration=self._num_search_evolutions
        )
        self._best_search_score = search_score
        await self.search_controller.postprocess_result(
            initial_result, self._num_search_evolutions, verbose=False
        )

        self.search_controller.database.initial_program_id = initial_program.id
        self.search_controller.database.initial_program_score = search_score
        self._num_search_evolutions += 1

        self._reset_search_window()
        await self._generate_and_validate_search_algorithm(solution_iter)
````

## → Calls
- [[AdaptiveState.to_dict]]
- [[AgenticGenerator.__init__]]
- [[CheckpointManager.__init__]]
- [[CoEvolutionController._compute_search_metrics]]
- [[CoEvolutionController._generate_and_validate_search_algorithm]]
- [[CoEvolutionController._reset_search_window]]
- [[CodeDiversity.__init__]]
- [[Config.to_dict]]
- [[ContainerizedEvaluator.__init__]]
- [[ContextBuilder.__init__]]
- [[DiscoveryController.__init__]]
- [[DiscoveryController.postprocess_result]]
- [[DiscoveryControllerInput.config]]
- [[DiscoveryControllerInput.database]]
- [[EvaluationResult.to_dict]]
- [[Evaluator.__init__]]
- [[HumanFeedbackReader.__init__]]
- [[HybridDiversity.__init__]]
- [[LLMJudge.__init__]]
- [[LLMPool.__init__]]
- [[LangFuseTracer.__init__]]
- [[LangFuseTracer.get]]
- [[LogWindowScorer.__init__]]
- [[LogWindowScorer.get_start_score]]
- [[MetricDiversity.__init__]]
- [[MonitorServer.__init__]]
- [[OpenAILLM.__init__]]
- [[ParadigmGenerator.__init__]]
- [[ParadigmTracker.to_dict]]
- [[Program.id]]
- [[Program.metadata]]
- [[Program.to_dict]]
- [[ProgramDatabase.__init__]]
- [[ProgramDatabase.get]]
- [[ProgramDatabase.get_statistics]]
- [[Runner.__init__]]
- [[SearchConfig.database]]
- [[TaskPool.__init__]]
- [[TemplateManager.__init__]]
- [[UnifiedArchive.__init__]]
- [[UnifiedArchive.get]]
- [[_FinalResult.__init__]]
- [[coevolve_logging.make_json_serializable]]
- [[default_discovery_controller.DiscoveryController]]
- [[discovery_utils.SerializableResult]]
- [[registry.get_program]]
- [[registry.setup_search]]

## ← Called by
- [[CoEvolutionController._evolve_search]]
