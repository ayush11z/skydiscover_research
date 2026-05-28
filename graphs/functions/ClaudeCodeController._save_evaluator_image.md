---
name: ClaudeCodeController._save_evaluator_image
description: method in skydiscover/search/claude_code/controller.py (claude-code)
metadata:
  type: project
---

# ClaudeCodeController._save_evaluator_image

**File:** `skydiscover/search/claude_code/controller.py:84`  
**Kind:** method  
**Layer:** #claude-code

## Source
````python
    def _save_evaluator_image(self, workspace: Path, image_tag: str) -> None:
        tar_path = workspace / ".evaluator-image.tar"
        logger.info(f"Saving evaluator image '{image_tag}' for DinD...")
        subprocess.run(
            ["docker", "save", "-o", str(tar_path), image_tag],
            check=True,
        )
````

## → Calls
- [[Runner.run]]
- [[TaskPool.run]]
- [[gepa_backend.run]]
- [[openevolve_backend.run]]
- [[shinkaevolve_backend.run]]
- [[wrapper.run]]

## ← Called by
- [[ClaudeCodeController.run_discovery]]
