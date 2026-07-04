from pathlib import Path
import sys

from src.config import Config
from src.exception import CustomException
from src.logger import logger
from src.utils import read_csv


class DataIngestion:
    """
    Handles data ingestion for the project.
    """

    def __init__(self):
        self.config = Config()
        self.raw_data_path = Path(self.config.get("paths", "raw_data"))

    def initiate_data_ingestion(self):
        """
        Read the raw dataset and return a DataFrame.
        """

        try:
            logger.info("Starting Data Ingestion...")

            if not self.raw_data_path.exists():
                raise FileNotFoundError(
                    f"Dataset not found: {self.raw_data_path}"
                )

            logger.info(f"Dataset Found: {self.raw_data_path}")

            df = read_csv(self.raw_data_path)
            logger.info("Data Ingestion Completed Successfully.")

            return df

        except Exception as e:
            logger.error("Data Ingestion Failed.")
            raise CustomException(e, sys)