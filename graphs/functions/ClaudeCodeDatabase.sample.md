---
name: ClaudeCodeDatabase.sample
description: method in skydiscover/search/claude_code/database.py (claude-code)
metadata:
  type: project
---

# ClaudeCodeDatabase.sample

**File:** `skydiscover/search/claude_code/database.py:20`  
**Kind:** method  
**Layer:** #claude-code

## Source
````python
    def sample(self, num_context_programs=4, **kwargs):
        best = self.get_best_program()
        return best, []
````

## → Calls
- [[ProgramDatabase.get_best_program]]

## ← Called by
_(entry point — nothing in this graph calls it)_
