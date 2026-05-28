---
name: registry.setup_search
description: function in skydiscover/search/registry.py (search-core)
metadata:
  type: project
---

# registry.setup_search

**File:** `skydiscover/search/registry.py:116`  
**Kind:** function  
**Layer:** #search-core

## Source
````python
def setup_search(
    initial_program_path: str,
    evaluation_file: str,
    config_path: str,
    output_dir: Optional[str] = None,
    evaluator_env_vars: Optional[Dict[str, str]] = None,
    parent_llm_config: Optional["LLMConfig"] = None,
) -> Tuple[DiscoveryControllerInput, str]:
    """
    Load config, create database, and build a DiscoveryControllerInput from a config path.

    This is the lightweight alternative to creating a full Runner when
    you only need the config/database/controller (e.g. for the search side of
    co-evolution).

    Args:
        parent_llm_config: If provided, inherit LLM settings (api_base, api_key,
            models) from the parent config so the search-side evolution uses the
            same endpoint as the main discovery process.

    Returns:
        Tuple of (controller_input, initial_program_solution)
    """
    config = load_config(config_path)

    # Inherit LLM settings from parent config when provided.
    # Use the parent's actual model configs (which have the correct per-model
    # api_base/api_key, e.g. Azure endpoints) rather than the top-level
    # LLMConfig defaults which may still point to api.openai.com.
    if parent_llm_config is not None and parent_llm_config.models:
        import copy

        parent_models = [copy.deepcopy(m) for m in parent_llm_config.models]
        config.llm.models = parent_models
        config.llm.evaluator_models = [copy.deepcopy(m) for m in parent_llm_config.models]
        config.llm.guide_models = [copy.deepcopy(m) for m in parent_llm_config.models]
        # Sync top-level api_base/api_key from the first parent model
        config.llm.api_base = parent_models[0].api_base or config.llm.api_base
        config.llm.api_key = parent_models[0].api_key or config.llm.api_key

    with open(initial_program_path, "r") as f:
        initial_program_solution = f.read()

    if not config.language:
        config.language = extract_solution_language(initial_program_solution)

    file_extension = os.path.splitext(initial_program_path)[1] or ".py"
    if not file_extension.startswith("."):
        file_extension = f".{file_extension}"
    if config.file_suffix == ".py":
        config.file_suffix = file_extension

    database = create_database(config.search.type, config.search.database)

    if not output_dir:
        output_dir = build_output_dir(config.search.type, initial_program_path)

    controller_input = DiscoveryControllerInput(
        config=config,
        evaluation_file=evaluation_file,
        database=database,
        file_suffix=config.file_suffix,
        output_dir=output_dir,
        evaluator_env_vars=evaluator_env_vars,
    )
    return controller_input, initial_program_solution
````

## → Calls
- [[AgenticGenerator.__init__]]
- [[CheckpointManager.__init__]]
- [[CodeDiversity.__init__]]
- [[Config.language]]
- [[Config.llm]]
- [[Config.search]]
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]
- [[ContainerizedEvaluator.__init__]]
- [[ContextBuilder.__init__]]
- [[DiscoveryController.__init__]]
- [[Evaluator.__init__]]
- [[EvaluatorConfig.file_suffix]]
- [[HumanFeedbackReader.__init__]]
- [[HybridDiversity.__init__]]
- [[LLMConfig.models]]
- [[LLMJudge.__init__]]
- [[LLMPool.__init__]]
- [[LangFuseTracer.__init__]]
- [[LogWindowScorer.__init__]]
- [[MetricDiversity.__init__]]
- [[MonitorServer.__init__]]
- [[OpenAILLM.__init__]]
- [[ParadigmGenerator.__init__]]
- [[Program.language]]
- [[ProgramDatabase.__init__]]
- [[Runner.__init__]]
- [[TaskPool.__init__]]
- [[TemplateManager.__init__]]
- [[UnifiedArchive.__init__]]
- [[_FinalResult.__init__]]
- [[code_utils.extract_solution_language]]
- [[config.build_output_dir]]
- [[config.load_config]]
- [[default_discovery_controller.DiscoveryControllerInput]]
- [[registry.create_database]]

## ← Called by
- [[CoEvolutionController._generate_and_validate_search_algorithm]]
- [[CoEvolutionController._init_search_evolution_controller]]
- [[CoEvolutionController._initialize_first_search_program]]
- [[CoEvolutionController._restore_fallback_database]]
- [[CoEvolutionController._switch_to_new_search_algorithm]]
