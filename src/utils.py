import sys
from pathlib import Path
import yaml
import pandas as pd

from src.logger import logger
from src.exception import CustomException


def read_yaml(file_path):
    """
    Read YAML file.

    Args:
        file_path (str | Path)

    Returns:
        dict
    """

    try:

        logger.info(f"Reading YAML : {file_path}")

        with open(file_path, "r") as file:
            data = yaml.safe_load(file)

        logger.info("YAML Loaded Successfully.")

        return data

    except Exception as e:

        logger.error("Unable to read YAML.")

        raise CustomException(e, sys)

def create_directories(paths):
    """
    Create one or more directories.

    Args:
        paths (list | str): Directory path(s) to create.
    """

    try:
        if isinstance(paths, str):
            paths = [paths]

        for path in paths:
            Path(path).mkdir(parents=True, exist_ok=True)
            logger.info(f"Directory created/verified: {path}")

    except Exception as e:
        logger.error("Error while creating directories.")
        raise CustomException(e, sys)


def read_csv(file_path):
    """
    Read a CSV file.

    Args:
        file_path (str | Path)

    Returns:
        pandas.DataFrame
    """

    try:
        logger.info(f"Reading CSV file: {file_path}")

        df = pd.read_csv(file_path)

        logger.info(f"Dataset loaded successfully.")
        logger.info(f"Dataset Shape: {df.shape}")

        return df

    except Exception as e:
        logger.error(f"Unable to read CSV: {file_path}")
        raise CustomException(e, sys)


def save_csv(df, file_path):
    """
    Save DataFrame to CSV.

    Args:
        df (DataFrame)
        file_path (str | Path)
    """

    try:
        file_path = Path(file_path)

        file_path.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"Saving CSV to: {file_path}")

        df.to_csv(file_path, index=False)

        logger.info("CSV saved successfully.")

    except Exception as e:
        logger.error(f"Unable to save CSV: {file_path}")
        raise CustomException(e, sys)