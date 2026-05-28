---
name: AdaEvolveDatabase.get_comprehensive_iteration_stats
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase.get_comprehensive_iteration_stats

**File:** `skydiscover/search/adaevolve/database.py:927`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def get_comprehensive_iteration_stats(
        self,
        iteration: int,
        sampling_mode: Optional[str] = None,
        sampling_intensity: Optional[float] = None,
    ) -> Dict[str, Any]:
        """
        Get comprehensive statistics for JSON logging at each iteration.

        This method collects ALL AdaEvolve signals for detailed analysis including:
        - Island-level adaptive state (G, intensity, UCB stats)
        - Global evolution state
        - Paradigm breakthrough state
        - Dynamic island spawning state

        Args:
            iteration: Current iteration number
            sampling_mode: The sampling mode used this iteration (exploration/exploitation/balanced)
            sampling_intensity: The search intensity value used this iteration

        Returns:
            Comprehensive dictionary with all AdaEvolve signals
        """
        import math

        # =========================================================================
        # Island-level statistics
        # =========================================================================
        island_stats = []
        for i in range(self.num_islands):
            state = self.adapter.states[i] if i < len(self.adapter.states) else None

            island_data = {
                "island_idx": i,
                "is_current": i == self.current_island,
                "config_name": (
                    self.island_config_names[i] if i < len(self.island_config_names) else "unknown"
                ),
            }

            # Population stats
            if self.use_unified_archive and self.archives and i < len(self.archives):
                archive = self.archives[i]
                island_data["population_size"] = archive.size()
                island_data["top_count"] = len(archive.get_top_programs())
                if hasattr(archive, "stats"):
                    archive_stats = archive.stats()
                    island_data["archive_stats"] = archive_stats
            elif self.islands and i < len(self.islands):
                island_data["population_size"] = len(self.islands[i])
                island_data["top_count"] = 0

            # Adaptive state (G, intensity, etc.)
            if state:
                island_data["accumulated_signal_G"] = state.accumulated_signal
                island_data["best_score"] = (
                    state.best_score if not math.isinf(state.best_score) else None
                )
                island_data["search_intensity"] = state.get_search_intensity()
                island_data["improvement_count"] = state.improvement_count
                island_data["total_evaluations"] = state.total_evaluations
                island_data["productivity"] = state.get_productivity()

                # Hyperparameters
                island_data["decay"] = state.decay
                island_data["intensity_min"] = state.intensity_min
                island_data["intensity_max"] = state.intensity_max

            # UCB stats
            if i < len(self.adapter.dimension_visits):
                island_data["ucb_raw_visits"] = self.adapter.dimension_visits[i]
            if i < len(self.adapter.decayed_visits):
                island_data["ucb_decayed_visits"] = self.adapter.decayed_visits[i]
            if i < len(self.adapter.dimension_rewards):
                island_data["ucb_decayed_rewards"] = self.adapter.dimension_rewards[i]
                dec_visits = (
                    self.adapter.decayed_visits[i] if i < len(self.adapter.decayed_visits) else 0.0
                )
                island_data["ucb_reward_avg"] = (
                    self.adapter.dimension_rewards[i] / dec_visits if dec_visits > 0 else 0.0
                )

            island_stats.append(island_data)

        # =========================================================================
        # Global statistics
        # =========================================================================
        best_program = self.get_best_program()
        pareto_front = self.get_global_pareto_front() if self.is_multiobjective_enabled() else []
        global_stats = {
            "iteration": iteration,
            "num_islands": self.num_islands,
            "current_island_idx": self.current_island,
            "global_best_score": (
                self._global_best_score if not math.isinf(self._global_best_score) else None
            ),
            "global_best_program_id": self.best_program_id,
            "optimization_mode": "pareto" if self.is_multiobjective_enabled() else "scalar",
            "pareto_objectives": list(self.pareto_objectives),
            "higher_is_better": dict(self.higher_is_better),
            "fitness_proxy_key": self.fitness_key,
            "global_pareto_front_size": len(pareto_front),
            "global_pareto_front_ids": [program.id for program in pareto_front],
            "global_productivity": self.adapter.get_global_productivity(),
            "total_programs": len(self.programs),
            # UCB global state
            "ucb_global_best_score": (
                self.adapter.global_best_score
                if not math.isinf(self.adapter.global_best_score)
                else None
            ),
            "ucb_exploration_constant": self.adapter.ucb_exploration,
            "ucb_min_visits": self.adapter.min_visits,
        }

        # Best program details (truncated code for logging)
        if best_program:
            code_preview = (
                best_program.solution[:500] + "..."
                if len(best_program.solution) > 500
                else best_program.solution
            )
            global_stats["best_program"] = {
                "id": best_program.id,
                "metrics": best_program.metrics,
                "generation": best_program.generation,
                "iteration_found": best_program.iteration_found,
                "is_pareto_representative": self.is_multiobjective_enabled(),
                "code_length": len(best_program.solution),
                "code_preview": code_preview,
            }

        # =========================================================================
        # Sampling state (for this iteration)
        # =========================================================================
        sampling_stats = {
            "mode": sampling_mode,
            "intensity_used": sampling_intensity,
            "use_adaptive_search": self.use_adaptive_search,
            "use_ucb_selection": self.use_ucb_selection,
            "fixed_intensity": self.fixed_intensity if not self.use_adaptive_search else None,
        }

        # =========================================================================
        # Paradigm breakthrough state
        # =========================================================================
        paradigm_stats = {
            "enabled": self.use_paradigm_breakthrough,
        }

        if self.use_paradigm_breakthrough and self.paradigm_tracker is not None:
            tracker = self.paradigm_tracker

            paradigm_stats.update(
                {
                    "is_stagnating": tracker.is_paradigm_stagnating(),
                    "has_active_paradigm": tracker.has_active_paradigm(),
                    "improvement_rate": tracker.get_improvement_rate(),
                    "improvement_threshold": tracker.improvement_threshold,
                    "window_size": tracker.window_size,
                    "improvement_history_length": len(tracker.improvement_history),
                    # Active paradigms
                    "num_active_paradigms": len(tracker.active_paradigms),
                    "current_paradigm_index": tracker.current_paradigm_index,
                    "max_paradigm_uses": tracker.max_paradigm_uses,
                    # Count non-exhausted paradigms
                    "num_non_exhausted_paradigms": sum(
                        1
                        for i in range(len(tracker.active_paradigms))
                        if tracker.paradigm_usage_counts.get(i, 0) < tracker.max_paradigm_uses
                    ),
                    # Paradigm usage counts
                    "paradigm_usage_counts": dict(tracker.paradigm_usage_counts),
                    # Current paradigm details
                    "current_paradigm": None,
                    # Previously tried paradigms
                    "num_tried_paradigms": len(tracker.tried_paradigms),
                    "tried_paradigms_summary": [
                        {
                            "idea": p.get("idea", "N/A"),
                            "outcome": p.get("outcome", "UNCLEAR"),
                            "score_improvement": p.get("score_improvement", 0.0),
                            "uses": p.get("uses", 0),
                        }
                        for p in tracker.tried_paradigms[-5:]  # Last 5 tried
                    ],
                    # Score tracking
                    "best_score_at_paradigm_gen": tracker.best_score_at_paradigm_gen,
                    "best_score_during_paradigm": tracker.best_score_during_paradigm,
                }
            )

            # Current paradigm details (if available)
            current = tracker.get_current_paradigm()
            if current:
                paradigm_stats["current_paradigm"] = {
                    "idea": current.get("idea", "N/A"),
                    "description": current.get("description", "N/A"),
                    "approach_type": current.get("approach_type", "N/A"),
                    "what_to_optimize": current.get("what_to_optimize", "N/A"),
                    "cautions": current.get("cautions", "N/A"),
                    "uses_remaining": (
                        tracker.max_paradigm_uses
                        - tracker.paradigm_usage_counts.get(tracker.current_paradigm_index, 0)
                    ),
                }

            # All active paradigms summary
            paradigm_stats["active_paradigms"] = [
                {
                    "index": i,
                    "idea": p.get("idea", "N/A"),
                    "approach_type": p.get("approach_type", "N/A"),
                    "uses": tracker.paradigm_usage_counts.get(i, 0),
                    "exhausted": tracker.paradigm_usage_counts.get(i, 0)
                    >= tracker.max_paradigm_uses,
                }
                for i, p in enumerate(tracker.active_paradigms)
            ]

        # =========================================================================
        # Dynamic island spawning state
        # =========================================================================
        dynamic_island_stats = {
            "enabled": self.use_dynamic_islands,
        }

        if self.use_dynamic_islands:
            dynamic_island_stats.update(
                {
                    "max_islands": self.max_islands,
                    "current_num_islands": self.num_islands,
                    "islands_remaining": self.max_islands - self.num_islands,
                    "last_spawn_iteration": self.last_spawn_iteration,
                    "spawn_cooldown": self.spawn_cooldown,
                    "iterations_since_spawn": iteration - self.last_spawn_iteration,
                    "spawn_productivity_threshold": self.spawn_productivity_threshold,
                    "would_spawn": self._should_spawn_island(),
                }
            )

        # =========================================================================
        # Configuration summary
        # =========================================================================
        config_stats = {
            "decay": self.decay,
            "intensity_min": self.intensity_min,
            "intensity_max": self.intensity_max,
            "population_size": self.population_size,
            "migration_interval": self.migration_interval,
            "migration_count": self.migration_count,
            "use_migration": self.use_migration,
            "use_unified_archive": self.use_unified_archive,
            "local_context_program_ratio": self.local_context_program_ratio,
        }

        # =========================================================================
        # Assemble complete stats
        # =========================================================================
        return {
            "iteration": iteration,
            "timestamp": None,  # Will be filled by controller
            "global": global_stats,
            "islands": island_stats,
            "sampling": sampling_stats,
            "paradigm": paradigm_stats,
            "dynamic_islands": dynamic_island_stats,
            "config": config_stats,
        }
````

## → Calls
- [[AdaEvolveDatabase.__init__]]
- [[AdaEvolveDatabase._should_spawn_island]]
- [[AdaEvolveDatabase.get_best_program]]
- [[AdaEvolveDatabase.get_current_paradigm]]
- [[AdaEvolveDatabase.get_global_pareto_front]]
- [[AdaEvolveDatabase.has_active_paradigm]]
- [[AdaEvolveDatabase.is_multiobjective_enabled]]
- [[AdaEvolveDatabase.is_paradigm_stagnating]]
- [[AdaEvolveDatabaseConfig.higher_is_better]]
- [[AdaEvolveDatabaseConfig.population_size]]
- [[ArchiveConfig.higher_is_better]]
- [[CheckpointManager.load]]
- [[EvaluationResult.metrics]]
- [[GEPANativeDatabaseConfig.population_size]]
- [[LangFuseTracer.get]]
- [[MultiDimensionalAdapter.get_global_productivity]]
- [[MultiDimensionalAdapter.select_dimension_ucb]]
- [[OpenEvolveNativeDatabaseConfig.population_size]]
- [[ParadigmTracker.active_paradigms]]
- [[ParadigmTracker.best_score_at_paradigm_gen]]
- [[ParadigmTracker.best_score_during_paradigm]]
- [[ParadigmTracker.current_paradigm_index]]
- [[ParadigmTracker.get_current_paradigm]]
- [[ParadigmTracker.get_improvement_rate]]
- [[ParadigmTracker.has_active_paradigm]]
- [[ParadigmTracker.improvement_history]]
- [[ParadigmTracker.improvement_threshold]]
- [[ParadigmTracker.is_paradigm_stagnating]]
- [[ParadigmTracker.max_paradigm_uses]]
- [[ParadigmTracker.paradigm_usage_counts]]
- [[ParadigmTracker.tried_paradigms]]
- [[ParadigmTracker.window_size]]
- [[Program.generation]]
- [[Program.id]]
- [[Program.iteration_found]]
- [[Program.metrics]]
- [[Program.solution]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]
- [[adaptation.MultiDimensionalAdapter]]

## ← Called by
_(entry point — nothing in this graph calls it)_
