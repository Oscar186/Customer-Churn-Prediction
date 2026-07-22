import mlflow
import mlflow.sklearn
from mlflow.models.signature import infer_signature
import sys
from src.logger import logger
from src.exception import CustomException

class MLFlowManager:

    def __init__(self, experiment_name: str):
        self.experiment_name = experiment_name
        
    def set_experiment(self):

        try:
            
            logger.info(
                f'Setting ML Flow Experiment: {self.experiment_name}'
            )

            mlflow.set_experiment(self.experiment_name)

        except Exception as e:
            raise CustomException(e, sys)
        
    def start_run(self):

        try:
            logger.info("Starting ML Flow Run.")

            return mlflow.start_run()

        except Exception as e:
            raise CustomException(e,sys)
        
    def log_params(self, params: dict):

        try:
            logger.info(f"Logging Params: {params}")
            mlflow.log_params(params)
        except Exception as e:
            raise CustomException(e,sys)
        
    def log_metrics(self, metrics: dict):
        try:
            logger.info(f"Logging Metrics: {metrics}")
            mlflow.log_metrics(metrics)

        except Exception as e:
            raise CustomException(e,sys)
        
    def log_model(self,model,X_train,predictions,artifact_path="model"):
        
        try:
            signature = infer_signature(
                X_train,
                predictions
            )

            model_info = mlflow.sklearn.log_model(
                sk_model=model,
                artifact_path="model",
                signature=signature,
                input_example=X_train[:5]
            )

            mlflow.register_model(
                model_uri=model_info.model_uri,
                name="Customer-Churn-Model"
            )

        except Exception as e:
            raise CustomException(e, sys)
        
    def log_tags(self, tags: dict):
        try:
            logger.info(f"Logging tags: {tags}")
            mlflow.set_tags(tags)

        except Exception as e:
            raise CustomException(e,sys)
    
    def log_artifact(self, path: str,artifact_path):
        try:
            logger.info(f"Logging Artifact: {path}")
            mlflow.log_artifact(path,artifact_path)

        except Exception as e:
            raise CustomException(e,sys)
        
    def log_artifacts(self, directory: str):
        try:
            logger.info(f"Logging Artifacts: {directory}")
            mlflow.log_artifacts(directory)

        except Exception as e:
            raise CustomException(e,sys)
    
