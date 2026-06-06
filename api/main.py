from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

class Customer(BaseModel):
    tenure: int
    monthly_charges: float
    contract: str
    internet_service: str
    online_security: str
    tech_support: str
    partner: str
    dependents: str
    paperless_billing: str
    payment_method: str

pipeline = joblib.load("Saved_Model/churn_pipeline.pkl")

@app.get("/")
def home():
    return {"message": "Customer Churn API is running"}

@app.get("/model-info")
def model_info():
    return {
        "model": "Logistic Regression",
        "accuracy": 81.69,
        "precision": 68.85,
        "recall": 56.30,
        "f1_score": 61.95,
        "features": 10
    }

@app.post("/predict")
def predict(customer: Customer):

    data = {
        "tenure": [customer.tenure],
        "MonthlyCharges": [customer.monthly_charges],
        "Contract": [customer.contract],
        "InternetService": [customer.internet_service],
        "OnlineSecurity": [customer.online_security],
        "TechSupport": [customer.tech_support],
        "Partner": [customer.partner],
        "Dependents": [customer.dependents],
        "PaperlessBilling": [customer.paperless_billing],
        "PaymentMethod": [customer.payment_method]
    }

    import pandas as pd

    input_df = pd.DataFrame(data)

    prediction = pipeline.predict(input_df)

    probability = pipeline.predict_proba(input_df)

    churn_probability = round(
        float(probability[0][1]) * 100,
        2
    )

    return {
        "prediction": "Will Churn" if prediction[0] == "Yes" else "Will Not Churn",
        "churn_probability_percent": churn_probability
    }