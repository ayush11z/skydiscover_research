---
name: CheckpointManager.save
description: method in skydiscover/search/utils/checkpoint_manager.py (search-utils)
metadata:
  type: project
---

# CheckpointManager.save

**File:** `skydiscover/search/utils/checkpoint_manager.py:59`  
**Kind:** method  
**Layer:** #search-utils

## Source
````python
    def save(
        self,
        programs: Dict[str, Program],
        prompts_by_program: Optional[Dict[str, Dict[str, Dict[str, str]]]],
        best_program_id: Optional[str],
        last_iteration: int,
        path: Optional[str] = None,
    ) -> None:
        """
        Save the database to disk

        Args:
            programs: Dictionary of program ID to Program
            prompts_by_program: Optional prompts by program ID
            best_program_id: ID of the best program
            last_iteration: Last iteration number
            path: Path to save to (uses config.db_path if None)
        """
        save_path = path or self.config.db_path
        if not save_path:
            logger.warning("No database path specified, skipping save")
            return

        # create directory if it doesn't exist
        os.makedirs(save_path, exist_ok=True)

        # Save each program
        for program in programs.values():
            prompts = None
            if self.config.log_prompts and prompts_by_program and program.id in prompts_by_program:
                prompts = prompts_by_program[program.id]
            self._save_program(program, save_path, prompts=prompts)

        # Save metadata
        metadata = {
            "best_program_id": best_program_id,
            "last_iteration": last_iteration,
        }

        with open(os.path.join(save_path, "metadata.json"), "w") as f:
            json.dump(metadata, f)

        logger.info(f"[CHECKPOINT] Saved database with {len(programs)} programs to {save_path}")
````

## → Calls
- [[CheckpointManager.__init__]]
- [[CheckpointManager._save_program]]
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]
- [[DatabaseConfig.db_path]]
- [[DatabaseConfig.log_prompts]]
- [[Program.id]]
- [[base_database.Program]]

## ← Called by
- [[ProgramDatabase.save]]
