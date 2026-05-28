---
name: EvaluationResult.metrics
description: name in skydiscover/evaluation/evaluation_result.py (evaluation)
metadata:
  type: project
---

# EvaluationResult.metrics

**File:** `skydiscover/evaluation/evaluation_result.py:11`  
**Kind:** name  
**Layer:** #evaluation

## Source
_(source not extracted — see file)_

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[AdaEvolveController._ensure_all_islands_seeded]]
- [[AdaEvolveController._execute_generation]]
- [[AdaEvolveController._generate_child]]
- [[AdaEvolveDatabase.get_comprehensive_iteration_stats]]
- [[AdaEvolveDatabase.seed_all_islands]]
- [[BeamSearchDatabase._get_program_score]]
- [[BestOfNDatabase.sample.safe_score]]
- [[ClaudeCodeController.run_discovery]]
- [[CoEvolutionController._get_best_score]]
- [[DiscoveryController._create_child_program]]
- [[DiscoveryController._run_iteration]]
- [[EvaluationResult.to_dict]]
- [[Evaluator._cascade_evaluate]]
- [[Evaluator.evaluate_program]]
- [[EvolvedProgramDatabase.add]]
- [[EvolvedProgramDatabase.sample]]
- [[GEPANativeController._attempt_merge]]
- [[GEPANativeController._build_merge_prompt]]
- [[GEPANativeController.run_discovery]]
- [[GEPANativeDatabase._rebuild_elite_pool]]
- [[GEPANativeDatabase._select_parent_pareto]]
- [[GEPANativeDatabase.add]]
- [[MetricDiversity._compute_fallback_distance]]
- [[MetricDiversity.distance]]
- [[MetricDiversity.update]]
- [[OpenEvolveNativeDatabase._calculate_feature_coords]]
- [[OpenEvolveNativeDatabase._cleanup_stale_island_bests]]
- [[OpenEvolveNativeDatabase._enforce_population_limit]]
- [[OpenEvolveNativeDatabase._is_better]]
- [[OpenEvolveNativeDatabase._log_island_status]]
- [[OpenEvolveNativeDatabase._migrate_programs]]
- [[OpenEvolveNativeDatabase._sample_other_context_programs]]
- [[OpenEvolveNativeDatabase._update_archive]]
- [[OpenEvolveNativeDatabase._update_best_program]]
- [[ProgramDatabase._is_better]]
- [[ProgramDatabase.get_best_program]]
- [[ProgramDatabase.get_statistics]]
- [[ProgramDatabase.get_top_programs]]
- [[ProgramDatabase.log_status]]
- [[Runner._add_initial_program]]
- [[Runner._save_best_program]]
- [[Runner._save_checkpoint]]
- [[Runner.initial_score]]
- [[Runner.run]]
- [[SearchStrategyDatabase.sample.safe_score]]
- [[UnifiedArchive._compute_pareto_ranking]]
- [[UnifiedArchive._get_fitness]]
- [[UnifiedArchive._get_objective_vector]]
- [[callback._push_program_event]]
- [[create_external_callback._callback]]
- [[discovery_utils.build_image_content]]
- [[openevolve_backend._get_initial_score]]
- [[openevolve_backend._to_skydiscover_program]]
- [[search_strategy_evaluator.evaluate]]
