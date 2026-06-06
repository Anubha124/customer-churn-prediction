🔍 Customer Churn Prediction System

Predicting which customers will leave — before they do.
An end-to-end ML system with a REST API and interactive dashboard, built to solve one of the most expensive problems in any subscription business.


The Business Problem
Every month, businesses lose customers silently. By the time churn shows up in a report, it's already too late to act. The real question isn't "who left?" — it's "who is about to?"
This project answers that question. Given a customer's demographics, service usage, and billing behaviour, the system predicts churn probability in real time — giving business teams a 30-day window to intervene before revenue walks out the door.

Live Demo
ComponentLink🖥️ Streamlit Dashboard[Add your Streamlit URL here]⚡ FastAPI Endpoint[Add your API URL here]📓 Notebook Walkthrough[Link to .ipynb in repo]

What This System Does
Customer Profile Input
        ↓
Streamlit Dashboard  ←——  Human-friendly interface for business users
        ↓
FastAPI REST API     ←——  Real-time prediction endpoint (POST /predict)
        ↓
ML Pipeline          ←——  Automated preprocessing + feature encoding
        ↓
Logistic Regression  ←——  Trained on 7,000+ customer records
        ↓
Churn Probability    ←——  e.g. "54.5% likelihood of churn"

Model Performance
MetricScoreWhat It MeansAccuracy81.69%Correct overall prediction 4 out of 5 timesPrecision68.85%When model flags churn, it's right ~7 in 10 timesRecall56.30%Catches over half of all actual churnersF1 Score61.95%Balanced score on an imbalanced dataset

Context: The dataset is imbalanced (~27% churn rate). Optimising for recall is the business-correct choice here — missing a churner costs more than a false alarm.


Key Features

Probability-based scoring — not just "will churn / won't churn" but a risk percentage, so teams can prioritise high-risk customers
REST API — predictions available programmatically via POST /predict, enabling integration into CRM tools or dashboards
Interactive dashboard — business users can input any customer profile and get instant results without touching code
Automated preprocessing pipeline — consistent feature encoding and scaling via Scikit-Learn Pipeline, reducing human error


API Reference
GET /
Health check — confirms API is live.
GET /model-info
Returns model metadata: algorithm, features used, training accuracy.
POST /predict
Accepts customer profile, returns churn prediction + probability.
Sample request:
json{
  "tenure": 12,
  "MonthlyCharges": 65.5,
  "Contract": "Month-to-month",
  "PaymentMethod": "Electronic check",
  "InternetService": "Fiber optic"
}
Sample response:
json{
  "prediction": "Will Churn",
  "churn_probability_percent": 54.53
}

Tech Stack
LayerTechnologyData ProcessingPython, PandasMachine LearningScikit-Learn, Logistic RegressionAPI LayerFastAPIFrontendStreamlitModel SerialisationJoblib

Project Structure
customer-churn-prediction/
│
├── data/
│   └── telco_churn.csv          # Raw dataset
│
├── notebooks/
│   └── churn_analysis.ipynb     # EDA + model training walkthrough
│
├── model/
│   └── churn_pipeline.joblib    # Serialised ML pipeline
│
├── api/
│   └── main.py                  # FastAPI app
│
├── dashboard/
│   └── app.py                   # Streamlit dashboard
│
├── requirements.txt
└── README.md

How to Run Locally
1. Clone the repo
bashgit clone https://github.com/Anubha124/customer-churn-prediction.git
cd customer-churn-prediction
2. Install dependencies
bashpip install -r requirements.txt
3. Start the API
bashuvicorn api.main:app --reload
4. Launch the dashboard
bashstreamlit run dashboard/app.py

What I'd Improve With More Time

 SHAP explainability — show which features drove each individual prediction
 XGBoost / Random Forest comparison — benchmark against tree-based models to improve recall
 Docker containerisation — single-command deployment
 Cloud deployment — host on AWS / GCP for persistent availability
 Real-time monitoring — track prediction drift over time with Evidently AI


Key Insight

Month-to-month contract customers on electronic check payments showed the highest churn rates in the dataset — consistent with real-world telco behaviour where payment friction and low commitment drive exit.


Author
Anubha Khatri
Data Analyst | ML Enthusiast | KIIT '26
LinkedIn · GitHub
