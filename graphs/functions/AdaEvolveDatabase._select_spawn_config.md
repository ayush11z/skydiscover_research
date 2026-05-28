---
name: AdaEvolveDatabase._select_spawn_config
description: method in skydiscover/search/adaevolve/database.py (adaevolve)
metadata:
  type: project
---

# AdaEvolveDatabase._select_spawn_config

**File:** `skydiscover/search/adaevolve/database.py:2107`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def _select_spawn_config(self) -> Tuple[str, Dict[str, Any]]:
        """
        Select a configuration preset for a new island.

        Prefers presets that are not yet used or underused.
        """
        usage_counts = {preset["name"]: 0 for preset in ISLAND_CONFIG_PRESETS}
        for name in self.island_config_names:
            if name in usage_counts:
                usage_counts[name] += 1

        min_usage = min(usage_counts.values())
        underused = [
            preset for preset in ISLAND_CONFIG_PRESETS if usage_counts[preset["name"]] == min_usage
        ]

        selected = random.choice(underused)
        return selected["name"], selected
````

## → Calls
- [[LangFuseTracer.get]]
- [[ProgramDatabase.get]]
- [[UnifiedArchive.get]]
- [[database.ISLAND_CONFIG_PRESETS]]

## ← Called by
- [[AdaEvolveDatabase._spawn_island]]
