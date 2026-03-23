import joblib
import pandas as pd

def load_model():
    """Loads the saved model and the list of features."""
    # We load the dictionary we saved in Day 7/8
    model_data = joblib.load('../models/churn_model.pkl')
    return model_data['model'], model_data['features']

def predict_churn(customer_dict):
    """Takes a single customer dictionary and predicts their churn risk."""
    model, features = load_model()
    
    # 1. Convert the dictionary into a Pandas DataFrame (1 row)
    df = pd.DataFrame([customer_dict])
    
    # 2. Convert text to numbers (One-Hot Encoding)
    df_encoded = pd.get_dummies(df)
    
    # 3. ALIGNMENT (CRITICAL STEP)
    # The new customer might not have all the categories the model saw during training.
    # We force this 1 row to have the EXACT same columns as the training data.
    df_encoded = df_encoded.reindex(columns=features, fill_value=0)
    
    # 4. Ask the model for the Probability (0.0 to 1.0)
    probability = model.predict_proba(df_encoded)[0][1]
    
    # 5. Apply our custom Tuned Threshold (0.4) from Week 1!
    prediction = 1 if probability >= 0.4 else 0
    
    return prediction, probability

# The Test Switch
if __name__ == "__main__":
    # Let's invent a fake customer who is very unhappy
    fake_customer = {
        "tenure": 2,
        "MonthlyCharges": 95.0,
        "TotalCharges": 190.0,
        "gender": "Female",
        "SeniorCitizen": 0,
        "Partner": "No",
        "Dependents": "No",
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "Fiber optic",
        "OnlineSecurity": "No",
        "OnlineBackup": "No",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "Yes",
        "StreamingMovies": "Yes",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check"
    }
    
    print("Testing Prediction Machine...")
    pred, prob = predict_churn(fake_customer)
    
    print(f"Risk Score: {prob:.2f} ({(prob*100):.0f}%)")
    if pred == 1:
        print("ALERT: This customer is highly likely to CHURN.")
    else:
        print("SAFE: This customer is likely to STAY.")