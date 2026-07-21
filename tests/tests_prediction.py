# from Customer_Churn.src.Pipeline.prediction_pipeline import (
#     CustomerData,
#     PredictionPipeline
# )

from src.Pipeline.prediction_pipeline import (
    CustomerData,
    PredictionPipeline
)

customer = CustomerData(
    gender="Female",
    SeniorCitizen=0,
    Partner="Yes",
    Dependents="No",
    tenure=12,
    PhoneService="Yes",
    MultipleLines="No",
    InternetService="Fiber optic",
    OnlineSecurity="No",
    OnlineBackup="Yes",
    DeviceProtection="No",
    TechSupport="No",
    StreamingTV="Yes",
    StreamingMovies="Yes",
    Contract="Month-to-month",
    PaperlessBilling="Yes",
    PaymentMethod="Electronic check",
    MonthlyCharges=85.5,
    TotalCharges=1026.0
)

df  = CustomerData.get_data_as_dataframe(customer)
# print(df)

pipeline = PredictionPipeline()
prediction = pipeline.predict(df)
# print(prediction)
prediction = prediction[0]

if prediction == 1:
    print("Customer is likely to churn.")
else:
    print("Customer is not likely to churn.")