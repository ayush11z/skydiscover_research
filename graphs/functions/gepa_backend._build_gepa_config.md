---
name: gepa_backend._build_gepa_config
description: function in skydiscover/extras/external/gepa_backend.py (external)
metadata:
  type: project
---

# gepa_backend._build_gepa_config

**File:** `skydiscover/extras/external/gepa_backend.py:136`  
**Kind:** function  
**Layer:** #external

## Source
````python
def _build_gepa_config(config: Config, iterations: int):
    from gepa.optimize_anything import EngineConfig, GEPAConfig, RefinerConfig, ReflectionConfig

    # Power-user escape hatch
    ext = getattr(config, "external_config", None)
    if isinstance(ext, GEPAConfig):
        if iterations is not None:
            ext.engine.max_candidate_proposals = iterations
        return ext

    engine_kwargs: Dict[str, Any] = {"max_candidate_proposals": iterations}
    reflection_kwargs: Dict[str, Any] = {}
    refiner_kwargs: Dict[str, Any] = {}

    # GEPA supports two model roles:
    #   reflection_lm  — generates candidate mutations  (models[0])
    #   refiner_lm     — optional refinement pass       (models[1], else defaults to reflection_lm)
    if config.llm.models:
        primary = config.llm.models[0]
        if primary.name is not None:
            provider, bare_name, _, _ = _parse_model_spec(primary.name)
            reflection_kwargs["reflection_lm"] = f"{provider}/{bare_name}"

        if len(config.llm.models) >= 2:
            secondary = config.llm.models[1]
            if secondary.name is not None:
                provider, bare_name, _, _ = _parse_model_spec(secondary.name)
                refiner_kwargs["refiner_lm"] = f"{provider}/{bare_name}"

            logger.info(
                "GEPA model mapping: reflection_lm='%s', refiner_lm='%s'",
                primary.name,
                secondary.name,
            )
            if len(config.llm.models) > 2:
                logger.warning(
                    "GEPA supports at most 2 models (reflection + refiner); "
                    "ignoring %d extra model(s)",
                    len(config.llm.models) - 2,
                )
        else:
            logger.info(
                "GEPA model mapping: reflection_lm='%s' (also used as refiner_lm)",
                primary.name,
            )

    gepa_kwargs: Dict[str, Any] = {
        "engine": EngineConfig(**engine_kwargs),
        "reflection": ReflectionConfig(**reflection_kwargs),
    }
    if refiner_kwargs:
        gepa_kwargs["refiner"] = RefinerConfig(**refiner_kwargs)

    return GEPAConfig(**gepa_kwargs)
````

## → Calls
- [[Config.llm]]
- [[config.Config]]
- [[config._parse_model_spec]]

## ← Called by
- [[gepa_backend.run]]
