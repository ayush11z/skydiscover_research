---
name: AdaptiveState.get_search_intensity
description: method in skydiscover/search/adaevolve/adaptation.py (adaevolve)
metadata:
  type: project
---

# AdaptiveState.get_search_intensity

**File:** `skydiscover/search/adaevolve/adaptation.py:152`  
**Kind:** method  
**Layer:** #adaevolve

## Source
````python
    def get_search_intensity(self) -> float:
        """
        Compute search intensity based on accumulated signal.

        Uses inverse relationship with sqrt of accumulated signal:
            intensity = I_min + (I_max - I_min) / (1 + √(G + ε))

        - High G → intensity approaches I_min (exploit productive island)
        - Low G → intensity approaches I_max (explore stagnating island)

        Returns:
            intensity: Float in [intensity_min, intensity_max]
        """
        G = self.accumulated_signal

        intensity = self.intensity_min + (self.intensity_max - self.intensity_min) / (
            1 + math.sqrt(G + self.epsilon)
        )

        return intensity
````

## → Calls
_(leaf — calls nothing in this graph)_

## ← Called by
_(entry point — nothing in this graph calls it)_
