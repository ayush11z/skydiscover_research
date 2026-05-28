---
name: Runner._save_checkpoint
description: method in skydiscover/runner.py (runner)
metadata:
  type: project
---

# Runner._save_checkpoint

**File:** `skydiscover/runner.py:396`  
**Kind:** method  
**Layer:** #runner

## Source
````python
    def _save_checkpoint(self, iteration: int) -> None:
        checkpoint_dir = os.path.join(self.output_dir, "checkpoints")
        checkpoint_path = os.path.join(checkpoint_dir, f"checkpoint_{iteration}")
        os.makedirs(checkpoint_path, exist_ok=True)

        self.database.save(checkpoint_path, iteration)

        best = self._get_best_program()
        if best:
            with open(
                os.path.join(checkpoint_path, f"best_program{self.file_extension}"), "w"
            ) as f:
                f.write(best.solution)
            with open(os.path.join(checkpoint_path, "best_program_info.json"), "w") as f:
                from skydiscover.search.utils.checkpoint_manager import SafeJSONEncoder

                json.dump(
                    {
                        "id": best.id,
                        "generation": best.generation,
                        "iteration": best.iteration_found,
                        "current_iteration": iteration,
                        "metrics": best.metrics,
                        "language": best.language,
                        "timestamp": best.timestamp,
                        "saved_at": time.time(),
                    },
                    f,
                    indent=2,
                    cls=SafeJSONEncoder,
                )
            logger.info(f"Checkpoint {iteration}: best={format_metrics(best.metrics)}")

        logger.info(f"Checkpoint saved to {checkpoint_path}")
````

## → Calls
- [[Config.language]]
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]
- [[DiscoveryControllerInput.output_dir]]
- [[DiscoveryResult.output_dir]]
- [[EvaluationResult.metrics]]
- [[Program.generation]]
- [[Program.id]]
- [[Program.iteration_found]]
- [[Program.language]]
- [[Program.metrics]]
- [[Program.solution]]
- [[Program.timestamp]]
- [[Runner._get_best_program]]
- [[SearchConfig.output_dir]]
- [[checkpoint_manager.SafeJSONEncoder]]
- [[metrics.format_metrics]]

## ← Called by
- [[Runner.run]]
- [[run.checkpoint_cb]]
