from pathlib import Path
import yaml

from src.Entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig
)


class ConfigurationManager:

    def __init__(self):

        project_root = Path(__file__).resolve().parent.parent.parent

        config_path = project_root / "configs" / "config.yaml"

        with open(config_path) as file:

            self.config = yaml.safe_load(file)

    def get(self, *keys):

        value = self.config

        for key in keys:

            value = value[key]

        return value