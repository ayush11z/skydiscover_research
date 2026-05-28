---
name: ClaudeCodeController.__init__
description: method in skydiscover/search/claude_code/controller.py (claude-code)
metadata:
  type: project
---

# ClaudeCodeController.__init__

**File:** `skydiscover/search/claude_code/controller.py:49`  
**Kind:** method  
**Layer:** #claude-code

## Source
````python
    def __init__(self, controller_input: DiscoveryControllerInput):
        self.config = controller_input.config
        self.evaluation_file = controller_input.evaluation_file
        self.database = controller_input.database
        self.file_suffix = controller_input.file_suffix
        self.output_dir = controller_input.output_dir

        self.config.evaluator.evaluation_file = self.evaluation_file
        self.config.evaluator.file_suffix = self.file_suffix
        self.config.evaluator.is_image_mode = self.config.language == "image"

        self.evaluator = create_evaluator(self.config.evaluator)
        self._inject_evaluator_context()

        self.monitor_callback = None
        self.feedback_reader = None
        self.early_stopping_triggered = False
        self.shutdown_event = mp.Event()
````

## → Calls
- [[Config.evaluator]]
- [[Config.language]]
- [[DiscoveryController._inject_evaluator_context]]
- [[DiscoveryControllerInput.config]]
- [[DiscoveryControllerInput.database]]
- [[DiscoveryControllerInput.evaluation_file]]
- [[DiscoveryControllerInput.output_dir]]
- [[DiscoveryResult.output_dir]]
- [[EvaluatorConfig.evaluation_file]]
- [[EvaluatorConfig.file_suffix]]
- [[EvoxDatabaseConfig.evaluation_file]]
- [[Program.language]]
- [[SearchConfig.database]]
- [[SearchConfig.output_dir]]
- [[default_discovery_controller.DiscoveryControllerInput]]
- [[evaluation.create_evaluator]]

## ← Called by
_(entry point — nothing in this graph calls it)_
