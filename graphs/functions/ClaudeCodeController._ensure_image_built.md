---
name: ClaudeCodeController._ensure_image_built
description: method in skydiscover/search/claude_code/controller.py (claude-code)
metadata:
  type: project
---

# ClaudeCodeController._ensure_image_built

**File:** `skydiscover/search/claude_code/controller.py:72`  
**Kind:** method  
**Layer:** #claude-code

## Source
````python
    def _ensure_image_built(self, image_name: str) -> None:
        result = subprocess.run(
            ["docker", "image", "inspect", image_name],
            capture_output=True,
        )
        if result.returncode != 0:
            logger.info(f"Building Claude Code runner image '{image_name}'...")
            subprocess.run(
                ["docker", "build", "-t", image_name, str(_RUNNER_IMAGE_DIR)],
                check=True,
            )
````

## → Calls
- [[Runner.run]]
- [[TaskPool.run]]
- [[controller._RUNNER_IMAGE_DIR]]
- [[gepa_backend.run]]
- [[openevolve_backend.run]]
- [[shinkaevolve_backend.run]]
- [[wrapper.run]]

## ← Called by
- [[ClaudeCodeController.run_discovery]]
