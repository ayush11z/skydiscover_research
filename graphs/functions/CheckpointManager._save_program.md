---
name: CheckpointManager._save_program
description: method in skydiscover/search/utils/checkpoint_manager.py (search-utils)
metadata:
  type: project
---

# CheckpointManager._save_program

**File:** `skydiscover/search/utils/checkpoint_manager.py:154`  
**Kind:** method  
**Layer:** #search-utils

## Source
````python
    def _save_program(
        self,
        program: Program,
        base_path: Optional[str] = None,
        prompts: Optional[Dict[str, Dict[str, str]]] = None,
    ) -> None:
        """
        Save a program to disk

        Args:
            program: Program to save
            base_path: Base path to save to (uses config.db_path if None)
            prompts: Optional prompts to save with the program, in the format {template_key: { 'system': str, 'user': str }}
        """
        save_path = base_path or self.config.db_path
        if not save_path:
            return

        # Create programs directory if it doesn't exist
        programs_dir = os.path.join(save_path, "programs")
        os.makedirs(programs_dir, exist_ok=True)

        # Save program
        program_dict = program.to_dict()
        if prompts:
            program_dict["prompts"] = prompts
        program_path = os.path.join(programs_dir, f"{program.id}.json")

        with open(program_path, "w") as f:
            json.dump(program_dict, f, cls=SafeJSONEncoder)
````

## → Calls
- [[AdaptiveState.to_dict]]
- [[CheckpointManager.__init__]]
- [[Config.to_dict]]
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]
- [[DatabaseConfig.db_path]]
- [[EvaluationResult.to_dict]]
- [[ParadigmTracker.to_dict]]
- [[Program.id]]
- [[Program.to_dict]]
- [[base_database.Program]]
- [[checkpoint_manager.SafeJSONEncoder]]

## ← Called by
- [[AdaEvolveDatabase.add]]
- [[AdaEvolveDatabase.add_merged_program]]
- [[BeamSearchDatabase.add]]
- [[BeamSearchDatabase.save]]
- [[BestOfNDatabase.add]]
- [[CheckpointManager.save]]
- [[ClaudeCodeDatabase.add]]
- [[EvolvedProgramDatabase.add]]
- [[GEPANativeDatabase.add]]
- [[OpenEvolveNativeDatabase.add]]
- [[ProgramDatabase._save_program]]
- [[SearchStrategyDatabase.add]]
- [[TopKDatabase.add]]
