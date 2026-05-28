---
name: IO-DiscoveryController.__init__
description: method in skydiscover/search/default_discovery_controller.py (inner-loop)
metadata:
  type: project
---

# DiscoveryController.__init__

**File:** `skydiscover/search/default_discovery_controller.py:63`  
**Kind:** method  
**Layer:** #inner-loop

## Source
````python
    def __init__(self, controller_input: DiscoveryControllerInput):
        self.config = controller_input.config
        self.evaluation_file = controller_input.evaluation_file
        self.database = controller_input.database
        self.file_suffix = controller_input.file_suffix
        self.output_dir = controller_input.output_dir
        self.evaluator_env_vars = controller_input.evaluator_env_vars

        self.shutdown_event = mp.Event()
        self.early_stopping_triggered = False

        self.llms = LLMPool(self.config.llm.models)
        self.evaluator_llms = LLMPool(self.config.llm.evaluator_models)
        self.guide_llms = LLMPool(self.config.llm.guide_models)

        self._init_context_builder()

        self.config.evaluator.evaluation_file = self.evaluation_file
        self.config.evaluator.file_suffix = self.file_suffix
        self.config.evaluator.is_image_mode = self.config.language == "image"

        llm_judge = None
        if self.config.evaluator.llm_as_judge:
            ctx = DefaultContextBuilder(self.config)
            ctx.set_templates("evaluator_system_message")
            llm_judge = LLMJudge(self.evaluator_llms, ctx, self.database)

        self.evaluator = create_evaluator(
            self.config.evaluator,
            llm_judge=llm_judge,
            max_concurrent=max(self.config.max_parallel_iterations, 4),
            env_vars=controller_input.evaluator_env_vars,
        )

        self.agentic_generator = None
        if self.config.agentic.enabled:
            from skydiscover.llm.agentic_generator import AgenticGenerator

            self.agentic_generator = AgenticGenerator(self.llms, self.config.agentic)
            logger.info(f"Agentic mode enabled (codebase: {self.config.agentic.codebase_root})")

        self.num_context_programs = controller_input.config.search.num_context_programs

        self.monitor_callback: Optional[Callable] = None
        self.feedback_reader: Optional[Any] = None
        self._prompt_context: Dict[str, Any] = {}
        self._solution_prompt_counter = 0

        # Load evaluator/task description and inject into system message so
        # the LLM knows what problem to solve (especially for from-scratch).
        self._inject_evaluator_context()

        logger.info(
            f"DiscoveryController initialized: num_context_programs={self.num_context_programs}"
        )
````

## → Calls
- [[IO-AgenticGenerator.__init__]]
- [[IO-DiscoveryController._init_context_builder]]
- [[IO-DiscoveryController._inject_evaluator_context]]
- [[IO-DiscoveryControllerInput.config]]
- [[IO-DiscoveryControllerInput.database]]
- [[IO-DiscoveryControllerInput.evaluation_file]]
- [[IO-DiscoveryControllerInput.evaluator_env_vars]]
- [[IO-DiscoveryControllerInput.file_suffix]]
- [[IO-DiscoveryControllerInput.output_dir]]
- [[IO-LLMPool.__init__]]
- [[IO-Program.language]]
- [[IO-agentic_generator.AgenticGenerator]]
- [[IO-default_discovery_controller.DiscoveryControllerInput]]
- [[IO-llm_pool.LLMPool]]

## ← Called by
- [[IO-CoEvolutionController.__init__]]
- [[IO-CoEvolutionController._init_search_evolution_controller]]
- [[IO-DiscoveryController._build_prompt]]
- [[IO-DiscoveryController._call_llm]]
- [[IO-DiscoveryController._create_child_program]]
- [[IO-DiscoveryController._run_from_scratch_iteration]]
- [[IO-DiscoveryController._run_iteration]]
- [[IO-Runner.run]]
