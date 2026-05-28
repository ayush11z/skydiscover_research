---
name: ContainerizedEvaluator.__exit__
description: method in skydiscover/evaluation/container_evaluator.py (evaluation)
metadata:
  type: project
---

# ContainerizedEvaluator.__exit__

**File:** `skydiscover/evaluation/container_evaluator.py:118`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
````

## → Calls
- [[ContainerizedEvaluator.close]]

## ← Called by
- [[AdaEvolveController._log_iteration_stats]]
- [[AdaEvolveDatabase.load]]
- [[AdaEvolveDatabase.save]]
- [[AgenticGenerator._tool_read_file]]
- [[AgenticGenerator._tool_search]]
- [[BeamSearchDatabase.load]]
- [[BeamSearchDatabase.save]]
- [[CheckpointManager._save_program]]
- [[CheckpointManager.load]]
- [[CheckpointManager.save]]
- [[CoEvolutionController._switch_to_new_search_algorithm]]
- [[Config.from_yaml]]
- [[Config.to_yaml]]
- [[DiscoveryController._save_solution_prompt]]
- [[Evaluator._call_with_env]]
- [[Evaluator._scoped_env]]
- [[Evaluator.evaluate_program]]
- [[EvoxContextBuilder.__init__]]
- [[EvoxContextBuilder._save_guide_prompt]]
- [[GEPANativeDatabase.load]]
- [[GEPANativeDatabase.save]]
- [[HarborEvaluator._apply_task_toml_timeout]]
- [[HarborEvaluator._extract_path_from_instruction]]
- [[HarborEvaluator._extract_path_from_solve_sh]]
- [[HumanFeedbackReader._create_initial_file]]
- [[HumanFeedbackReader._write_feedback]]
- [[HumanFeedbackReader.read]]
- [[MonitorServer._call_llm_api]]
- [[MonitorServer._handle_client_msg]]
- [[OpenAILLM._generate_with_image]]
- [[OpenEvolveNativeDatabase.load]]
- [[OpenEvolveNativeDatabase.save]]
- [[Runner._load_initial_program]]
- [[Runner._save_best_program]]
- [[Runner._save_checkpoint]]
- [[TemplateManager._load_from_directory]]
- [[build_image_content._encode_image]]
- [[builder.run_async_safely]]
- [[coevolve_logging.log_active_algorithm]]
- [[coevolve_logging.log_failed_attempt]]
- [[coevolve_logging.save_search_algorithm]]
- [[coevolve_logging.update_saved_search_algorithm_score]]
- [[defaults.load_defaults]]
- [[formatters.format_evaluator_context]]
- [[gepa_backend.run]]
- [[prepare.prepare_evaluator]]
- [[prepare.prepare_program]]
- [[registry.setup_search]]
- [[run_discovery._run_with_turn_limit]]
- [[run_discovery._write_progress]]
- [[search_strategy_evaluator.evaluate]]
- [[search_strategy_evaluator.evaluate_batch]]
- [[shinkaevolve_backend.run]]
- [[variation_operator_generator.get_available_packages]]
- [[variation_operator_generator.load_config]]
- [[variation_operator_generator.load_evaluator]]
- [[variation_operator_generator.load_initial_program]]
- [[variation_operator_generator.main]]
- [[viewer.load_programs]]
