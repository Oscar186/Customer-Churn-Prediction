from src.Components.data_ingestion import DataIngestion
from src.Components.data_validation import DataValidation
from src.Components.data_transformation import DataTransformation
from src.Config.Configuration import ConfigurationManager


class TrainingPipeline:
    def __init__(self):
        self.config = ConfigurationManager()

    def start(self):
        ingestion_config = self.config.get_data_ingestion_config()
        ingestion = DataIngestion(ingestion_config)
        ingestion_artifact = ingestion.initiate_data_ingestion()

        validation_config = self.config.get_data_validation_config()
        validation = DataValidation(validation_config, ingestion_artifact)
        validation_artifact = validation.initiate_data_validation()

        transformation_config = self.config.get_data_transformation_config()
        transformation = DataTransformation(
            transformation_config,
            validation_artifact
        )
        transformation_artifact = transformation.initiate_data_transformation()

        return transformation_artifact
    
if __name__ == "__main__":
    pipeline = TrainingPipeline()
    pipeline.start()