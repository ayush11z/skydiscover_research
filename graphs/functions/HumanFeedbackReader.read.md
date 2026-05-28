---
name: HumanFeedbackReader.read
description: method in skydiscover/context_builder/human_feedback.py (context-builder)
metadata:
  type: project
---

# HumanFeedbackReader.read

**File:** `skydiscover/context_builder/human_feedback.py:59`  
**Kind:** method  
**Layer:** #context-builder

## Source
````python
    def read(self) -> str:
        """
        Read current feedback, stripping comment lines.
        Returns empty string if file is empty, missing, or only has comments.
        """
        try:
            with open(self.path, "r") as f:
                raw = f.read()
        except (FileNotFoundError, PermissionError):
            return ""

        lines = []
        for line in raw.splitlines():
            stripped = line.strip()
            if stripped and not stripped.startswith("#"):
                lines.append(line)

        content = "\n".join(lines).strip()
        if len(content) > MAX_FEEDBACK_CHARS:
            content = content[:MAX_FEEDBACK_CHARS]

        if content != self._last_content:
            if content:
                logger.info(f"Human feedback updated ({len(content)} chars)")
            elif self._last_content:
                logger.info("Human feedback cleared")
            self._last_content = content

        return content
````

## → Calls
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]

## ← Called by
- [[DiscoveryController._run_from_scratch_iteration]]
- [[DiscoveryController._run_iteration]]
- [[HumanFeedbackReader.apply_feedback]]
- [[MonitorServer._consume_queue]]
- [[MonitorServer._get_feedback_state]]
- [[gepa_backend.run]]
- [[openevolve_backend.run._poll_programs]]
- [[shinkaevolve_backend.run._poll_programs]]
