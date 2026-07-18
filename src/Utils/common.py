import sys
from pathlib import Path
import yaml
import pandas as pd
import numpy as np
import joblib
from src.logger import logger
from src.exception import CustomException
import json

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
    
def save_yaml(file_path,data):
    try:

        logger.info(f"Saving YAML file : {file_path}")

        with open(file_path, "w") as file:
            data = yaml.dump(data,file,sort_keys=False)

        logger.info("YAML file Saved Successfully.")

        return data

    except Exception as e:

        logger.error("Unable to save YAML file.")

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

        logger.info("Dataset loaded successfully.")
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
        ensure_parent_directory(file_path)

        logger.info(f"Saving CSV to: {file_path}")

        df.to_csv(file_path, index=False)

        logger.info("CSV saved successfully.")

    except Exception as e:
        logger.error(f"Unable to save CSV: {file_path}")
        raise CustomException(e, sys)

def save_object(file_path, obj):

    try:
        ensure_parent_directory(file_path)

        logger.info(f"Saving object: {file_path}")

        joblib.dump(obj, file_path)

        logger.info("Object saved successfully.")

    except Exception as e:
        logger.error("Unable to save object.")
        raise CustomException(e, sys)
    
def load_object(file_path):
    try:
        logger.info(f"Loading object: {file_path}")

        obj = joblib.load(file_path)

        logger.info("Object loaded successfully.")

        return obj

    except Exception as e:
        logger.error("Unable to load object.")
        raise CustomException(e, sys)
    
def save_numpy_array(file_path, array):
    try:
        ensure_parent_directory(file_path)

        np.save(file_path, array)

        logger.info(f"Numpy array saved: {file_path}")
        logger.info("NumPy array saved successfully.")
        
    except Exception as e:
        raise CustomException(e, sys)

def load_numpy_array(file_path):
    try:
        logger.info(f"Loading NumPy array: {file_path}")

        array = np.load(file_path)

        logger.info("NumPy array loaded successfully.")

        return array

    except Exception as e:
        raise CustomException(e, sys)
    
def save_json(file_path, data):
    """
    Save dictionary as JSON.

    Args:
        file_path (str | Path)
        data (dict)
    """
    try:
        ensure_parent_directory(file_path)

        logger.info(f"Saving JSON file: {file_path}")

        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

        logger.info("JSON file saved successfully.")

    except Exception as e:
        logger.error("Unable to save JSON file.")
        raise CustomException(e, sys)
    
def save_dataframe(file_path, df):
    """
    Save DataFrame to CSV.

    Args:
        file_path (str | Path)
        df (pd.DataFrame)
    """
    try:
        ensure_parent_directory(file_path)

        logger.info(f"Saving DataFrame: {file_path}")

        df.to_csv(file_path, index=False)

        logger.info("DataFrame saved successfully.")

    except Exception as e:
        logger.error("Unable to save DataFrame.")
        raise CustomException(e, sys)
    
def ensure_parent_directory(file_path):
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)