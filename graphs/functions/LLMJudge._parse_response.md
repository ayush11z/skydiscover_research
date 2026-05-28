---
name: LLMJudge._parse_response
description: method in skydiscover/evaluation/llm_judge.py (evaluation)
metadata:
  type: project
---

# LLMJudge._parse_response

**File:** `skydiscover/evaluation/llm_judge.py:77`  
**Kind:** method  
**Layer:** #evaluation

## Source
````python
    def _parse_response(self, response: str) -> dict:
        """
        Extract a JSON dict from an LLM response.

        Tries a fenced json block first, then the outermost { ... }.
        Numeric values become metrics; everything else becomes artifacts.
        Override for XML, YAML, or structured output formats.
        """
        match = re.search(r"```json\n(.*?)\n```", response, re.DOTALL)
        if match:
            return json.loads(match.group(1))

        start, end = response.find("{"), response.rfind("}") + 1
        if start >= 0 and end > start:
            return json.loads(response[start:end])

        return json.loads(response)
````

## → Calls
- [[Config.search]]

## ← Called by
- [[LLMJudge.evaluate]]
