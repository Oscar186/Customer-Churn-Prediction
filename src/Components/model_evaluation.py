import sys
from src.Config.Configuration import ModelEvaluationConfig
from src.Entity.artifact_entity import (
    DataTransformationArtifact,
    ModelTrainerArtifact,
    ModelEvaluationArtifact
)
from src.Utils.common import (
    load_numpy_array,
    save_yaml,
    load_object
)
from src.logger import logger
from src.exception import CustomException
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)
class ModelEvaluation:

    def __init__(
        self,config : ModelEvaluationConfig, 
        data_transformation_artifact : DataTransformationArtifact, 
        model_trainer_artifact : ModelTrainerArtifact
    ):

        self.config = config
        self.data_transformation_artifact = data_transformation_artifact
        self.model_trainer_artifact = model_trainer_artifact

    def load_test_data(self):

        try:

            logger.info('Loading transformed test arrays.')

            test_arr = load_numpy_array(
                self.data_transformation_artifact.test_array_path
            )
            X_test = test_arr[:, :-1]
            y_test = test_arr[:, -1]

            logger.info('Test data loaded successfully') 

            return X_test, y_test

        except Exception as e:
            raise CustomException(e, sys)

    def get_best_model(self): #Check if whether a production model already exist else return None.
        return None

    def evaluate_model(self,model,X_test,y_test): #Run Predictions and Calculate Metrics

        """Evaluate a trained model on the test dataset and return the evaluation metrics."""
        try: 
            logger.info('Evaluating candidate model.')
            predictions = model.predict(X_test)

            if hasattr(model, "predict_proba"):
                probabilities = model.predict_proba(X_test)[:, 1]
            else:
                probabilities = predictions

            metrics = {
                "Accuracy": accuracy_score(y_test, predictions),

                "Precision": precision_score(y_test, predictions,zero_division=0),

                "Recall": recall_score(y_test, predictions,zero_division = 0),

                "F1 Score": f1_score(y_test, predictions,zero_division = 0),

                "ROC AUC": roc_auc_score(y_test, probabilities)
            }

            logger.info('Candidate model evaluated successfully.')

            return metrics

        except Exception as e:
            raise CustomException(e, sys)
    
    # def compare_models(self): #Compares prod and base model.

    def write_evaluation_report(self,report: dict): #Create output directories and saving results to evaluation.yaml
        try:

            logger.info("Writing evaluation report.")

            save_yaml(self.config.model_evaluation_file_path,report)

            logger.info("Evaluation report saved successfully.")

        except Exception as e:
            raise CustomException(e,sys)

    def initiate_model_evaluation(self):

        try: 

            logger.info("Starting Model Evaluation.")

            X_test,y_test = self.load_test_data()

            candidate_model = load_object(self.model_trainer_artifact.trained_model_path)

            candidate_metrics = self.evaluate_model(candidate_model,X_test,y_test)

            best_model = self.get_best_model()

            if best_model is None:
                is_model_accepted = True
            else:
                is_model_accepted = False

            report = {
                "is_model_accepted": is_model_accepted,
                "accuracy_difference": candidate_metrics["Accuracy"],
                "best_model_path": self.model_trainer_artifact.trained_model_path,
                "trained_model_path": self.model_trainer_artifact.trained_model_path
            }

            self.write_evaluation_report(report)

            logger.info("Model Evaluation completed successfully.")

            return ModelEvaluationArtifact(
                is_model_accepted=is_model_accepted,
                accuracy_difference=candidate_metrics["Accuracy"],
                best_model_path=self.model_trainer_artifact.trained_model_path,
                trained_model_path=self.model_trainer_artifact.trained_model_path
            )
        except Exception as e:
            raise CustomException(e, sys)