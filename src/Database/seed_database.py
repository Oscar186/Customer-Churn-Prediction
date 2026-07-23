import pandas as pd
# from src.logger import logger
from sqlalchemy.exc import SQLAlchemyError
from src.Database.database import Session
from src.Database.models import Customer

CSV_PATH = "data/RAW/WA_Fn-UseC_-Telco-Customer-Churn.csv"

def seed_database():
    
    session = Session()

    try: 

        if session.query(Customer).first():
            print('Database already contains data.')
            return 
        
        df = pd.read_csv(CSV_PATH)

        df['TotalCharges'] = (
            df['TotalCharges'].replace(" ",0).astype(float)
        )

        customers = []

        for _, row in df.iterrows():

            customer = Customer(
                customerID=row["customerID"],
                gender=row["gender"],
                SeniorCitizen=int(row["SeniorCitizen"]),
                Partner=row["Partner"],
                Dependents=row["Dependents"],
                tenure=int(row["tenure"]),
                PhoneService=row["PhoneService"],
                MultipleLines=row["MultipleLines"],
                InternetService=row["InternetService"],
                OnlineSecurity=row["OnlineSecurity"],
                OnlineBackup=row["OnlineBackup"],
                DeviceProtection=row["DeviceProtection"],
                TechSupport=row["TechSupport"],
                StreamingTV=row["StreamingTV"],
                StreamingMovies=row["StreamingMovies"],
                Contract=row["Contract"],
                PaperlessBilling=row["PaperlessBilling"],
                PaymentMethod=row["PaymentMethod"],
                MonthlyCharges=float(row["MonthlyCharges"]),
                TotalCharges=float(row["TotalCharges"]),
                Churn=row["Churn"]
            )

            customers.append(customer)

        session.bulk_save_objects(customers)

        session.commit()

        print(f"{len(customers)} records inserted successfully.")

    
    except SQLAlchemyError:
        session.rollback()
        raise

    finally:
        session.close()

if __name__ == "__main__":
    seed_database()

