---
name: CheckpointManager.load
description: method in skydiscover/search/utils/checkpoint_manager.py (search-utils)
metadata:
  type: project
---

# CheckpointManager.load

**File:** `skydiscover/search/utils/checkpoint_manager.py:103`  
**Kind:** method  
**Layer:** #search-utils

## Source
````python
    def load(self, path: str) -> Tuple[Dict[str, Program], Optional[str], int]:
        """
        Load the database from disk

        Args:
            path: Path to load from

        Returns:
            Tuple of (programs_dict, best_program_id, last_iteration)
        """
        # Import here to avoid circular import
        from skydiscover.search.base_database import Program

        programs: Dict[str, Program] = {}
        best_program_id: Optional[str] = None
        last_iteration: int = 0

        if not os.path.exists(path):
            logger.warning(f"Database path {path} does not exist, skipping load")
            return programs, best_program_id, last_iteration

        # Load metadata first
        metadata_path = os.path.join(path, "metadata.json")
        if os.path.exists(metadata_path):
            with open(metadata_path, "r") as f:
                metadata = json.load(f)

            best_program_id = metadata.get("best_program_id")
            last_iteration = metadata.get("last_iteration", 0)

            logger.info(f"Loaded database metadata with last_iteration={last_iteration}")

        # Load programs
        programs_dir = os.path.join(path, "programs")
        if os.path.exists(programs_dir):
            for program_file in os.listdir(programs_dir):
                if program_file.endswith(".json"):
                    program_path = os.path.join(programs_dir, program_file)
                    try:
                        with open(program_path, "r") as f:
                            program_data = json.load(f)

                        program = Program.from_dict(program_data)
                        programs[program.id] = program
                    except Exception as e:
                        logger.warning(f"Error loading program {program_file}: {str(e)}")

        logger.info(f"Loaded database with {len(programs)} programs from {path}")

        return programs, best_program_id, last_iteration
````

## → Calls
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]
- [[LangFuseTracer.get]]
- [[Program.from_dict]]
- [[ProgramDatabase.get]]
- [[ProgramDatabase.load]]
- [[UnifiedArchive.get]]
- [[base_database.Program]]

## ← Called by
- [[AdaEvolveDatabase._all_population_programs]]
- [[AdaEvolveDatabase._distribute_programs_to_islands]]
- [[AdaEvolveDatabase._enforce_island_population_limit]]
- [[AdaEvolveDatabase._should_spawn_island]]
- [[AdaEvolveDatabase.get_best_program]]
- [[AdaEvolveDatabase.get_children]]
- [[AdaEvolveDatabase.get_comprehensive_iteration_stats]]
- [[AdaEvolveDatabase.load]]
- [[AdaEvolveDatabase.save]]
- [[AgenticGenerator._call_llm]]
- [[BeamSearchDatabase._diverse_selection]]
- [[BeamSearchDatabase._prune_beam]]
- [[BeamSearchDatabase._reconstruct_depths]]
- [[BeamSearchDatabase._select_diversity_weighted]]
- [[BeamSearchDatabase._select_parent]]
- [[BeamSearchDatabase._validate_and_reconstruct_beam]]
- [[BeamSearchDatabase.get_beam_programs]]
- [[BeamSearchDatabase.get_search_stats]]
- [[BeamSearchDatabase.get_unexpanded_beam]]
- [[BeamSearchDatabase.load]]
- [[BeamSearchDatabase.save]]
- [[BestOfNDatabase.sample]]
- [[EvolvedProgramDatabase.add]]
- [[EvolvedProgramDatabase.sample]]
- [[GEPANativeDatabase._rebuild_elite_pool]]
- [[GEPANativeDatabase._select_other_context_programs]]
- [[GEPANativeDatabase._select_parent]]
- [[GEPANativeDatabase._select_parent_pareto]]
- [[GEPANativeDatabase.add]]
- [[GEPANativeDatabase.get_merge_candidates]]
- [[GEPANativeDatabase.load]]
- [[GEPANativeDatabase.sample]]
- [[OpenEvolveNativeDatabase._calculate_feature_coords]]
- [[OpenEvolveNativeDatabase._cleanup_stale_island_bests]]
- [[OpenEvolveNativeDatabase._distribute_programs_to_islands]]
- [[OpenEvolveNativeDatabase._enforce_population_limit]]
- [[OpenEvolveNativeDatabase._log_island_status]]
- [[OpenEvolveNativeDatabase._migrate_programs]]
- [[OpenEvolveNativeDatabase._reconstruct_islands]]
- [[OpenEvolveNativeDatabase._sample_exploitation_parent]]
- [[OpenEvolveNativeDatabase._sample_exploration_parent]]
- [[OpenEvolveNativeDatabase._sample_other_context_programs]]
- [[OpenEvolveNativeDatabase._sample_random_parent]]
- [[OpenEvolveNativeDatabase._seed_empty_island]]
- [[OpenEvolveNativeDatabase._update_archive]]
- [[OpenEvolveNativeDatabase._update_best_program]]
- [[OpenEvolveNativeDatabase._update_diversity_reference_set]]
- [[OpenEvolveNativeDatabase._update_island_best_program]]
- [[OpenEvolveNativeDatabase.add]]
- [[OpenEvolveNativeDatabase.load]]
- [[OpenEvolveNativeDatabase.sample]]
- [[ProgramDatabase._update_best_program]]
- [[ProgramDatabase.get]]
- [[ProgramDatabase.get_best_program]]
- [[ProgramDatabase.get_statistics]]
- [[ProgramDatabase.get_top_programs]]
- [[ProgramDatabase.load]]
- [[ProgramDatabase.log_status]]
- [[ProgramDatabase.save]]
- [[SearchStrategyDatabase.sample]]
- [[TopKDatabase.sample]]
- [[coevolve_logging.log_active_algorithm]]
- [[coevolve_logging.log_failed_attempt]]
- [[coevolve_logging.update_saved_search_algorithm_score]]
- [[variation_operator_generator.get_available_packages]]
- [[viewer.load_programs]]
