import sys
from pathlib import Path

from src.config import Config
from src.exception import CustomException
from src.logger import logger
from src.utils import read_csv, read_yaml


class DataValidation:

    def __init__(self):

        self.config = Config()

        self.raw_data_path = Path(
            self.config.get("paths", "raw_data")
        )

        self.schema_path = Path(
            self.config.get("schema", "schema_file")
        )

    def validate_dataset(self):

        try:

            logger.info("Starting Data Validation...")

            df = read_csv(self.raw_data_path)

            schema = read_yaml(self.schema_path)
            # print("Project Schema:",schema)

            expected_columns = list(
                schema["columns"].keys()
            )

            missing_columns = []

            for column in expected_columns:

                if column not in df.columns:

                    missing_columns.append(column)

            if len(missing_columns) > 0:

                logger.error(
                    f"Missing Columns : {missing_columns}"
                )

                raise ValueError(
                    f"Missing Columns : {missing_columns}"
                )

            logger.info(
                "Dataset Validation Successful."
            )

            return True

        except Exception as e:

            logger.error(
                "Data Validation Failed."
            )

            raise CustomException(e, sys)