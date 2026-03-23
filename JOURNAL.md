# Engineering Journal - Churn Prediction Project

## Day 1: Setup & Planning
- Created project structure (src, data, notebooks).
- Learned about Virtual Environments (venv) to isolate dependencies.
- Metric chosen: Recall (because missing a churner is expensive).

## Day 2: Data Exploration (EDA)
- **Goal:** Find out if the data is clean.
- **Findings:**
    - Dataset size: 7,043 Rows.
    - Churn Rate: ~26.5% (Imbalanced Dataset).
    - TotalCharges column: Was 'Object' (String). Converted to 'Float'. Found 11 missing values.
## Day 6 & 7: Tuning & Saving
- **Model Selection:** Balanced Logistic Regression outperformed Random Forest.
- **Threshold Tuning:** Lowering threshold to 0.4 increased Recall to **86%**.
- **Final Result:** Saved model to `models/churn_model.pkl`.


## Week 2: Engineering & Migration
- **Goal:** Move Machine Learning logic from Jupyter Notebooks into production-ready Python scripts.
- **Accomplishments:**
  - Built `data_preprocessing.py`: Extracted data loading, cleaning, and one-hot encoding logic into reusable functions.
  - Built `train.py`: Automated model training (Balanced Logistic Regression) and saved the brain as `churn_model.pkl`.
  - Built `predict.py`: Created an inference engine that takes a single customer profile, aligns the columns, and outputs a Risk Score.
- **Result:** Code is now modular, automated, and ready to be wrapped in a Web API.

### Deployment & Containerization
- **Containerized the API:** Created a `Dockerfile` to package the Python environment, libraries, and model artifacts.
- **Fixed Pathing Issues:** Resolved `ModuleNotFoundError` by adjusting the `WORKDIR` within the container layers.
- **Ensured Consistency:** Used `--no-cache` builds to verify the environment is reproducible from scratch.
- **Validated Connectivity:** Successfully mapped Port 8000 from the local machine to the Docker container to access the FastAPI Swagger UI.

**Result:** The model is now a production-ready microservice.