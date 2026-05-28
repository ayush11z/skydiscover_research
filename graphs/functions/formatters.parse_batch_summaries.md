---
name: formatters.parse_batch_summaries
description: function in skydiscover/context_builder/evox/formatters.py (context-builder)
metadata:
  type: project
---

# formatters.parse_batch_summaries

**File:** `skydiscover/context_builder/evox/formatters.py:603`  
**Kind:** function  
**Layer:** #context-builder

## Source
````python
def parse_batch_summaries(response: str, programs_data: List[Dict]) -> Dict[int, str]:
    """Parse batch summary response into individual summaries by program number."""
    summaries = {}
    if not response or not programs_data:
        return summaries

    for prog in programs_data:
        num = prog["program_num"]
        marker = f"[PROGRAM {num}]"
        if marker in response:
            start_idx = response.find(marker) + len(marker)
            next_idx = len(response)
            for other in programs_data:
                if other["program_num"] != num:
                    other_marker = f"[PROGRAM {other['program_num']}]"
                    if other_marker in response:
                        idx = response.find(other_marker)
                        if start_idx < idx < next_idx:
                            next_idx = idx
            summaries[num] = response[start_idx:next_idx].strip()

    if not summaries and response:
        summaries[programs_data[0]["program_num"]] = response
    return summaries
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[EvoxContextBuilder.build_prompt]]
