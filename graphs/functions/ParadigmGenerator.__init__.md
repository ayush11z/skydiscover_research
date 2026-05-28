---
name: ParadigmGenerator.__init__
description: method in skydiscover/search/adaevolve/paradigm/generator.py (adaevolve)
metadata:
  type: project
---

# ParadigmGenerator.__init__

**File:** `skydiscover/search/adaevolve/paradigm/generator.py:46`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def __init__(
        self,
        llm_pool: LLMPool,
        system_message: str = "",
        evaluator_code: str = "",
        num_paradigms: int = 3,
        eval_timeout: int = 300,
        language: str = "python",
        objective_names: Optional[List[str]] = None,
        higher_is_better: Optional[Dict[str, bool]] = None,
        fitness_key: Optional[str] = None,
    ):
        """
        Initialize the paradigm generator.

        Args:
            llm_pool: LLM pool for generation
            system_message: Problem description from config
            evaluator_code: Evaluator source code
            num_paradigms: Number of paradigms to generate per call
            eval_timeout: Evaluation timeout in seconds
            language: Language of the solution being evolved ("python" for code, "image" for images, etc.)
        """
        self.llm_pool = llm_pool
        self.system_message = system_message
        self.evaluator_code = evaluator_code
        self.num_paradigms = num_paradigms
        self.eval_timeout = eval_timeout
        self.language = language
        self._is_image_mode = language.lower() == "image"
        self._is_prompt_optimization = language.lower() in ("text", "prompt", "image")
        self.objective_names = list(objective_names or [])
        self.higher_is_better = dict(higher_is_better or {})
        self.fitness_key = fitness_key
````

## → Calls
- [[llm_pool.LLMPool]]

## ← Called by
- [[AdaEvolveController._ensure_all_islands_seeded]]
- [[AdaEvolveController._execute_generation]]
- [[AdaEvolveController._generate_child]]
- [[AdaEvolveController._process_result]]
- [[AdaEvolveController._run_normal_step]]
- [[AdaEvolveDatabase.__init__]]
- [[AdaEvolveDatabase._expand_to_island_count]]
- [[AdaEvolveDatabase._migrate_archives]]
- [[AdaEvolveDatabase._migrate_legacy]]
- [[AdaEvolveDatabase._seed_new_island]]
- [[AdaEvolveDatabase._spawn_island]]
- [[AdaEvolveDatabase.seed_all_islands]]
- [[AdaptiveState.from_dict]]
- [[ClaudeCodeController.run_discovery]]
- [[CoEvolutionController._initialize_first_search_program]]
- [[Config.from_dict]]
- [[ContainerizedEvaluator._parse_output]]
- [[ContainerizedEvaluator._run_single_in_container]]
- [[ContainerizedEvaluator.evaluate_program]]
- [[DiscoveryController._call_llm]]
- [[DiscoveryController._create_child_program]]
- [[DiscoveryController._run_from_scratch_iteration]]
- [[DiscoveryController._run_iteration]]
- [[EvaluationResult.from_dict]]
- [[Evaluator._cascade_evaluate]]
- [[Evaluator._normalize_result]]
- [[Evaluator.evaluate_program]]
- [[GEPANativeController._attempt_merge]]
- [[HarborEvaluator._read_reward]]
- [[HarborEvaluator._run_container]]
- [[LLMJudge.evaluate]]
- [[MultiDimensionalAdapter.add_dimension]]
- [[MultiDimensionalAdapter.from_dict]]
- [[OpenAILLM._generate_with_image]]
- [[OpenAILLM.generate]]
- [[OpenEvolveNativeDatabase._migrate_programs]]
- [[OpenEvolveNativeDatabase._seed_empty_island]]
- [[ParadigmGenerator.generate]]
- [[ParadigmTracker.from_dict]]
- [[Program.from_dict]]
- [[Runner.run]]
- [[UnifiedArchive.__init__]]
- [[_ConsoleFormatter.format]]
- [[_make_gepa_evaluator.gepa_evaluator]]
- [[api._run_discovery_async]]
- [[cli._configure_logging]]
- [[config.apply_overrides]]
- [[config.load_config]]
- [[gepa_backend.run]]
- [[logging_utils.setup_search_logging]]
- [[openevolve_backend._to_skydiscover_program]]
- [[openevolve_backend.run]]
- [[registry.setup_search]]
- [[search_strategy_evaluator.evaluate]]
- [[shinkaevolve_backend._to_skydiscover_program]]
- [[shinkaevolve_backend.run]]
- [[variation_operator_generator.main]]
