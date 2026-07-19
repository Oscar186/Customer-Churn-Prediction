from pathlib import Path
import yaml
# import os
from src.Utils.common import create_directories
from src.Entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
    ModelEvaluationConfig,
    ModelPusherConfig
)
from src.Constants import (
    MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE_KEY,
    MODEL_EVALUATION_CONFIG_KEY,
    MODEL_EVALUATION_FILE_PATH_KEY,
    MODEL_PUSHER_CONFIG_KEY,
    SAVED_MODEL_DIR_KEY,
    MODEL_FILE_NAME_KEY
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
    
    def get_data_ingestion_config(self):
        config = self.get("data_ingestion")

        return DataIngestionConfig(

            root_dir=Path(config["root_dir"]),

            source_data_path = Path(config["source_data_path"]),

            local_data_file=Path(config["local_data_file"])
            
        )
    
    def get_data_validation_config(self):

        config = self.get("data_validation")

        return DataValidationConfig(

            root_dir=Path(config["root_dir"]),

            data_path=Path(config["data_path"]),

            schema_path=Path(config["schema_path"])

        )

    def get_data_transformation_config(self):

        config = self.get("data_transformation")

        return DataTransformationConfig(

            root_dir=Path(config["root_dir"]),

            data_path=Path(config["data_path"]),

            preprocessor_path=Path(config["preprocessor_path"]),

            train_array_path=Path(config["train_array_path"]),

            test_array_path=Path(config["test_array_path"]),

        )
    
    def get_model_trainer_config(self):

        config = self.config["model_trainer"]

        create_directories([config["root_dir"]])

        return ModelTrainerConfig(

            root_dir=Path(config["root_dir"]),

            trained_model_path=Path(config["trained_model_path"]),

            metrics_file_path=Path(config["metrics_file_path"]),

            model_report_path=Path(config["model_report_path"]),

            test_array_path= Path(config['test_array_path']),

            train_array_path= Path(config['test_array_path'])

        )
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        
        config = self.config[MODEL_EVALUATION_CONFIG_KEY]

        return ModelEvaluationConfig(

            changed_threshold_score=config[MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE_KEY],

            model_evaluation_file_path=Path(config[MODEL_EVALUATION_FILE_PATH_KEY])

        )
    
    def get_model_pusher_config(self) -> ModelPusherConfig:

        config = self.config[MODEL_PUSHER_CONFIG_KEY]

        return ModelPusherConfig(

            saved_model_dir=Path(config[SAVED_MODEL_DIR_KEY]),

            model_file_name=Path(config[MODEL_FILE_NAME_KEY])

        )


