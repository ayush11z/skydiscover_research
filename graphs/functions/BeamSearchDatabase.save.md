---
name: BeamSearchDatabase.save
description: method in skydiscover/search/beam_search/database.py (beam-search)
metadata:
  type: project
---

# BeamSearchDatabase.save

**File:** `skydiscover/search/beam_search/database.py:527`  
**Kind:** method  
**Layer:** #beam-search

## Source
````python
    def save(self, path: Optional[str] = None, iteration: int = 0) -> None:
        """
        Save the database to disk, including beam search state.

        Args:
            path: Path to save to (uses config.db_path if None)
            iteration: Current iteration number
        """
        save_path = path or self.config.db_path
        if not save_path:
            logger.warning("No database path specified, skipping save")
            return

        # Create directory if it doesn't exist
        os.makedirs(save_path, exist_ok=True)

        # Save each program
        for program in self.programs.values():
            prompts = None
            if (
                self.config.log_prompts
                and self.prompts_by_program
                and program.id in self.prompts_by_program
            ):
                prompts = self.prompts_by_program[program.id]
            self._save_program(program, save_path, prompts=prompts)

        # Save metadata including beam search state
        metadata = {
            "best_program_id": self.best_program_id,
            "last_iteration": iteration if iteration is not None else self.last_iteration,
            # Beam search specific state
            "beam": list(self.beam),
            "depth": self.depth,
            "expanded": list(self.expanded),
            "rr_index": self._rr_index,
            "stats": self.stats,
        }

        with open(os.path.join(save_path, "metadata.json"), "w") as f:
            json.dump(metadata, f, indent=2)

        logger.info(
            f"Saved BeamSearchDatabase with {len(self.programs)} programs, "
            f"beam_size={len(self.beam)} to {save_path}"
        )
````

## → Calls
- [[CheckpointManager._save_program]]
- [[CheckpointManager.load]]
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]
- [[DiscoveryControllerInput.config]]
- [[LangFuseTracer.get]]
- [[Program.id]]
- [[ProgramDatabase._save_program]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]
- [[UnifiedArchive.stats]]
- [[base_database.ProgramDatabase]]

## ← Called by
_(entry point — nothing in this graph calls it)_
