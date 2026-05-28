---
name: ClaudeCodeController._build_docker_cmd
description: staticmethod in skydiscover/search/claude_code/controller.py (claude-code)
metadata:
  type: project
---

# ClaudeCodeController._build_docker_cmd

**File:** `skydiscover/search/claude_code/controller.py:499`  
**Kind:** staticmethod  
**Layer:** #claude-code

## Source
````python
    def _build_docker_cmd(
        image_name: str,
        container_name: str,
        workspace: Path,
        api_key: str,
        is_docker_eval: bool,
    ) -> list:
        if is_docker_eval:
            return [
                "docker",
                "run",
                "--rm",
                "--name",
                container_name,
                "--privileged",
                "-e",
                "DIND=1",
                "-e",
                f"ANTHROPIC_API_KEY={api_key}",
                "-v",
                f"{workspace}:/workspace",
                "-w",
                "/workspace",
                image_name,
                "/workspace/.run.sh",
            ]
        return [
            "docker",
            "run",
            "--rm",
            "--name",
            container_name,
            "--user",
            f"{os.getuid()}:{os.getgid()}",
            "-e",
            "HOME=/workspace",
            "-e",
            f"ANTHROPIC_API_KEY={api_key}",
            "-v",
            f"{workspace}:/workspace",
            "-w",
            "/workspace",
            "--entrypoint",
            "bash",
            image_name,
            "/workspace/.run.sh",
        ]
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[ClaudeCodeController.run_discovery]]
- [[run_discovery._run_with_turn_limit]]
