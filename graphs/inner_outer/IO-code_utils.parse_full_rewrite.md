---
name: IO-code_utils.parse_full_rewrite
description: function in skydiscover/utils/code_utils.py (utils)
metadata:
  type: project
---

# code_utils.parse_full_rewrite

**File:** `skydiscover/utils/code_utils.py:59`  
**Kind:** function  
**Layer:** #utils

## Source
````python
def parse_full_rewrite(llm_response: str, language: str = "python") -> Optional[str]:
    """
    Extract a full rewrite from an LLM response

    Args:
        llm_response: Response from the LLM
        language: Programming language

    Returns:
        Extracted code or None if not found
    """
    solution_block_pattern = r"```" + language + r"\n(.*?)```"
    matches = re.findall(solution_block_pattern, llm_response, re.DOTALL)

    if matches:
        return matches[0].strip()

    # Fallback to any solution block
    solution_block_pattern = r"```(.*?)```"
    matches = re.findall(solution_block_pattern, llm_response, re.DOTALL)

    if matches:
        return matches[0].strip()

    # Fallback to plain text
    return llm_response
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-DiscoveryController._parse_llm_response]]
- [[IO-DiscoveryController._run_from_scratch_iteration]]
