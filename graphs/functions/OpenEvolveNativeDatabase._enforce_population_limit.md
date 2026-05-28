---
name: OpenEvolveNativeDatabase._enforce_population_limit
description: method in skydiscover/search/openevolve_native/database.py (openevolve)
metadata:
  type: project
---

# OpenEvolveNativeDatabase._enforce_population_limit

**File:** `skydiscover/search/openevolve_native/database.py:687`  
**Kind:** method  
**Layer:** #openevolve

## Source
````python
    def _enforce_population_limit(self, exclude_program_id: Optional[str] = None) -> None:
        if len(self.programs) <= self.population_size:
            return

        num_to_remove = len(self.programs) - self.population_size
        sorted_progs = sorted(
            self.programs.values(),
            key=lambda p: _get_fitness(p.metrics, self.feature_dimensions),
        )

        protected = {self.best_program_id, exclude_program_id} - {None}
        to_remove: List[Program] = []
        for prog in sorted_progs:
            if len(to_remove) >= num_to_remove:
                break
            if prog.id not in protected:
                to_remove.append(prog)

        for prog in to_remove:
            pid = prog.id
            self.programs.pop(pid, None)

            for imap in self.island_feature_maps:
                for k in [k for k, v in imap.items() if v == pid]:
                    del imap[k]

            for island in self.islands:
                island.discard(pid)

            self.archive.discard(pid)

        self._cleanup_stale_island_bests()
        logger.info(
            "Population limit: removed %d, now %d",
            len(to_remove),
            len(self.programs),
        )
````

## → Calls
- [[CheckpointManager.load]]
- [[EvaluationResult.metrics]]
- [[OpenEvolveNativeDatabase._cleanup_stale_island_bests]]
- [[Program.id]]
- [[Program.metrics]]
- [[base_database.Program]]
- [[database._get_fitness]]

## ← Called by
- [[OpenEvolveNativeDatabase.add]]
