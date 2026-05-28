---
name: AdaEvolveDatabase._sample_legacy
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase._sample_legacy

**File:** `skydiscover/search/adaevolve/database.py:609`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _sample_legacy(
        self,
        island_idx: int,
        num_context_programs: Optional[int] = 4,
        force_exploration: bool = False,
    ) -> Tuple[Dict[str, Program], Dict[str, List[Program]]]:
        """Sample using legacy list-based logic."""
        population = self.islands[island_idx]

        if not population:
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
            parent = self._sample_random(population)
            mode = "exploration"
        elif rand < intensity + (1 - intensity) * 0.7:
            parent = self._sample_top(population)
            mode = "exploitation"
        else:
            parent = self._sample_weighted(population)
            mode = "balanced"

        # Sample context programs from ALL islands (global cross-pollination)
        num = num_context_programs or 4
        other_context_programs = self._sample_global_top(parent.id, num)

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
- [[AdaEvolveDatabase._sample_random]]
- [[AdaEvolveDatabase._sample_top]]
- [[AdaEvolveDatabase._sample_weighted]]
- [[MultiDimensionalAdapter.get_search_intensity]]
- [[Program.id]]
- [[base_database.Program]]

## ← Called by
- [[AdaEvolveDatabase.sample]]
