---
name: Config.from_yaml
description: classmethod in skydiscover/config.py (config)
metadata:
  type: project
---

# Config.from_yaml

**File:** `skydiscover/config.py:627`  
**Kind:** classmethod  
**Layer:** #config

## Source
````python
    def from_yaml(cls, path: Union[str, Path]) -> Config:
        """Load configuration from a YAML file"""
        config_path = Path(path)
        config_dir = config_path.parent

        with open(path, "r") as f:
            raw = f.read()
        config_dict = yaml.safe_load(_expand_env_vars(raw))

        # Handle file references for system_message
        if "prompt" in config_dict and "system_message" in config_dict["prompt"]:
            system_message = config_dict["prompt"]["system_message"]
            if (
                isinstance(system_message, str)
                and "\n" not in system_message.strip()
                and len(system_message.strip()) < 256
            ):
                file_path = config_dir / system_message
                try:
                    if file_path.exists() and file_path.is_file():
                        with open(file_path, "r") as f:
                            config_dict["prompt"]["system_message"] = f.read()
                except OSError:
                    logger.debug("Could not read system_message from %s", file_path, exc_info=True)

        return cls.from_dict(config_dict)
````

## → Calls
- [[Config.from_dict]]
- [[ContainerizedEvaluator.__enter__]]
- [[ContainerizedEvaluator.__exit__]]
- [[config._expand_env_vars]]

## ← Called by
- [[config.load_config]]
