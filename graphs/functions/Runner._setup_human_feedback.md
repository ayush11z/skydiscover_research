---
name: Runner._setup_human_feedback
description: method in skydiscover/runner.py (runner)
metadata:
  type: project
---

# Runner._setup_human_feedback

**File:** `skydiscover/runner.py:317`  
**Kind:** method  
**Layer:** #runner

## Source
````python
    def _setup_human_feedback(self, monitor_server) -> None:
        if not (self.config.human_feedback_enabled or monitor_server):
            return
        try:
            from skydiscover.context_builder import HumanFeedbackReader

            path = self.config.human_feedback_file or os.path.join(
                self.output_dir, "human_feedback.md"
            )
            mode = getattr(self.config, "human_feedback_mode", "append")
            reader = HumanFeedbackReader(path, mode=mode)
            self.discovery_controller.feedback_reader = reader
            if monitor_server:
                monitor_server.set_feedback_reader(reader)
            logger.info(f"Human feedback: {path}")
        except Exception as e:
            logger.warning(f"Failed to set up human feedback: {e}")
````

## → Calls
- [[DiscoveryControllerInput.config]]
- [[DiscoveryControllerInput.output_dir]]
- [[DiscoveryResult.output_dir]]
- [[MonitorServer.set_feedback_reader]]
- [[Runner.run]]
- [[SearchConfig.output_dir]]
- [[human_feedback.HumanFeedbackReader]]

## ← Called by
- [[Runner.run]]
