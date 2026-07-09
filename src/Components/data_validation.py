# The Data Validation component should:
    #  Read the dataset path from DataIngestionArtifact
    #  Read the schema from config.schema_path
    #  Verify all expected columns exist Return a DataValidationArtifact

# It should not:
    #  Perform EDA
    #  Handle missing values
    #  Transform features
    #  Encode categorical variables

import sys

from src.Entity.config_entity import DataValidationConfig
from src.Entity.artifact_entity import (
    DataIngestionArtifact,
    DataValidationArtifact
)

from src.Utils.common import read_csv, read_yaml
from src.logger import logger
from src.exception import CustomException


class DataValidation:

    def __init__(
        self,
        config: DataValidationConfig,
        ingestion_artifact: DataIngestionArtifact
    ):

        self.config = config
        self.ingestion_artifact = ingestion_artifact

    def validate_dataset(self) -> DataValidationArtifact:

        try:

            logger.info("=" * 60)
            logger.info("Starting Data Validation")
            logger.info("=" * 60)

            df = read_csv(
                self.ingestion_artifact.raw_data_path
            )

            schema = read_yaml(
                self.config.schema_path
            )

            expected_columns = list(
                schema["columns"].keys()
            )

            missing_columns = []

            for column in expected_columns:

                if column not in df.columns:
                    missing_columns.append(column)

            if missing_columns:

                logger.error(
                    f"Missing Columns: {missing_columns}"
                )

                raise ValueError(
                    f"Missing Columns: {missing_columns}"
                )

            logger.info("Dataset validation successful.")

            validation_artifact = DataValidationArtifact(

                validation_status=True,

                validated_data_path=self.ingestion_artifact.raw_data_path

            )

            return validation_artifact

        except Exception as e:

            logger.error("Data Validation Failed.")

            raise CustomException(e, sys)