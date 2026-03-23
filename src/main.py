from fastapi import FastAPI
from pydantic import BaseModel
# We import your brain
from predict import predict_churn

app = FastAPI(title="Churn Prediction Factory API")

# THE ARMOR: Our Strict Data Contract
class CustomerData(BaseModel):
    tenure: int
    MonthlyCharges: float
    TotalCharges: float
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str

@app.get("/")
def home():
    return {"message": "Welcome to the Armored Churn API!"}

# Notice we changed Dict[str, Any] to our new CustomerData contract
@app.post("/predict")
def predict_customer(customer: CustomerData):
    """Receives a strictly validated customer profile and returns risk score."""
    
    # Pydantic is an object. Our ML model expects a dictionary. 
    # model_dump() safely translates the validated object back into a dictionary.
    customer_dict = customer.model_dump()
    
    # Hand the safe data to your machine learning script
    pred, prob = predict_churn(customer_dict)
    
    return {
        "risk_score": float(prob),
        "prediction": int(pred),
        "status": "HIGH RISK CHURN" if pred == 1 else "SAFE"
    }