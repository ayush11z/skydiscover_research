---
name: IO-code_utils.extract_diffs
description: function in skydiscover/utils/code_utils.py (utils)
metadata:
  type: project
---

# code_utils.extract_diffs

**File:** `skydiscover/utils/code_utils.py:44`  
**Kind:** function  
**Layer:** #utils

## Source
````python
def extract_diffs(diff_text: str) -> List[Tuple[str, str]]:
    """
    Extract diff blocks from the diff text

    Args:
        diff_text: Diff in the SEARCH/REPLACE format

    Returns:
        List of tuples (search_text, replace_text)
    """
    diff_pattern = r"<<<<<<< SEARCH\n(.*?)=======\n(.*?)>>>>>>> REPLACE"
    diff_blocks = re.findall(diff_pattern, diff_text, re.DOTALL)
    return [(match[0].rstrip(), match[1].rstrip()) for match in diff_blocks]
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-DiscoveryController._parse_llm_response]]
- [[IO-code_utils.apply_diff]]
