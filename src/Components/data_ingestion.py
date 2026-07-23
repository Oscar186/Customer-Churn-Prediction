# Responsibility of this file

# This component should only:
    # Read the configuration.
    # Verify the dataset exists.
    # Return the artifact.

# It should not:
    # Validate the schema.
    # Transform the data.
    # Split train/test.
    # Perform preprocessing.

import sys
# import shutil
from src.Entity.config_entity import DataIngestionConfig
from src.Entity.artifact_entity import DataIngestionArtifact

from src.logger import logger
from src.exception import CustomException

from src.Utils.db_utils import read_table
from src.Utils.common import save_dataframe



class DataIngestion:
    """
    Handles data ingestion for the project.
    """

    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def initiate_data_ingestion(self) -> DataIngestionArtifact:

        try:

            logger.info("=" * 60)
            logger.info("Starting Data Ingestion")
            logger.info("=" * 60)

            logger.info("Reading customer data from PostgreSQL.")

            df = read_table("customers")

            logger.info(
                f"Retrieved {len(df)} records from PostgreSQL."
            )

            save_dataframe(
                self.config.local_data_file,
                df
            )

            logger.info(
                f"Dataset saved to {self.config.local_data_file}"
            )

            ingestion_artifact = DataIngestionArtifact(
                raw_data_path=self.config.local_data_file
            )

            logger.info("Data Ingestion Completed Successfully.")

            return ingestion_artifact

        except Exception as e:

            logger.error("Data Ingestion Failed.")

            raise CustomException(e, sys)