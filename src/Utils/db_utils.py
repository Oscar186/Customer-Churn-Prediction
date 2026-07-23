import pandas as pd
from sqlalchemy import text

from src.Database.database import engine
from src.logger import logger
from src.exception import CustomException

import sys

def read_table(table_name: str) -> pd.DataFrame:

    try:

        logger.info(f"Reading table '{table_name}' from PostgreSQL.")

        query = text(f"SELECT * FROM {table_name}")

        with engine.connect() as conn:
            df = pd.read_sql(query, conn)

        logger.info(f"Successfully loaded {len(df)} records from '{table_name}'.")

        return df
    
    except Exception as e:
        raise CustomException(e, sys)
