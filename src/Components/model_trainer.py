import sys
import pandas as pd
import time

from src.logger import logger
from src.exception import CustomException
from src.Entity.artifact_entity import DataTransformationArtifact
from src.Entity.artifact_entity import ModelTrainerArtifact
from src.Entity.config_entity import ModelTrainerConfig
from src.Utils.common import (
    load_numpy_array,
    save_json,
    save_object,
    save_dataframe
)
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    RandomForestClassifier,
    GradientBoostingClassifier,
    AdaBoostClassifier
)

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)
from src.Utils.mlflow_utils import MLFlowManager
import sklearn
import platform
class ModelTrainer:

    def __init__(self,config: ModelTrainerConfig, data_transformation_artifact: DataTransformationArtifact):

        self.config = config
        self.data_transformation_artifact = data_transformation_artifact

    def load_train_test_data(self):
        try:
            logger.info("Loading transformed training and test arrays.")

            train_arr = load_numpy_array(
                self.data_transformation_artifact.train_array_path
            )

            test_arr = load_numpy_array(
                self.data_transformation_artifact.test_array_path
            )

            X_train = train_arr[:, :-1]
            y_train = train_arr[:, -1]

            X_test = test_arr[:, :-1]
            y_test = test_arr[:, -1]

            logger.info('Train/Test data loaded successfully.')

            return X_train,y_train,X_test,y_test
        
        except Exception as e:
            raise CustomException(e, sys)
            
    def get_models(self):

        models = {

            "Logistic Regression": LogisticRegression(max_iter=1000),

            "Decision Tree": DecisionTreeClassifier(random_state=42),

            "Random Forest": RandomForestClassifier(random_state=42),

            "Gradient Boosting": GradientBoostingClassifier(random_state=42),

            "AdaBoost": AdaBoostClassifier(random_state=42)

        }

        return models

    def evaluate_model(self,model,X_train,y_train,X_test,y_test):
    
        model.fit(X_train,y_train)

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

        return metrics

    def get_best_model(
        self,
        models,
        X_train,
        y_train,
        X_test,
        y_test
    ):
        """
        Train all models, evaluate them and return the best model.

        Returns:
            best_model
            best_model_name
            best_metrics
            report_df
        """

        try:

            logger.info("Evaluating candidate models.")

            report = []

            best_model = None
            best_model_name = None
            best_metrics = None
            best_score = float("-inf")

            for model_name, model in models.items():

                logger.info(f"Training {model_name}")

                metrics = self.evaluate_model(
                    model,
                    X_train,
                    y_train,
                    X_test,
                    y_test
                )

                report.append({
                    "Model": model_name,
                    **metrics
                })

                if metrics["ROC AUC"] > best_score:

                    best_score = metrics["ROC AUC"]
                    best_model = model
                    best_model_name = model_name
                    best_metrics = metrics

            report_df = pd.DataFrame(report)

            logger.info(
                f"Best Model: {best_model_name} | ROC AUC: {best_score:.4f}"
            )

            return (
                best_model,
                best_model_name,
                best_metrics,
                report_df,
                best_score
            )

        except Exception as e:
            raise CustomException(e, sys)

    def save_artifacts(
            self,
            best_model,
            report_df,
            metrics
        ):

        logger.info("Saving trained model.")

        save_object(
            self.config.trained_model_path,
            best_model
        )

        logger.info("Saving metrics.")

        save_json(
            self.config.metrics_file_path,
            metrics
        )

        logger.info("Saving model report.")

        save_dataframe(
            self.config.model_report_path,
            report_df
        )

    def initiate_model_trainer(self):

        try:



            logger.info("Starting Model Training.")

            mlflowmanager = MLFlowManager("Customer-Churn")

            mlflowmanager.set_experiment()

            X_train, y_train, X_test, y_test = self.load_train_test_data()

            models = self.get_models()

            start_time = time.time()

            with mlflowmanager.start_run():
                (
                    best_model,
                    best_model_name,
                    best_metrics,
                    report_df,
                    best_score
                ) = self.get_best_model(
                    models,
                    X_train,
                    y_train,
                    X_test,
                    y_test
                )

                self.save_artifacts(
                    best_model=best_model,
                    report_df=report_df,
                    metrics=best_metrics
                )
                training_time = round(time.time() - start_time, 2)
                mlflowmanager.log_metrics(best_metrics)
                mlflowmanager.log_metrics(
                    {
                        "training_time_seconds": training_time
                    }
                )
                mlflowmanager.log_params({
                        "model_name": best_model.__class__.__name__,
                        "train_rows": X_train.shape[0],
                        "test_rows": X_test.shape[0],
                        "features": X_train.shape[1]
                    }
                )
                mlflowmanager.log_artifact(
                    self.config.model_report_path,
                    artifact_path="reports"
                )
                mlflowmanager.log_artifact(
                    self.config.metrics_file_path,
                    artifact_path="metrics"
                )
                mlflowmanager.log_artifact("configs/config.yaml", artifact_path= None)
                mlflowmanager.log_artifact("configs/schema.yaml", artifact_path= None)
                mlflowmanager.log_params({
                    "python_version": platform.python_version(),
                    "sklearn_version": sklearn.__version__,
                })
                mlflowmanager.log_tags(
                    {
                        "project": "Customer Churn Prediction",
                        "framework": "Scikit-Learn",
                        "stage": "Training",
                        "algorithm": best_model_name,
                        "version": "1.0"
                    }
                )

                predictions = best_model.predict(X_train)

                mlflowmanager.log_model(
                    model=best_model,
                    X_train=X_train,
                    predictions=predictions
                )

            logger.info(
                f"Best Model : {best_model_name} | ROC AUC : {best_score:.4f}"
            )

            return ModelTrainerArtifact(

                trained_model_path=self.config.trained_model_path,

                metrics_file_path=self.config.metrics_file_path,

                report_file_path=self.config.model_report_path,

                best_model_name=best_model_name,

                best_score=best_score

            )

        except Exception as e:

            raise CustomException(e, sys)