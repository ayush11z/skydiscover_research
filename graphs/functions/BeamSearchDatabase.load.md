---
name: BeamSearchDatabase.load
description: method in skydiscover/search/beam_search/database.py (beam-search)
metadata:
  type: project
---

# BeamSearchDatabase.load

**File:** `skydiscover/search/beam_search/database.py:574`  
**Kind:** method  
**Layer:** #beam-search

## Source
````python
    def load(self, path: str) -> None:
        """
        Load the database from disk, restoring beam search state.

        Args:
            path: Path to load from
        """
        if not os.path.exists(path):
            logger.warning(f"Database path {path} does not exist, skipping load")
            return

        # Load metadata first
        metadata_path = os.path.join(path, "metadata.json")
        if os.path.exists(metadata_path):
            with open(metadata_path, "r") as f:
                metadata = json.load(f)

            self.best_program_id = metadata.get("best_program_id")
            self.last_iteration = metadata.get("last_iteration", 0)

            # Restore beam search state
            self.beam = set(metadata.get("beam", []))
            self.depth = metadata.get("depth", {})
            self.expanded = set(metadata.get("expanded", []))
            self._rr_index = metadata.get("rr_index", 0)
            saved_stats = metadata.get("stats", {})
            self.stats.update(saved_stats)

            logger.info(
                f"Loaded metadata: last_iteration={self.last_iteration}, "
                f"beam_size={len(self.beam)}"
            )

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
                        self.programs[program.id] = program
                    except Exception as e:
                        logger.warning(f"Error loading program {program_file}: {str(e)}")

        # Validate and reconstruct beam if needed
        self._validate_and_reconstruct_beam()

        logger.info(f"Loaded BeamSearchDatabase with {len(self.programs)} programs from {path}")
        self.log_status()
````

## → Calls
- [[BeamSearchDatabase.__init__]]
- [[BeamSearchDatabase._validate_and_reconstruct_beam]]
- [[BeamSearchDatabase.log_status]]
- [[CheckpointManager.load]]
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]
- [[LangFuseTracer.get]]
- [[Program.from_dict]]
- [[ProgramDatabase.get]]
- [[ProgramDatabase.load]]
- [[UnifiedArchive.get]]
- [[UnifiedArchive.stats]]

## ← Called by
_(entry point — nothing in this graph calls it)_
