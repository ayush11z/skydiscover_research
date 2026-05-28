---
name: OpenEvolveNativeDatabase._sample_other_context_programs
description: method in skydiscover/search/openevolve_native/database.py (openevolve)
metadata:
  type: project
---

# OpenEvolveNativeDatabase._sample_other_context_programs

**File:** `skydiscover/search/openevolve_native/database.py:367`  
**Kind:** method  
**Layer:** #openevolve

## Source
````python
    def _sample_other_context_programs(self, parent: Program, n: int = 4) -> List[Program]:
        """Sample other context programs from parent's island.

        Strategy (matching OpenEvolve):
          1. Island best (if different from parent)
          2. Top elite programs from island
          3. Programs from nearby MAP-Elites cells (±2 perturbation)
          4. Random fill from island
        """
        parent_island = parent.metadata.get("island", self.current_island)
        island_program_ids = list(self.islands[parent_island])
        island_programs = [self.programs[pid] for pid in island_program_ids if pid in self.programs]

        if not island_programs:
            return []

        other_context_programs: List[Program] = []
        used_ids: set = {parent.id}

        # 1. Island best
        island_best_id = self.island_best_programs[parent_island]
        if (
            island_best_id is not None
            and island_best_id != parent.id
            and island_best_id in self.programs
        ):
            other_context_programs.append(self.programs[island_best_id])
            used_ids.add(island_best_id)
        elif island_best_id is not None and island_best_id not in self.programs:
            self.island_best_programs[parent_island] = None

        # 2. Top elite programs from island
        top_n = max(1, int(n * self.elite_selection_ratio))
        top_island = sorted(
            island_programs,
            key=lambda p: _get_fitness(p.metrics, self.feature_dimensions),
            reverse=True,
        )[:top_n]
        for prog in top_island:
            if prog.id not in used_ids:
                other_context_programs.append(prog)
                used_ids.add(prog.id)

        # 3. Nearby MAP-Elites cells (±2 perturbation)
        if len(island_programs) > n and len(other_context_programs) < n:
            remaining_slots = n - len(other_context_programs)
            feature_coords = self._calculate_feature_coords(parent)

            # Build local feature-cell → program mapping for this island
            cell_map: Dict[str, str] = {}
            for pid in island_program_ids:
                if pid in self.programs:
                    coords = self._calculate_feature_coords(self.programs[pid])
                    cell_map[self._feature_coords_to_key(coords)] = pid

            nearby: List[Program] = []
            for _ in range(remaining_slots * 3):
                perturbed = [
                    max(0, min(self.feature_bins - 1, c + random.randint(-2, 2)))
                    for c in feature_coords
                ]
                key = self._feature_coords_to_key(perturbed)
                if key in cell_map:
                    pid = cell_map[key]
                    if (
                        pid not in used_ids
                        and pid not in {p.id for p in nearby}
                        and pid in self.programs
                    ):
                        nearby.append(self.programs[pid])
                        if len(nearby) >= remaining_slots:
                            break

            # 4. Random fill from island
            if len(other_context_programs) + len(nearby) < n:
                remaining = n - len(other_context_programs) - len(nearby)
                all_used = used_ids | {p.id for p in nearby}
                available = [
                    pid
                    for pid in island_program_ids
                    if pid not in all_used and pid in self.programs
                ]
                if available:
                    sampled = random.sample(available, min(remaining, len(available)))
                    nearby.extend(self.programs[pid] for pid in sampled)

            other_context_programs.extend(nearby)

        return other_context_programs[:n]
````

## → Calls
- [[CheckpointManager.load]]
- [[EvaluationResult.metrics]]
- [[LangFuseTracer.get]]
- [[OpenEvolveNativeDatabase._calculate_feature_coords]]
- [[OpenEvolveNativeDatabase._feature_coords_to_key]]
- [[Program.id]]
- [[Program.metadata]]
- [[Program.metrics]]
- [[ProgramDatabase.get]]
- [[ProgramDatabase.sample]]
- [[UnifiedArchive.get]]
- [[base_database.Program]]
- [[database._get_fitness]]

## ← Called by
- [[OpenEvolveNativeDatabase.sample]]
