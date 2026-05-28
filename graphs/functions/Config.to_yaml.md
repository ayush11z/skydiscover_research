---
name: Config.to_yaml
description: method in skydiscover/config.py (config)
metadata:
  type: project
---

# Config.to_yaml

**File:** `skydiscover/config.py:654`  
**Kind:** method  
**Layer:** #config

## Source
````python
    def to_yaml(self, path: Union[str, Path]) -> None:
        """Save configuration to a YAML file"""
        with open(path, "w") as f:
            yaml.dump(self.to_dict(), f, default_flow_style=False)
````

## → Calls
- [[Config.to_dict]]
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]

## ← Called by
_(entry point — nothing in this graph calls it)_
