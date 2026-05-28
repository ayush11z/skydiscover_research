---
name: Program.id
description: name in skydiscover/search/base_database.py (database)
metadata:
  type: project
---

# Program.id

**File:** `skydiscover/search/base_database.py:28`  
**Kind:** name  
**Layer:** #database

## Source
_(source not extracted — see file)_

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[AdaEvolveController._execute_generation]]
- [[AdaEvolveController._generate_child]]
- [[AdaEvolveController._process_result]]
- [[AdaEvolveDatabase._compute_global_pareto_front]]
- [[AdaEvolveDatabase._get_archive_crowding_distance]]
- [[AdaEvolveDatabase._get_archive_elite_score]]
- [[AdaEvolveDatabase._get_pareto_representative_sort_key]]
- [[AdaEvolveDatabase._sample_from_archive]]
- [[AdaEvolveDatabase._sample_global_top]]
- [[AdaEvolveDatabase._sample_legacy]]
- [[AdaEvolveDatabase._sample_pareto_front]]
- [[AdaEvolveDatabase._update_best_program]]
- [[AdaEvolveDatabase.add]]
- [[AdaEvolveDatabase.add_merged_program]]
- [[AdaEvolveDatabase.get_best_program]]
- [[AdaEvolveDatabase.get_comprehensive_iteration_stats]]
- [[AdaEvolveDatabase.get_pareto_front]]
- [[AdaEvolveDatabase.get_top_programs]]
- [[BeamSearchDatabase._get_program_score]]
- [[BeamSearchDatabase._update_beam]]
- [[BeamSearchDatabase._validate_and_reconstruct_beam]]
- [[BeamSearchDatabase.add]]
- [[BeamSearchDatabase.sample]]
- [[BeamSearchDatabase.save]]
- [[BestOfNDatabase.add]]
- [[BestOfNDatabase.sample]]
- [[CheckpointManager._save_program]]
- [[CheckpointManager.save]]
- [[ClaudeCodeController.run_discovery]]
- [[ClaudeCodeDatabase.add]]
- [[CoEvolutionController._initialize_first_search_program]]
- [[CoEvolutionController._migrate_to_db]]
- [[CoEvolutionController._restore_fallback_database]]
- [[DiscoveryController._create_child_program]]
- [[DiscoveryController._run_iteration]]
- [[EvolvedProgramDatabase.add]]
- [[EvolvedProgramDatabase.sample]]
- [[GEPANativeController._attempt_merge]]
- [[GEPANativeDatabase.add]]
- [[GEPANativeDatabase.get_merge_candidates]]
- [[GEPANativeDatabase.sample]]
- [[GEPANativeDatabase.save]]
- [[OpenEvolveNativeDatabase._enforce_population_limit]]
- [[OpenEvolveNativeDatabase._reconstruct_islands]]
- [[OpenEvolveNativeDatabase._sample_other_context_programs]]
- [[OpenEvolveNativeDatabase._seed_empty_island]]
- [[OpenEvolveNativeDatabase._update_archive]]
- [[OpenEvolveNativeDatabase._update_best_program]]
- [[OpenEvolveNativeDatabase._update_island_best_program]]
- [[OpenEvolveNativeDatabase.add]]
- [[OpenEvolveNativeDatabase.sample]]
- [[ProgramDatabase._update_best_program]]
- [[ProgramDatabase.get_best_program]]
- [[ProgramDatabase.get_statistics]]
- [[Runner._add_initial_program]]
- [[Runner._push_existing_to_monitor]]
- [[Runner._save_best_program]]
- [[Runner._save_checkpoint]]
- [[Runner.run]]
- [[SearchStrategyDatabase.add]]
- [[SearchStrategyDatabase.sample]]
- [[SearchStrategyDatabase.sample.safe_score]]
- [[TopKDatabase.add]]
- [[UnifiedArchive._compute_elite_score]]
- [[UnifiedArchive._compute_novelty]]
- [[UnifiedArchive._compute_pareto_ranking]]
- [[UnifiedArchive._track_genealogy]]
- [[UnifiedArchive._track_merged_genealogy]]
- [[UnifiedArchive.add]]
- [[UnifiedArchive.add_merged_program]]
- [[UnifiedArchive.sample_other_context_programs]]
- [[callback._push_program_event]]
- [[create_external_callback._callback]]
- [[gepa_backend.run]]
- [[openevolve_backend._to_skydiscover_program]]
- [[shinkaevolve_backend._to_skydiscover_program]]
- [[shinkaevolve_backend.run]]
- [[shinkaevolve_backend.run._poll_programs]]
