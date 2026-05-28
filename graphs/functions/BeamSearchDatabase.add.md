---
name: BeamSearchDatabase.add
description: method in skydiscover/search/beam_search/database.py (beam-search)
metadata:
  type: project
---

# BeamSearchDatabase.add

**File:** `skydiscover/search/beam_search/database.py:84`  
**Kind:** method  
**Layer:** #beam-search

## Source
````python
    def add(self, program: Program, iteration: Optional[int] = None, **kwargs) -> str:
        """
        Add a program to the database and update the beam.

        The beam is updated to always contain the top beam_width programs,
        considering both fitness scores and optionally diversity.

        Args:
            program: Program to add
            iteration: Current iteration (for tracking)

        Returns:
            Program ID
        """
        # Store the program
        self.programs[program.id] = program

        # Track iteration
        if iteration is not None:
            self.last_iteration = max(self.last_iteration, iteration)

        # Calculate depth from parent
        if program.parent_id and program.parent_id in self.depth:
            self.depth[program.id] = self.depth[program.parent_id] + 1
        else:
            self.depth[program.id] = 0

        # Update max depth statistic
        self.stats["max_depth_reached"] = max(
            self.stats["max_depth_reached"], self.depth[program.id]
        )

        # Update the beam
        self._update_beam(program)

        # Update best program tracking (from base class)
        self._update_best_program(program)

        # Save to disk if configured
        if self.config.db_path:
            self._save_program(program)

        logger.debug(
            f"Added program {program.id} at depth {self.depth[program.id]}, "
            f"beam size: {len(self.beam)}"
        )

        return program.id
````

## → Calls
- [[BeamSearchDatabase._update_beam]]
- [[CheckpointManager._save_program]]
- [[DiscoveryControllerInput.config]]
- [[LangFuseTracer.get]]
- [[Program.id]]
- [[Program.parent_id]]
- [[ProgramDatabase._save_program]]
- [[ProgramDatabase._update_best_program]]
- [[ProgramDatabase.get]]
- [[SerializableResult.parent_id]]
- [[UnifiedArchive.get]]
- [[UnifiedArchive.stats]]
- [[base_database.Program]]
- [[base_database.ProgramDatabase]]

## ← Called by
_(entry point — nothing in this graph calls it)_
