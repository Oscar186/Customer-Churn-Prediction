from pathlib import Path
import yaml


class Config:
    def __init__(self):
        project_root = Path(__file__).resolve().parent.parent
        config_path = project_root / "configs" / "config.yaml"

        print("Config Path:", config_path)

        with open(config_path, "r") as file:
            self.config = yaml.safe_load(file)

        print("Loaded Config:", self.config)

    def get(self, *keys):
        value = self.config

        for key in keys:
            if not isinstance(value, dict):
                raise TypeError(
                    f"Expected a dictionary while looking for '{key}', "
                    f"but found {type(value).__name__}."
                )

            if key not in value:
                raise KeyError(
                    f"Configuration key '{key}' not found."
                )

            value = value[key]

        return value