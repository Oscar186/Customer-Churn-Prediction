from src.Entity.artifact_entity import (
    ModelEvaluationArtifact,
    ModelPusherArtifact,
    DataTransformationArtifact,
    ModelTrainerArtifact
)
from src.Entity.config_entity import ModelPusherConfig
from shutil import copy2
from src.logger import logger
from src.exception import CustomException
import sys
from src.Utils.common import ensure_parent_directory
from pathlib import Path

class ModelPusher:

    def __init__(self,
        config: ModelPusherConfig,
        model_evaluation_artifact: ModelEvaluationArtifact,
        data_transformation_artifact: DataTransformationArtifact,
        model_trainer_artifact: ModelTrainerArtifact
    ):
        self.config = config
        self.model_evaluation_artifact = model_evaluation_artifact
        self.data_transformation_artifact = data_transformation_artifact
        self.model_trainer_artifact = model_trainer_artifact

    def push_model(self):

        try:

            logger.info("Copying accepted model to production directory.")

            saved_model_path = (Path(self.config.saved_model_dir)/self.config.model_file_name)
            model_source = self.model_evaluation_artifact.trained_model_path
            preprocessor_source = self.data_transformation_artifact.preprocessor_path
            ensure_parent_directory(saved_model_path)

            model_destination = (Path(self.config.saved_model_dir)/ "model.pkl")
            preprocessor_destination = (Path(self.config.saved_model_dir)/ "preprocessor.pkl")
            ensure_parent_directory(model_destination)

            copy2(model_source, model_destination)
            copy2(preprocessor_source, preprocessor_destination)

            logger.info('Successfully copied model to production directory.')

            return saved_model_path
        
        except Exception as e:
            raise CustomException(e, sys)

    def initiate_model_pusher(self):

        try:
            
            logger.info("Starting Model Pusher.")

            if self.model_evaluation_artifact.is_model_accepted:
                saved_model_path = self.push_model()
            else:
                saved_model_path = None

            logger.info("Model Pusher completed successfully.")
            
            return ModelPusherArtifact(str(saved_model_path) if saved_model_path else None)

        except Exception as e:
            raise CustomException(e, sys)
        