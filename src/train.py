import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Look at this! We are importing your OWN custom functions!
from data_preprocessing import load_and_clean_data, split_and_encode_data

def train_and_save_model(X_train, y_train, X_test, y_test):
    """Trains the model, evaluates it, and saves it to the models folder."""
    print("Training Balanced Logistic Regression model...")
    # This is the winning model from Week 1
    model = LogisticRegression(max_iter=2000, class_weight='balanced')
    model.fit(X_train, y_train)
    
    print("Evaluating model...")
    y_pred = model.predict(X_test)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    
    print("Saving model to ../models/churn_model.pkl...")
    model_data = {
        'model': model,
        'features': X_train.columns.tolist()
    }
    joblib.dump(model_data, '../models/churn_model.pkl')
    print("Model saved successfully!")

# The Test Switch
if __name__ == "__main__":
    # 1. Get the data
    raw_data = load_and_clean_data('../data/data.csv')
    X_train, X_test, y_train, y_test = split_and_encode_data(raw_data)
    
    # 2. Train and save the model
    train_and_save_model(X_train, y_train, X_test, y_test)