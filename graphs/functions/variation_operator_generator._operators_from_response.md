---
name: variation_operator_generator._operators_from_response
description: function in skydiscover/search/evox/utils/variation_operator_generator.py (evox)
metadata:
  type: project
---

# variation_operator_generator._operators_from_response

**File:** `skydiscover/search/evox/utils/variation_operator_generator.py:471`  
**Kind:** function  
**Layer:** #evox

## Source
````python
def _operators_from_response(combined_response: str) -> Tuple[str, str]:
    """Parse LLM response and build diverge/refine variation operators."""
    explore_examples, refine_examples = _parse_combined_response(combined_response)
    diverge_operator = DIVERGE_TEMPLATE.replace("{GENERATED_EXAMPLES}", explore_examples)
    refine_operator = REFINE_TEMPLATE.replace("{GENERATED_EXAMPLES}", refine_examples)
    return diverge_operator, refine_operator
````

## → Calls
- [[template.DIVERGE_TEMPLATE]]
- [[template.REFINE_TEMPLATE]]
- [[variation_operator_generator._parse_combined_response]]

## ← Called by
- [[variation_operator_generator.generate_variation_operators]]
