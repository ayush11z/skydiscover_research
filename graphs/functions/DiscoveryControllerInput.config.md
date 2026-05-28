---
name: DiscoveryControllerInput.config
description: name in skydiscover/search/default_discovery_controller.py (inner-loop)
metadata:
  type: project
---

# DiscoveryControllerInput.config

**File:** `skydiscover/search/default_discovery_controller.py:43`  
**Kind:** name  
**Layer:** #inner-loop

## Source
_(source not extracted — see file)_

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[AdaEvolveContextBuilder._build_search_guidance]]
- [[AdaEvolveContextBuilder._db_config]]
- [[AdaEvolveContextBuilder._task_objective_text]]
- [[AdaEvolveController.__init__]]
- [[AdaEvolveController._execute_generation]]
- [[AdaEvolveController._generate_child]]
- [[AdaEvolveController._process_result]]
- [[AdaEvolveDatabase._expand_to_island_count]]
- [[AdaEvolveDatabase._spawn_island]]
- [[AdaEvolveDatabase.add]]
- [[AdaEvolveDatabase.add_merged_program]]
- [[AdaEvolveDatabase.load]]
- [[AdaEvolveDatabase.save]]
- [[BeamSearchDatabase.add]]
- [[BeamSearchDatabase.save]]
- [[BestOfNDatabase.add]]
- [[ClaudeCodeController.__init__]]
- [[ClaudeCodeController.run_discovery]]
- [[ClaudeCodeDatabase.add]]
- [[CoEvolutionController._build_search_stats]]
- [[CoEvolutionController._generate_variation_operators]]
- [[CoEvolutionController._init_output_dir]]
- [[CoEvolutionController._init_search_evolution_controller]]
- [[CoEvolutionController._init_search_tracking]]
- [[CoEvolutionController._initialize_first_search_program]]
- [[CoEvolutionController._migrate_to_db]]
- [[CoEvolutionController._switch_to_new_search_algorithm]]
- [[DefaultContextBuilder.build_prompt]]
- [[DiscoveryController.__init__]]
- [[DiscoveryController._init_context_builder]]
- [[DiscoveryController._run_iteration]]
- [[EvolvedProgramDatabase.add]]
- [[EvoxContextBuilder.build_prompt]]
- [[GEPANativeController.__init__]]
- [[GEPANativeController._attempt_merge]]
- [[GEPANativeDatabase.add]]
- [[GEPANativeDatabase.save]]
- [[HarborEvaluator._run_container]]
- [[LLMJudge.evaluate]]
- [[OpenEvolveNativeDatabase.add]]
- [[OpenEvolveNativeDatabase.save]]
- [[Runner.__init__]]
- [[Runner._add_initial_program]]
- [[Runner._save_best_program]]
- [[Runner._setup_human_feedback]]
- [[Runner._setup_logging]]
- [[Runner._setup_monitor_summary]]
- [[Runner._start_monitor]]
- [[Runner.run]]
- [[SearchStrategyDatabase.add]]
- [[TopKDatabase.add]]
- [[UnifiedArchive.__init__]]
- [[UnifiedArchive._compute_elite_score]]
- [[UnifiedArchive._compute_elite_score_for_new]]
- [[UnifiedArchive._compute_novelty]]
- [[UnifiedArchive._compute_pareto_ranking]]
- [[UnifiedArchive._get_fitness]]
- [[UnifiedArchive._get_objective_vector]]
- [[UnifiedArchive._get_protected_ids]]
- [[UnifiedArchive._normalize_metric_value]]
- [[UnifiedArchive.add]]
- [[UnifiedArchive.add_merged_program]]
- [[UnifiedArchive.get_pareto_front]]
- [[UnifiedArchive.stats]]
- [[cli.main_async]]
- [[route.get_discovery_controller]]
