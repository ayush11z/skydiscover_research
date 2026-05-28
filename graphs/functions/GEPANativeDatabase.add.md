---
name: GEPANativeDatabase.add
description: method in skydiscover/search/gepa_native/database.py (gepa)
metadata:
  type: project
---

# GEPANativeDatabase.add

**File:** `skydiscover/search/gepa_native/database.py:75`  
**Kind:** method  
**Layer:** #gepa

## Source
````python
    def add(self, program: Program, iteration: Optional[int] = None, **kwargs: Any) -> str:
        """Add a program to the database and elite pool.

        Inserts into the elite pool (sorted descending by fitness), evicts
        the weakest members if the pool exceeds ``population_size``, and
        updates per-metric best tracking.

        Args:
            program: Program to add.
            iteration: Current iteration number for tracking.

        Returns:
            The program's ID.
        """
        if not self.programs:
            self.initial_program_id = program.id

        self.programs[program.id] = program

        if iteration is not None:
            self.last_iteration = max(self.last_iteration, iteration)

        # Insert into elite pool, keep sorted by score descending
        if program.id not in self.elite_pool:
            self.elite_pool.append(program.id)
        self.elite_pool.sort(
            key=lambda pid: get_score(self.programs[pid].metrics if pid in self.programs else {}),
            reverse=True,
        )

        # Cap at population_size, but pin best and initial programs.
        # Only remove from elite_pool (sampling); keep self.programs as
        # a full archive so parent lookups for reflective prompting work.
        if len(self.elite_pool) > self.population_size:
            pinned = {self.best_program_id, self.initial_program_id, program.id} - {None}
            keep = []
            for pid in self.elite_pool:
                if pid in pinned or len(keep) < self.population_size:
                    keep.append(pid)
            self.elite_pool = keep

        # Update per-metric best tracking
        if program.metrics:
            for metric_name, value in program.metrics.items():
                if not isinstance(value, (int, float)):
                    continue
                current = self.metric_best.get(metric_name)
                if current is None or value > current[1]:
                    self.metric_best[metric_name] = (program.id, value)
                    self.program_at_metric_front[metric_name] = {program.id}
                elif value == current[1]:
                    self.program_at_metric_front[metric_name].add(program.id)

        # Update global best
        self._update_best_program(program)

        # Persist to disk
        if self.config.db_path:
            self._save_program(program)

        logger.debug(
            f"Added program {program.id} to GEPA elite pool " f"(pool size: {len(self.elite_pool)})"
        )
        return program.id
````

## → Calls
- [[CheckpointManager._save_program]]
- [[CheckpointManager.load]]
- [[DiscoveryControllerInput.config]]
- [[EvaluationResult.metrics]]
- [[GEPANativeDatabase.__init__]]
- [[Program.id]]
- [[Program.metrics]]
- [[ProgramDatabase._save_program]]
- [[ProgramDatabase._update_best_program]]
- [[base_database.Program]]
- [[base_database.ProgramDatabase]]
- [[metrics.get_score]]

## ← Called by
_(entry point — nothing in this graph calls it)_
