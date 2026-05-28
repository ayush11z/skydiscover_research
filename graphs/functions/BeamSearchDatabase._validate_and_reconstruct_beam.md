---
name: BeamSearchDatabase._validate_and_reconstruct_beam
description: method in skydiscover/search/beam_search/database.py (beam-search)
metadata:
  type: project
---

# BeamSearchDatabase._validate_and_reconstruct_beam

**File:** `skydiscover/search/beam_search/database.py:628`  
**Kind:** method  
**Layer:** #beam-search

## Source
````python
    def _validate_and_reconstruct_beam(self) -> None:
        """
        Validate beam state after loading and reconstruct if necessary.

        This handles cases where:
        - Beam contains IDs that no longer exist in programs
        - Beam is empty but programs exist
        - Depth information is missing for some programs
        """
        # Remove invalid beam entries (programs that don't exist)
        valid_beam = {pid for pid in self.beam if pid in self.programs}
        if len(valid_beam) != len(self.beam):
            removed = len(self.beam) - len(valid_beam)
            logger.warning(f"Removed {removed} invalid entries from beam")
            self.beam = valid_beam

        # Remove invalid expanded entries
        valid_expanded = {pid for pid in self.expanded if pid in self.programs}
        self.expanded = valid_expanded

        # Reconstruct depth for programs missing it
        missing_depth = [pid for pid in self.programs if pid not in self.depth]
        if missing_depth:
            logger.info(f"Reconstructing depth for {len(missing_depth)} programs")
            self._reconstruct_depths()

        # If beam is empty but we have programs, reconstruct beam from top programs
        if not self.beam and self.programs:
            logger.info("Beam is empty, reconstructing from top programs")
            top_programs = self.get_top_programs(self.beam_width)
            self.beam = {p.id for p in top_programs}
            logger.info(f"Reconstructed beam with {len(self.beam)} programs")
````

## → Calls
- [[BeamSearchDatabase._reconstruct_depths]]
- [[CheckpointManager.load]]
- [[LangFuseTracer.get]]
- [[Program.id]]
- [[ProgramDatabase.get]]
- [[ProgramDatabase.get_top_programs]]
- [[UnifiedArchive.get]]
- [[UnifiedArchive.get_top_programs]]

## ← Called by
- [[BeamSearchDatabase.load]]
