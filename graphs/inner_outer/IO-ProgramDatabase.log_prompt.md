---
name: IO-ProgramDatabase.log_prompt
description: method in skydiscover/search/base_database.py (database)
metadata:
  type: project
---

# ProgramDatabase.log_prompt

**File:** `skydiscover/search/base_database.py:302`  
**Kind:** method  
**Layer:** #database

## Source
````python
    def log_prompt(
        self,
        program_id: str,
        template_key: str,
        prompt: Dict[str, str],
        responses: Optional[List[str]] = None,
    ) -> None:
        """
        Log a prompt for a program.
        Only logs if self.config.log_prompts is True.

        Args:
        program_id: ID of the program to log the prompt for
        template_key: Key for the prompt template
        prompt: Prompts in the format {template_key: { 'system': str, 'user': str }}.
        responses: Optional list of responses to the prompt, if available.
        """

        if not self.config.log_prompts:
            return

        if responses is None:
            responses = []
        prompt["responses"] = responses

        if self.prompts_by_program is None:
            self.prompts_by_program = {}

        if program_id not in self.prompts_by_program:
            self.prompts_by_program[program_id] = {}
        self.prompts_by_program[program_id][template_key] = prompt
````

## → Calls
- [[IO-ProgramDatabase.__init__]]

## ← Called by
- [[IO-DiscoveryController._process_iteration_result]]
