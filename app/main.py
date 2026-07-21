from fastapi import (
    FastAPI,
    HTTPException
)
from src.Pipeline.prediction_pipeline import (
    CustomerData,
    PredictionPipeline
)
from app.schema import (
    CustomerRequest,
    PredictionResponse
)
from src.logger import logger

app = FastAPI(
    title="Customer Churn Prediction API",
    description="Production-ready API for predicting customer churn using a trained Gradient Boosting model.",
    version="1.0.0",
    contact= {
        "Name": "Stark"
    },
    license_info= {
        "name": "MIT"
    }
)


@app.get('/health',tags=['General'])
def health_check():
    return {
        "status": "healthy",
        "model": "loaded",
        "message": "Customer Churn Prediction API is running."
    }


@app.post(
        "/predict",tags=['Prediction'],
        response_model= PredictionResponse,    
        summary="Predict customer churn",
        description="Predict whether a telecom customer is likely to churn."
    )
def predict(data: CustomerRequest):

    try: 
        customer = CustomerData(
            gender=data.gender,
            SeniorCitizen=data.SeniorCitizen,
            Partner=data.Partner,
            Dependents=data.Dependents,
            tenure=data.tenure,
            PhoneService=data.PhoneService,
            MultipleLines=data.MultipleLines,
            InternetService=data.InternetService,
            OnlineSecurity=data.OnlineSecurity,
            OnlineBackup=data.OnlineBackup,
            DeviceProtection=data.DeviceProtection,
            TechSupport=data.TechSupport,
            StreamingTV=data.StreamingTV,
            StreamingMovies=data.StreamingMovies,
            Contract=data.Contract,
            PaperlessBilling=data.PaperlessBilling,
            PaymentMethod=data.PaymentMethod,
            MonthlyCharges=data.MonthlyCharges,
            TotalCharges=data.TotalCharges,
        )

        df = customer.get_data_as_dataframe()

        pipeline = PredictionPipeline()

        prediction = pipeline.predict(df)

        probabilities = pipeline.predict_proba(df)[0]

        response = {
            "prediction": int(prediction),
            "probability": {
                "not_churn": round(float(probabilities[0]), 4)*100,
                "churn": round(float(probabilities[1]), 4)*100,
            },
            "result": (
                "Customer is likely to churn."
                if prediction == 1
                else "Customer is not likely to churn."
            ),
        }

        return response
    
    except Exception:
        logger.exception("Prediction failed.")

        raise HTTPException(
            status_code=500,
            detail="Prediction failed."
            )
