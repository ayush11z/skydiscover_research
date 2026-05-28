---
name: AdaEvolveDatabase._sample_from_archive
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase._sample_from_archive

**File:** `skydiscover/search/adaevolve/database.py:534`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _sample_from_archive(
        self,
        island_idx: int,
        num_context_programs: Optional[int] = 4,
        force_exploration: bool = False,
    ) -> Tuple[Dict[str, Program], Dict[str, List[Program]]]:
        """Sample using the per-island unified archive."""
        archive = self.archives[island_idx]

        if archive.size() == 0:
            raise ValueError(f"Cannot sample: island {island_idx} is empty")

        # Get search intensity: adaptive (G-based) or fixed
        if self.use_adaptive_search:
            intensity = self.adapter.get_search_intensity(island_idx)
        else:
            intensity = self.fixed_intensity

        if force_exploration:
            intensity = self.intensity_max

        # Determine sampling mode based on intensity
        # Formula: exploration=intensity%, exploitation=(1-intensity)*70%, balanced=(1-intensity)*30%
        # Example with intensity=0.4: exploration=40%, exploitation=42%, balanced=18%
        rand = random.random()
        if rand < intensity:
            mode = "exploration"
        elif rand < intensity + (1 - intensity) * 0.7:
            mode = "exploitation"
        else:
            mode = "balanced"

        # Sample parent based on mode
        population = archive.get_all()
        if mode == "exploitation":
            if archive.config.pareto_objectives and archive._pareto_ranks:
                parent = self._sample_pareto_front(archive, population)
            else:
                parent = self._sample_top(population)
        else:
            # exploration and balanced use archive's novelty-aware sampling
            parent = archive.sample_parent(mode)

        # Hybrid context programs: local diversity + global top
        num = num_context_programs or 4
        local_count = max(1, int(num * self.local_context_program_ratio))
        global_count = num - local_count

        # Local: most different from parent (but from top performers - see sample_other_context_programs)
        local_context_programs = archive.sample_other_context_programs(parent, local_count)

        # Global: top performers across all islands (cross-pollination)
        global_context_programs = self._sample_global_top(parent.id, global_count)

        other_context_programs = local_context_programs + global_context_programs

        # Map mode to label for the framework's prompt injection
        explore_label, exploit_label = self._get_mode_labels()
        if mode == "exploration":
            label = explore_label
        elif mode == "exploitation":
            label = exploit_label
        else:
            label = ""

        # Stash mode for controller to read (logging, paradigm, sibling context)
        self._last_sampling_mode = mode

        logger.debug(
            f"Sampled parent {parent.id[:8]} from island {island_idx} "
            f"in {mode} mode (intensity={intensity:.2f})"
        )

        return {label: parent}, {"": other_context_programs}
````

## → Calls
- [[AdaEvolveDatabase._get_mode_labels]]
- [[AdaEvolveDatabase._sample_global_top]]
- [[AdaEvolveDatabase._sample_pareto_front]]
- [[AdaEvolveDatabase._sample_top]]
- [[MultiDimensionalAdapter.get_search_intensity]]
- [[Program.id]]
- [[base_database.Program]]

## ← Called by
- [[AdaEvolveDatabase.sample]]
