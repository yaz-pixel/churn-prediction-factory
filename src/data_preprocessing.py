import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_clean_data(filepath):
    """Loads the CSV and fixes the TotalCharges and Null values."""
    print("Loading and cleaning data...")
    df = pd.read_csv(filepath)
    
    # Fix the trap we found in Week 1
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df = df.dropna()
    df = df.drop(columns=['customerID'])
    
    return df

def split_and_encode_data(df):
    """Splits data into train/test and applies One-Hot Encoding."""
    print("Splitting and encoding data...")
    X = df.drop(columns=['Churn'])
    y = df['Churn'].map({'Yes': 1, 'No': 0})
    
    # Study material (Train) and Exam material (Test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Convert text to numbers
    X_train_encoded = pd.get_dummies(X_train)
    X_test_encoded = pd.get_dummies(X_test)
    
    # Align the columns to prevent errors
    X_train_encoded, X_test_encoded = X_train_encoded.align(
        X_test_encoded, join='left', axis=1, fill_value=0
    )
    
    return X_train_encoded, X_test_encoded, y_train, y_test

# This is the "Test Switch"
if __name__ == "__main__":
    # If we run this script directly, test the machines
    raw_data = load_and_clean_data('../data/data.csv')
    X_train, X_test, y_train, y_test = split_and_encode_data(raw_data)
    
    print(f"Success! Training data shape is now: {X_train.shape}")