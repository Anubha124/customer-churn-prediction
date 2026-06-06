# 🔍 Customer Churn Prediction System

> **Predicting which customers will leave — before they do.**  
> An end-to-end ML system with a REST API and interactive dashboard, built to solve one of the most expensive problems in any subscription business.

---

## The Business Problem

Every month, businesses lose customers silently. By the time churn shows up in a report, it's already too late to act. The real question isn't *"who left?"* — it's *"who is about to?"*

This project answers that question. Given a customer's demographics, service usage, and billing behaviour, the system predicts churn probability in real time — giving business teams a 30-day window to intervene before revenue walks out the door.

---

## Live Demo

| Component | Link |
|-----------|------|
| 🖥️ Streamlit Dashboard | [Live App ↗](https://customer-churn-prediction-g3w38kmknzhvu4porydhpv.streamlit.app/) |
| ⚡ FastAPI Endpoint | Coming soon — deploying to Render |
| 📓 Notebook Walkthrough | [View in Repo ↗](https://github.com/Anubha124/customer-churn-prediction/tree/main/Model) |

---

## What This System Does

```
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
```

---

## Model Performance

| Metric | Score | What It Means |
|--------|-------|---------------|
| Accuracy | 81.69% | Correct overall prediction 4 out of 5 times |
| Precision | 68.85% | When model flags churn, it's right ~7 in 10 times |
| Recall | 56.30% | Catches over half of all actual churners |
| F1 Score | 61.95% | Balanced score on an imbalanced dataset |

> **Context:** The dataset is imbalanced (~27% churn rate). Optimising for recall is the business-correct choice here — missing a churner costs more than a false alarm.

---

## Key Features

- **Probability-based scoring** — not just "will churn / won't churn" but a risk percentage, so teams can prioritise high-risk customers
- **REST API** — predictions available programmatically via `POST /predict`, enabling integration into CRM tools or dashboards
- **Interactive dashboard** — business users can input any customer profile and get instant results without touching code
- **Automated preprocessing pipeline** — consistent feature encoding and scaling via Scikit-Learn Pipeline, reducing human error

---

## API Reference

### `GET /`
Health check — confirms API is live.

### `GET /model-info`
Returns model metadata: algorithm, features used, training accuracy.

### `POST /predict`
Accepts customer profile, returns churn prediction + probability.

**Sample request:**
```json
{
  "tenure": 12,
  "MonthlyCharges": 65.5,
  "Contract": "Month-to-month",
  "PaymentMethod": "Electronic check",
  "InternetService": "Fiber optic"
}
```

**Sample response:**
```json
{
  "prediction": "Will Churn",
  "churn_probability_percent": 54.53
}
```

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Data Processing | Python, Pandas |
| Machine Learning | Scikit-Learn, Logistic Regression |
| API Layer | FastAPI |
| Frontend | Streamlit |
| Model Serialisation | Joblib |

---

## Project Structure

```
customer-churn-prediction/
│
├── Data/                        # Raw dataset
├── Model/                       # Training notebooks + model files
├── Saved_Model/                 # Serialised ML pipeline (.joblib)
├── api/                         # FastAPI app
│   └── main.py
├── app.py                       # Streamlit dashboard
├── requirements.txt
└── README.md
```

---

## How to Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/Anubha124/customer-churn-prediction.git
cd customer-churn-prediction
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Start the API**
```bash
uvicorn api.main:app --reload
```

**4. Launch the dashboard**
```bash
streamlit run app.py
```

---

## What I'd Improve With More Time

- [ ] **SHAP explainability** — show *which features* drove each individual prediction
- [ ] **XGBoost / Random Forest comparison** — benchmark against tree-based models to improve recall
- [ ] **Docker containerisation** — single-command deployment
- [ ] **Cloud deployment (Render / AWS)** — persistent public API endpoint
- [ ] **Real-time monitoring** — track prediction drift over time with Evidently AI

---

## Key Insight

> Month-to-month contract customers on electronic check payments showed the highest churn rates in the dataset — consistent with real-world telco behaviour where payment friction and low commitment drive exit.

---

## Author

**Anubha Khatri**  
Data Analyst | ML Enthusiast | KIIT '26  
[LinkedIn](https://www.linkedin.com/in/anubha-khatri-41b1b8392/) · [GitHub](https://github.com/Anubha124)
