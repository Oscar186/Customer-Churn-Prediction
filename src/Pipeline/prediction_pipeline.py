import pandas as pd
from src.logger import logger
from src.exception import CustomException
import sys
from pathlib import Path
from src.Utils.common import load_object
class CustomerData:
    
    def __init__(self,
        gender: str,
        SeniorCitizen: int,
        Partner: str,
        Dependents: str,
        tenure: int,
        PhoneService: str,
        MultipleLines: str,
        InternetService: str,
        OnlineSecurity: str,
        OnlineBackup: str,
        DeviceProtection: str,
        TechSupport: str,
        StreamingTV: str,
        StreamingMovies: str,
        Contract: str,
        PaperlessBilling: str,
        PaymentMethod: str,
        MonthlyCharges: float,
        TotalCharges: float         
    ):
        self.gender = gender
        self.SeniorCitizen = SeniorCitizen
        self.Partner = Partner
        self.Dependents = Dependents
        self.tenure = tenure
        self.PhoneService = PhoneService
        self.MultipleLines = MultipleLines
        self.InternetService = InternetService
        self.OnlineSecurity = OnlineSecurity
        self.OnlineBackup = OnlineBackup
        self.DeviceProtection = DeviceProtection
        self.TechSupport = TechSupport
        self.StreamingTV = StreamingTV
        self.StreamingMovies = StreamingMovies
        self.Contract = Contract
        self.PaperlessBilling = PaperlessBilling
        self.PaymentMethod = PaymentMethod
        self.MonthlyCharges = MonthlyCharges
        self.TotalCharges = TotalCharges

    def get_data_as_dataframe(self):
        
        try: 

            logger.info("Creating customer input DataFrame.")
            customer_data = {
                "gender": [self.gender],
                "SeniorCitizen": [self.SeniorCitizen],
                "Partner": [self.Partner],
                "Dependents": [self.Dependents],
                "tenure": [self.tenure],
                "PhoneService": [self.PhoneService],
                "MultipleLines": [self.MultipleLines],
                "InternetService" : [self.InternetService],
                "OnlineSecurity" : [self.OnlineSecurity],
                "OnlineBackup": [self.OnlineBackup],
                "DeviceProtection": [self.DeviceProtection],
                "TechSupport": [self.TechSupport],
                "StreamingTV": [self.StreamingTV],
                "StreamingMovies": [self.StreamingMovies],
                "Contract": [self.Contract],
                "PaperlessBilling": [self.PaperlessBilling],
                "PaymentMethod": [self.PaymentMethod],
                "MonthlyCharges": [self.MonthlyCharges],
                "TotalCharges": [self.TotalCharges]
            }

            data_frame = pd.DataFrame(customer_data)

            logger.info("Customer DataFrame created successfully.")
            return data_frame
        
        except Exception as e:
            raise CustomException(e, sys)

class PredictionPipeline:
    
    def __init__(self):

        self.model_path = Path("production_models/model.pkl")
        self.preprocessor_path = Path("production_models/preprocessor.pkl")

    def predict(self, feature: pd.DataFrame):
        
        try:

            logger.info("Loading production preprocessor.")
            preprocessor = load_object(self.preprocessor_path)

            logger.info("Loading production model.")
            model = load_object(self.model_path)

            logger.info("Transforming the features.")
            transformed_features = preprocessor.transform(feature)

            logger.info("Generating Prediction.")
            prediction = model.predict(transformed_features)[0]

            # probability = None

            # if hasattr(model, "predict_proba"):
            #     probability = model.predict_proba(transformed_features)[0][1]
                
            return prediction

        except Exception as e:
            raise CustomException(e, sys)
        
    def predict_proba(self, features):
        try:

            preprocessor = load_object(self.preprocessor_path)
            model = load_object(self.model_path)

            transformed = preprocessor.transform(features)

            return model.predict_proba(transformed)

        except Exception as e:
            raise CustomException(e, sys)