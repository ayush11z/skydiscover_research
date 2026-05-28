---
name: CodeDiversity._extract_features
description: method in skydiscover/search/adaevolve/archive/diversity.py (adaevolve)
metadata:
  type: project
---

# CodeDiversity._extract_features

**File:** `skydiscover/search/adaevolve/archive/diversity.py:144`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _extract_features(self, solution: str) -> set:
        """Extract structural features from code."""
        import re

        features = set()

        # Import statements (what libraries are used)
        imports = re.findall(r"(?:from\s+(\S+)\s+)?import\s+(\S+)", solution)
        for from_mod, imp in imports:
            if from_mod:
                features.add(f"import:{from_mod}")
            features.add(f"import:{imp.split('.')[0]}")

        # Function definitions
        functions = re.findall(r"def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(", solution)
        for func in functions:
            features.add(f"func:{func}")

        # Class definitions
        classes = re.findall(r"class\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*[:\(]", solution)
        for cls in classes:
            features.add(f"class:{cls}")

        # Key function calls (common libraries)
        calls = re.findall(r"([a-zA-Z_][a-zA-Z0-9_]*(?:\.[a-zA-Z_][a-zA-Z0-9_]*)+)\s*\(", solution)
        for call in calls:
            features.add(f"call:{call}")

        # Control flow patterns
        if "for " in solution:
            features.add("pattern:for_loop")
        if "while " in solution:
            features.add("pattern:while_loop")
        if "try:" in solution or "try :" in solution:
            features.add("pattern:try_except")
        if "with " in solution:
            features.add("pattern:context_manager")
        if "yield " in solution:
            features.add("pattern:generator")
        if "async " in solution or "await " in solution:
            features.add("pattern:async")
        if "lambda " in solution:
            features.add("pattern:lambda")

        return features
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
- [[CodeDiversity._structural_distance]]
