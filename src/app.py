import streamlit as st
import requests

# 1. Page Configuration
st.set_page_config(page_title="Customer Churn Predictor", layout="centered")

# 2. Header Section
st.title("🛡️ Customer Churn Prediction Dashboard")
st.write("Enter the customer details below to calculate the risk of them leaving the service.")

st.divider()

# 3. Input Form
with st.form("customer_form"):
    st.subheader("Customer Profile")
    
    # Create two columns for a cleaner look
    col1, col2 = st.columns(2)
    
    with col1:
        tenure = st.number_input("Tenure (Months)", min_value=0, max_value=100, value=12)
        contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
        monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, value=50.0)

    with col2:
        internet_service = st.selectbox("Internet Service", ["Fiber optic", "DSL", "No"])
        tech_support = st.selectbox("Has Tech Support?", ["Yes", "No", "No internet service"])
        payment_method = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])

    # The Submit Button
    submitted = st.form_submit_button("Analyze Customer Risk")



# 4. Results Placeholder & API Call
if submitted:
    st.info(f"Analyzing data for customer with {tenure} months tenure...")
    
    # THE BRIDGE: Build the exact dictionary Pydantic expects
    # We use the UI inputs for the first 6, and hardcode defaults for the rest
    customer_data = {
        "tenure": tenure,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": monthly_charges * tenure, # Rough estimate for our UI
        "gender": "Female", 
        "SeniorCitizen": 0,
        "Partner": "No",
        "Dependents": "No",
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": internet_service,
        "OnlineSecurity": "No",
        "OnlineBackup": "No",
        "DeviceProtection": "No",
        "TechSupport": tech_support,
        "StreamingTV": "Yes",
        "StreamingMovies": "Yes",
        "Contract": contract,
        "PaperlessBilling": "Yes",
        "PaymentMethod": payment_method
    }
    
    # Send it to the Docker API!
    try:
        # We send a POST request to your local Docker container
        response = requests.post("https://churn-prediction-factory.onrender.com/predict", json=customer_data)
        response.raise_for_status() # Check for network errors
        
        # Unpack the response from the API
        result = response.json()
        risk_score = result['risk_score'] * 100
        
        # Display the results to the user!
        if result['prediction'] == 1:
            st.error(f"🚨 HIGH RISK CHURN! Risk Score: {risk_score:.0f}%")
        else:
            st.success(f"✅ SAFE. Customer is likely to stay. Risk Score: {risk_score:.0f}%")
            
    except Exception as e:
        st.error(f"Could not connect to the API. Is your Docker container running? Error: {e}")