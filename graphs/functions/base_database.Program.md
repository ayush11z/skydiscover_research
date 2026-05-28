---
name: base_database.Program
description: class in skydiscover/search/base_database.py (database)
metadata:
  type: project
---

# base_database.Program

**File:** `skydiscover/search/base_database.py:24`  
**Kind:** class  
**Layer:** #database

## Source
````python
class Program:
    """Represents a program in the database"""

    # Program identification
    id: str
    solution: str
    language: str = "python"

    # Performance
    metrics: Dict[str, Any] = field(default_factory=dict)

    # Tracking information
    iteration_found: int = 0
    parent_id: Optional[str] = None  # Parent program ID it mutates from
    other_context_ids: Optional[List[str]] = (
        None  # other program IDs to provide as context to generate this program
    )
    parent_info: Optional[Tuple[str, str]] = None  # information about the parent program
    context_info: Optional[List[Tuple[str, str]]] = None  # information about the context programs

    timestamp: float = field(default_factory=time.time)

    # Metadata
    metadata: Dict[str, Any] = field(default_factory=dict)
    artifacts: Dict[str, Any] = field(default_factory=dict)

    # Prompts
    prompts: Optional[Dict[str, Any]] = None
    generation: int = 0

````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[AdaEvolveContextBuilder._build_search_guidance]]
- [[AdaEvolveContextBuilder._format_current_program]]
- [[AdaEvolveContextBuilder._format_evaluator_feedback]]
- [[AdaEvolveContextBuilder._format_previous_attempts]]
- [[AdaEvolveContextBuilder._format_sibling_context]]
- [[AdaEvolveContextBuilder._identify_improvement_areas]]
- [[AdaEvolveContextBuilder.build_prompt]]
- [[AdaEvolveController._ensure_all_islands_seeded]]
- [[AdaEvolveController._execute_generation]]
- [[AdaEvolveController._process_result]]
- [[AdaEvolveController.run_discovery]]
- [[AdaEvolveDatabase.__init__]]
- [[AdaEvolveDatabase._all_population_programs]]
- [[AdaEvolveDatabase._choose_pareto_representative]]
- [[AdaEvolveDatabase._compute_global_pareto_front]]
- [[AdaEvolveDatabase._get_archive_crowding_distance]]
- [[AdaEvolveDatabase._get_archive_elite_score]]
- [[AdaEvolveDatabase._get_fitness]]
- [[AdaEvolveDatabase._get_multiobjective_proxy_score]]
- [[AdaEvolveDatabase._get_objective_vector]]
- [[AdaEvolveDatabase._get_pareto_representative_sort_key]]
- [[AdaEvolveDatabase._migrate_archives]]
- [[AdaEvolveDatabase._migrate_legacy]]
- [[AdaEvolveDatabase._sample_from_archive]]
- [[AdaEvolveDatabase._sample_global_top]]
- [[AdaEvolveDatabase._sample_legacy]]
- [[AdaEvolveDatabase._sample_pareto_front]]
- [[AdaEvolveDatabase._sample_random]]
- [[AdaEvolveDatabase._sample_top]]
- [[AdaEvolveDatabase._sample_weighted]]
- [[AdaEvolveDatabase._seed_new_island]]
- [[AdaEvolveDatabase._update_best_program]]
- [[AdaEvolveDatabase.active_programs]]
- [[AdaEvolveDatabase.add]]
- [[AdaEvolveDatabase.add_merged_program]]
- [[AdaEvolveDatabase.find_merge_candidates]]
- [[AdaEvolveDatabase.get_best_program]]
- [[AdaEvolveDatabase.get_children]]
- [[AdaEvolveDatabase.get_global_pareto_front]]
- [[AdaEvolveDatabase.get_island_population]]
- [[AdaEvolveDatabase.get_pareto_front]]
- [[AdaEvolveDatabase.get_program_proxy_score]]
- [[AdaEvolveDatabase.get_top_programs]]
- [[AdaEvolveDatabase.get_top_programs_for_island]]
- [[AdaEvolveDatabase.sample]]
- [[AdaEvolveDatabase.seed_all_islands]]
- [[BeamSearchDatabase._diverse_selection]]
- [[BeamSearchDatabase._get_program_score]]
- [[BeamSearchDatabase._select_best]]
- [[BeamSearchDatabase._select_diversity_weighted]]
- [[BeamSearchDatabase._select_parent]]
- [[BeamSearchDatabase._select_round_robin]]
- [[BeamSearchDatabase._select_stochastic]]
- [[BeamSearchDatabase._update_beam]]
- [[BeamSearchDatabase.add]]
- [[BeamSearchDatabase.get_beam_programs]]
- [[BeamSearchDatabase.get_unexpanded_beam]]
- [[BeamSearchDatabase.sample]]
- [[BestOfNDatabase.add]]
- [[BestOfNDatabase.sample]]
- [[CheckpointManager._save_program]]
- [[CheckpointManager.load]]
- [[CheckpointManager.save]]
- [[ClaudeCodeController._final_evaluation]]
- [[ClaudeCodeController.run_discovery]]
- [[ClaudeCodeDatabase.add]]
- [[CodeDiversity.distance]]
- [[ContextBuilder.build_prompt]]
- [[DefaultContextBuilder._format_current_program]]
- [[DefaultContextBuilder._format_other_context_programs]]
- [[DefaultContextBuilder._format_previous_attempts]]
- [[DefaultContextBuilder._format_single_context_program]]
- [[DefaultContextBuilder._identify_improvement_areas]]
- [[DefaultContextBuilder.build_prompt]]
- [[DiscoveryController._build_prompt]]
- [[DiscoveryController._create_child_program]]
- [[DiscoveryController._finalize_discovery]]
- [[DiscoveryController._process_iteration_result]]
- [[DiscoveryController._run_discovery_parallel]]
- [[DiscoveryController._run_discovery_sequential]]
- [[DiscoveryController._run_from_scratch_iteration]]
- [[DiscoveryController.run_discovery]]
- [[DiversityStrategy.distance]]
- [[DiversityStrategy.update]]
- [[EvoxContextBuilder.build_prompt]]
- [[GEPANativeContextBuilder._build_search_guidance]]
- [[GEPANativeContextBuilder._format_rejection_history]]
- [[GEPANativeContextBuilder.build_prompt]]
- [[GEPANativeController._attempt_merge]]
- [[GEPANativeController._build_merge_prompt]]
- [[GEPANativeController._build_prompt]]
- [[GEPANativeController.run_discovery]]
- [[GEPANativeDatabase._select_other_context_programs]]
- [[GEPANativeDatabase._select_parent]]
- [[GEPANativeDatabase._select_parent_pareto]]
- [[GEPANativeDatabase.add]]
- [[GEPANativeDatabase.add_rejected]]
- [[GEPANativeDatabase.get_merge_candidates]]
- [[GEPANativeDatabase.get_rejection_history]]
- [[GEPANativeDatabase.sample]]
- [[HybridDiversity.distance]]
- [[HybridDiversity.update]]
- [[MetricDiversity._compute_fallback_distance]]
- [[MetricDiversity.distance]]
- [[MetricDiversity.update]]
- [[OpenEvolveNativeDatabase._calculate_feature_coords]]
- [[OpenEvolveNativeDatabase._enforce_population_limit]]
- [[OpenEvolveNativeDatabase._get_cached_diversity]]
- [[OpenEvolveNativeDatabase._is_better]]
- [[OpenEvolveNativeDatabase._migrate_programs]]
- [[OpenEvolveNativeDatabase._sample_exploitation_parent]]
- [[OpenEvolveNativeDatabase._sample_exploration_parent]]
- [[OpenEvolveNativeDatabase._sample_other_context_programs]]
- [[OpenEvolveNativeDatabase._sample_parent]]
- [[OpenEvolveNativeDatabase._sample_random_parent]]
- [[OpenEvolveNativeDatabase._seed_empty_island]]
- [[OpenEvolveNativeDatabase._update_archive]]
- [[OpenEvolveNativeDatabase._update_best_program]]
- [[OpenEvolveNativeDatabase._update_diversity_reference_set]]
- [[OpenEvolveNativeDatabase._update_island_best_program]]
- [[OpenEvolveNativeDatabase.add]]
- [[OpenEvolveNativeDatabase.sample]]
- [[ProgramDatabase.__init__]]
- [[ProgramDatabase._is_better]]
- [[ProgramDatabase._save_program]]
- [[ProgramDatabase._update_best_program]]
- [[ProgramDatabase.add]]
- [[ProgramDatabase.get]]
- [[ProgramDatabase.get_best_program]]
- [[ProgramDatabase.get_top_programs]]
- [[ProgramDatabase.sample]]
- [[Runner._get_best_program]]
- [[Runner._save_best_program]]
- [[Runner.run]]
- [[TopKDatabase.add]]
- [[TopKDatabase.sample]]
- [[UnifiedArchive.__init__]]
- [[UnifiedArchive._compute_elite_score]]
- [[UnifiedArchive._compute_elite_score_for_new]]
- [[UnifiedArchive._compute_novelty]]
- [[UnifiedArchive._compute_pareto_ranking]]
- [[UnifiedArchive._find_eviction_candidate]]
- [[UnifiedArchive._get_fitness]]
- [[UnifiedArchive._get_objective_vector]]
- [[UnifiedArchive._insert]]
- [[UnifiedArchive._track_genealogy]]
- [[UnifiedArchive._track_merged_genealogy]]
- [[UnifiedArchive.add]]
- [[UnifiedArchive.add_merged_program]]
- [[UnifiedArchive.find_merge_candidates]]
- [[UnifiedArchive.get]]
- [[UnifiedArchive.get_all]]
- [[UnifiedArchive.get_best]]
- [[UnifiedArchive.get_children]]
- [[UnifiedArchive.get_parents]]
- [[UnifiedArchive.get_pareto_front]]
- [[UnifiedArchive.get_top_programs]]
- [[UnifiedArchive.sample_other_context_programs]]
- [[UnifiedArchive.sample_parent]]
- [[_make_gepa_evaluator.gepa_evaluator]]
- [[api.DiscoveryResult]]
- [[discovery_utils.build_image_content]]
- [[discovery_utils.load_database_from_file]]
- [[formatters.format_current_program]]
- [[formatters.format_search_algorithms]]
- [[formatters.format_single_program_section]]
- [[formatters.identify_search_improvement_areas]]
- [[formatters.prepare_search_algorithms_data]]
- [[gepa_backend.run]]
- [[get_top_programs._metric_key]]
- [[initial_search_strategy.EvolvedProgram]]
- [[openevolve_backend._to_skydiscover_program]]
- [[registry.get_program]]
- [[registry.register_program]]
- [[search_strategy_db.SearchStrategy]]
- [[search_strategy_evaluator.evaluate]]
- [[shinkaevolve_backend._to_skydiscover_program]]
