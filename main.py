# from Customer_Churn.src.Components.data_validation import DataValidation

# def main():

#     validator = DataValidation()

#     status = validator.validate_dataset()

#     print(f"\nValidation Status : {status}")


# if __name__ == "__main__":
#     main()

# import numpy as np

# np_ar = np.load(r'Customer_Churn\artifacts\data_transformation\test.npy')

# print(np_ar)

# from sqlalchemy import text
# from src.Database.database import engine

# with engine.connect() as conn:
#     result = conn.execute(text("SELECT version();"))
#     print(result.fetchone())

from src.Database.database import Base, engine
from src.Database.models import Customer

Base.metadata.create_all(bind=engine)

print("Tables created successfully.")