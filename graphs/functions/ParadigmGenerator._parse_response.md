---
name: ParadigmGenerator._parse_response
description: method in skydiscover/search/adaevolve/paradigm/generator.py (adaevolve)
metadata:
  type: project
---

# ParadigmGenerator._parse_response

**File:** `skydiscover/search/adaevolve/paradigm/generator.py:783`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _parse_response(self, response: str) -> List[Dict[str, Any]]:
        """
        Parse LLM response to extract paradigms.

        Args:
            response: Raw LLM response

        Returns:
            List of validated paradigm dicts
        """
        # Extract JSON from markdown code blocks if present
        text = response.strip()
        if "```json" in text:
            text = text.split("```json")[1].split("```")[0].strip()
        elif "```" in text:
            # Try to find JSON array in any code block
            parts = text.split("```")
            for part in parts[1::2]:  # Odd indices are inside code blocks
                part = part.strip()
                if part.startswith("["):
                    text = part
                    break

        try:
            paradigms = json.loads(text)
        except json.JSONDecodeError as e:
            logger.warning(f"Failed to parse paradigm JSON: {e}")
            logger.debug(f"Response text: {text[:500]}")
            return []

        if not isinstance(paradigms, list):
            logger.warning(f"Expected list, got {type(paradigms)}")
            return []

        # Validate each paradigm
        validated = []
        required_keys = ["idea", "description", "approach_type"]

        for p in paradigms:
            if not isinstance(p, dict):
                continue

            # Check required keys
            if not all(k in p for k in required_keys):
                logger.debug(f"Paradigm missing required keys: {p}")
                continue

            # Ensure all expected keys exist with defaults
            validated.append(
                {
                    "idea": p.get("idea", ""),
                    "description": p.get("description", ""),
                    "what_to_optimize": p.get("what_to_optimize", "score"),
                    "cautions": p.get("cautions", ""),
                    "approach_type": p.get("approach_type", "unknown"),
                }
            )

        return validated
````

## → Calls
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[SearchConfig.type]]
- [[UnifiedArchive.get]]

## ← Called by
- [[ParadigmGenerator.generate]]
