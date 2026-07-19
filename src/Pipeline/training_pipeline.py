from src.Components.data_ingestion import DataIngestion
from src.Components.data_validation import DataValidation
from src.Components.data_transformation import DataTransformation
from src.Config.Configuration import ConfigurationManager
from src.Components.model_trainer import ModelTrainer
from src.Components.model_evaluation import ModelEvaluation
from src.Entity.artifact_entity import ModelPusherArtifact
from src.Components.model_pusher import ModelPusher

class TrainingPipeline:
    # def __init__(self,):
        # self.config = ConfigurationManager()
    def start(self):

        config = ConfigurationManager()
        ingestion_config = config.get_data_ingestion_config()
        ingestion = DataIngestion(ingestion_config)
        ingestion_artifact = ingestion.initiate_data_ingestion()

        validation_config = config.get_data_validation_config()
        validation = DataValidation(validation_config, ingestion_artifact)
        validation_artifact = validation.initiate_data_validation()

        transformation_config = config.get_data_transformation_config()
        transformation = DataTransformation(
            transformation_config,
            validation_artifact
        )
        transformation_artifact = transformation.initiate_data_transformation()


        training_config = config.get_model_trainer_config()
        trainer = ModelTrainer(training_config, transformation_artifact)
        trainer_artifact = trainer.initiate_model_trainer()

        evaluation_config = config.get_model_evaluation_config()
        evaluater = ModelEvaluation(
            config=evaluation_config,
            data_transformation_artifact = transformation_artifact,
            model_trainer_artifact= trainer_artifact
        )
        evaluater_artifact = evaluater.initiate_model_evaluation()

        model_pusher_config = config.get_model_pusher_config()
        model_pusher = ModelPusher(config= model_pusher_config,model_evaluation_artifact = evaluater_artifact)
        # return evaluater_artifact
        model_pusher_artifact = ModelPusherArtifact(
            model_pusher.initiate_model_pusher()
        )
    
        return model_pusher_artifact

if __name__ == "__main__":
    pipeline = TrainingPipeline()
    pipeline.start()


#  py -m src.Pipeline.training_pipeline