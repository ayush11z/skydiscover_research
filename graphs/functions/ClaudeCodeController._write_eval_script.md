---
name: ClaudeCodeController._write_eval_script
description: method in skydiscover/search/claude_code/controller.py (claude-code)
metadata:
  type: project
---

# ClaudeCodeController._write_eval_script

**File:** `skydiscover/search/claude_code/controller.py:92`  
**Kind:** method  
**Layer:** #claude-code

## Source
````python
    def _write_eval_script(self, workspace: Path, eval_type: str, timeout: int = 360) -> None:
        """Write run_eval.sh that Claude Code calls to score a candidate."""
        if eval_type == "python":
            script = (
                "#!/bin/bash\nset -euo pipefail\n"
                f"timeout {timeout} python3 - \"$1\" <<'PYEOF'\n"
                "import sys, json\n"
                "sys.path.insert(0, '/workspace')\n"
                "import evaluator\n"
                "result = evaluator.evaluate(sys.argv[1])\n"
                "print(json.dumps(result))\n"
                "PYEOF\n"
            )
        else:
            script = (
                "#!/bin/bash\n"
                "set -euo pipefail\n"
                'PROGRAM_PATH="$1"\n'
                'MODE="${2:-train}"\n'
                'EXT="${PROGRAM_PATH##*.}"\n'
                "CID=$(cat /workspace/.evaluator-container-id)\n"
                'CANDIDATE="/tmp/candidate_$$.${EXT}"\n'
                'docker exec -i "$CID" tee "$CANDIDATE" < "$PROGRAM_PATH" > /dev/null\n'
                f'timeout {timeout} docker exec "$CID" /benchmark/evaluate.sh "$CANDIDATE" "$MODE"\n'
                'docker exec "$CID" rm -f "$CANDIDATE"\n'
            )
        path = workspace / "run_eval.sh"
        path.write_text(script)
        path.chmod(0o755)
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[ClaudeCodeController.run_discovery]]
