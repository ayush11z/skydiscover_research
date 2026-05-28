---
name: IO-Runner._save_best_program
description: method in skydiscover/runner.py (runner)
metadata:
  type: project
---

# Runner._save_best_program

**File:** `skydiscover/runner.py:444`  
**Kind:** method  
**Layer:** #runner

## Source
````python
    def _save_best_program(self, program: Program) -> None:
        best_dir = os.path.join(self.output_dir, "best")
        os.makedirs(best_dir, exist_ok=True)

        code_path = os.path.join(best_dir, f"best_program{self.file_extension}")
        with open(code_path, "w") as f:
            f.write(program.solution)

        info_path = os.path.join(best_dir, "best_program_info.json")
        with open(info_path, "w") as f:
            from skydiscover.search.utils.checkpoint_manager import SafeJSONEncoder

            json.dump(
                {
                    "id": program.id,
                    "generation": program.generation,
                    "iteration": program.iteration_found,
                    "timestamp": program.timestamp,
                    "parent_id": program.parent_id,
                    "metrics": program.metrics,
                    "language": program.language,
                    "saved_at": time.time(),
                },
                f,
                indent=2,
                cls=SafeJSONEncoder,
            )

        if self.config.language == "image" and program.metadata:
            img = program.metadata.get("image_path")
            if img and os.path.exists(img):
                import shutil

                shutil.copy2(img, os.path.join(best_dir, "best_image" + os.path.splitext(img)[1]))

        logger.info(f"Best program saved to {best_dir}")
````

## → Calls
- [[IO-DiscoveryControllerInput.config]]
- [[IO-DiscoveryControllerInput.output_dir]]
- [[IO-Program.generation]]
- [[IO-Program.id]]
- [[IO-Program.iteration_found]]
- [[IO-Program.language]]
- [[IO-Program.metadata]]
- [[IO-Program.metrics]]
- [[IO-Program.parent_id]]
- [[IO-Program.solution]]
- [[IO-Program.timestamp]]
- [[IO-base_database.Program]]

## ← Called by
- [[IO-Runner.run]]
