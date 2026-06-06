# Customer Churn Prediction System

## Overview

An end-to-end Machine Learning project that predicts customer churn using customer demographics, service information, and billing details.

The project includes:

* Machine Learning Pipeline
* Logistic Regression Model
* FastAPI REST API
* Streamlit Dashboard
* Probability-based Churn Prediction

---

## Features

* Predict customer churn risk
* Churn probability score
* Real-time predictions using FastAPI
* Interactive Streamlit dashboard
* Automated preprocessing pipeline using Scikit-Learn

---

## Tech Stack

* Python
* Pandas
* Scikit-Learn
* FastAPI
* Streamlit
* Joblib

---

## Model Performance

| Metric    | Score  |
| --------- | ------ |
| Accuracy  | 81.69% |
| Precision | 68.85% |
| Recall    | 56.30% |
| F1 Score  | 61.95% |

---

## Project Architecture

User Input

↓

Streamlit Dashboard

↓

FastAPI API

↓

Machine Learning Pipeline

↓

Logistic Regression Model

↓

Prediction + Probability

---

## API Endpoints

### Home

GET /

### Model Information

GET /model-info

### Churn Prediction

POST /predict

---

## Sample Prediction Response

```json
{
  "prediction": "Will Churn",
  "churn_probability_percent": 54.53
}
```

---

## Future Improvements

* Docker Deployment
* Cloud Deployment
* SHAP Explainability
* Advanced Model Comparison
* Real-Time Monitoring

---

## Author

Anubha Khatri
