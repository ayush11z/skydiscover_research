---
name: TemplateManager.__init__
description: method in skydiscover/context_builder/utils.py (context-builder)
metadata:
  type: project
---

# TemplateManager.__init__

**File:** `skydiscover/context_builder/utils.py:14`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def __init__(self, *directories: Optional[str]):
        """
        Initializes the TemplateManager with the given directories.
        If there are multiple directories, the templates from the later directories will override
        the templates from the earlier directories.
        """
        self.templates: dict[str, str] = {}
        for d in directories:
            if d:
                path = Path(d)
                if path.exists():
                    self._load_from_directory(path)
````

## → Calls
- [[TemplateManager._load_from_directory]]

## ← Called by
- [[AdaEvolveContextBuilder.__init__]]
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
- [[DefaultContextBuilder.__init__]]
- [[DiscoveryController._call_llm]]
- [[DiscoveryController._create_child_program]]
- [[DiscoveryController._run_from_scratch_iteration]]
- [[DiscoveryController._run_iteration]]
- [[EvaluationResult.from_dict]]
- [[Evaluator._cascade_evaluate]]
- [[Evaluator._normalize_result]]
- [[Evaluator.evaluate_program]]
- [[EvoxContextBuilder.__init__]]
- [[GEPANativeContextBuilder.__init__]]
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
