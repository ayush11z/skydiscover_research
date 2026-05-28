---
name: IO-CoEvolutionController._assign_labels_to_db
description: method in skydiscover/search/evox/controller.py (outer-loop)
metadata:
  type: project
---

# CoEvolutionController._assign_labels_to_db

**File:** `skydiscover/search/evox/controller.py:342`  
**Kind:** method  
**Layer:** #outer-loop

## Source
````python
    def _assign_labels_to_db(self, db) -> None:
        """Assign the variation operators to a database instance."""
        db.DIVERGE_LABEL = self._diverge_label
        db.REFINE_LABEL = self._refine_label
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[IO-CoEvolutionController._generate_variation_operators]]
- [[IO-CoEvolutionController._switch_to_new_search_algorithm]]
