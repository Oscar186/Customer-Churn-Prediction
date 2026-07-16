import sys
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from src.logger import logger
from src.exception import CustomException
from src.Entity.config_entity import DataTransformationConfig
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from src.Utils.common import (
    read_csv,
    save_object,
    save_numpy_array
)

from src.Entity.artifact_entity import (
    DataValidationArtifact,
    DataTransformationArtifact
)

class DataTransformation:

    def __init__(
        self, 
        config: DataTransformationConfig,
        validation_artifact: DataValidationArtifact
    ):
        self.config = config
        self.validation_artifact = validation_artifact

    def get_preprocessor(self):

        try: 
            logger.info("Creating preprocessing pipeline...")

            numerical_columns = [
            "tenure",
            "MonthlyCharges"
            ]

            categorical_columns = [
            "gender",
            "SeniorCitizen",
            "Partner",
            "Dependents",
            "PhoneService",
            "MultipleLines",
            "InternetService",
            "OnlineSecurity",
            "OnlineBackup",
            "DeviceProtection",
            "TechSupport",
            "StreamingTV",
            "StreamingMovies",
            "Contract",
            "PaperlessBilling",
            "PaymentMethod"
            ]
            

            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    (
                        "encoder",
                        OneHotEncoder(
                            handle_unknown="ignore",
                            drop="if_binary"
                        )
                    )
                ]
            )


            preprocessor = ColumnTransformer(
                    [
                        ("num", num_pipeline, numerical_columns),
                        ("cat", cat_pipeline, categorical_columns)
                    ]
                )
            
            logger.info("Preprocessing pipeline created successfully.")

            return preprocessor
        
        except Exception as e:
            logger.error("Error while creating preprocessing pipeline")
            raise CustomException(e, sys)
    
    def initiate_data_transformation(self) -> DataTransformationArtifact:

        try:

            logger.info("=" * 60)
            logger.info("Starting Data Transformation")
            logger.info("=" * 60)

            # ==============================
            # Read Validated Dataset
            # ==============================

            df = read_csv(
                self.validation_artifact.validated_data_path
            )

            logger.info(f"Dataset Loaded Successfully. Shape: {df.shape}")

            # ==============================
            # Split Features & Target
            # ==============================

            X = df.drop(columns=["customerID","Churn"])

            y = df["Churn"].map(
                {
                    "No": 0,
                    "Yes": 1
                }
            )

            logger.info("Features and Target separated successfully.")

            # ==============================
            # Train Test Split
            # ==============================

            X_train, X_test, y_train, y_test = train_test_split(

                X,
                y,

                test_size=0.20,

                random_state=42,

                stratify=y

            )

            logger.info(
                f"Train Shape : {X_train.shape}"
            )

            logger.info(
                f"Test Shape : {X_test.shape}"
            )

            # ==============================
            # Create Preprocessor
            # ==============================

            preprocessor = self.get_preprocessor()

            # ==============================
            # Fit & Transform
            # ==============================

            X_train_processed = preprocessor.fit_transform(
                X_train
            )

            X_test_processed = preprocessor.transform(
                X_test
            )

            logger.info(
                "Data preprocessing completed successfully."
            )

            # ==============================
            # Combine X and y
            # ==============================

            train_array = np.c_[

                X_train_processed,

                y_train.to_numpy()

            ]

            test_array = np.c_[

                X_test_processed,

                # np.array(y_test)
                y_test.to_numpy()

            ]

            # ==============================
            # Save Preprocessor
            # ==============================
            logger.info(
                "Saving preprocessing pipeline..."
            )
            save_object(

                self.config.preprocessor_path,

                preprocessor

            )

            logger.info(
                "Preprocessor saved successfully."
            )

            # ==============================
            # Save Train/Test Arrays
            # ==============================

            save_numpy_array(

                self.config.train_array_path,

                train_array

            )

            save_numpy_array(

                self.config.test_array_path,

                test_array

            )

            logger.info(
                "Train and Test arrays saved successfully."
            )

            # ==============================
            # Create Artifact
            # ==============================

            transformation_artifact = DataTransformationArtifact(

                train_array_path=self.config.train_array_path,

                test_array_path=self.config.test_array_path,

                preprocessor_path=self.config.preprocessor_path,
                
                # trained_model_path = self.config.trained_model_path,

                # metrics_path = self.config.metrics_path,

                # report_path = self.config.report_path


            )

            logger.info("=" * 60)
            logger.info("Data Transformation Completed Successfully.")
            logger.info("=" * 60)

            return transformation_artifact

        except Exception as e:

            logger.error(
                "Data Transformation Failed."
            )

            raise CustomException(e, sys)