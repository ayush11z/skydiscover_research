---
name: IO-DiscoveryController._get_image_output_dir
description: method in skydiscover/search/default_discovery_controller.py (inner-loop)
metadata:
  type: project
---

# DiscoveryController._get_image_output_dir

**File:** `skydiscover/search/default_discovery_controller.py:916`  
**Kind:** method  
**Layer:** #inner-loop

## Source
````python
    def _get_image_output_dir(self) -> str:
        """Return the directory for saving VLM-generated images."""
        base = self.output_dir or "."
        d = os.path.join(base, "generated_images")
        os.makedirs(d, exist_ok=True)
        return d
````

## → Calls
- [[IO-DiscoveryControllerInput.output_dir]]

## ← Called by
- [[IO-DiscoveryController._run_iteration]]
