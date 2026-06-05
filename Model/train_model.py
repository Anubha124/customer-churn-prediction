import joblib
from sklearn.linear_model import LogisticRegression
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

df = df[[
    "tenure",
    "MonthlyCharges",
    "Contract",
    "InternetService",
    "OnlineSecurity",
    "TechSupport",
    "Partner",
    "Dependents",
    "PaperlessBilling",
    "PaymentMethod",
    "Churn"
]]

X = df.drop("Churn", axis=1)
y = df["Churn"]

categorical_features = [
    "Contract",
    "InternetService",
    "OnlineSecurity",
    "TechSupport",
    "Partner",
    "Dependents",
    "PaperlessBilling",
    "PaymentMethod"
]

numeric_features = [
    "tenure",
    "MonthlyCharges"
]

preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ],
    remainder="passthrough"
)

from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", LogisticRegression(max_iter=1000))
    ]
)

pipeline.fit(X_train, y_train)

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

predictions = pipeline.predict(X_test)

print("Accuracy :", accuracy_score(y_test, predictions))
print("Precision:", precision_score(y_test, predictions, pos_label="Yes"))
print("Recall   :", recall_score(y_test, predictions, pos_label="Yes"))
print("F1 Score :", f1_score(y_test, predictions, pos_label="Yes"))

joblib.dump(pipeline, "saved_model/churn_pipeline.pkl")

print("Pipeline saved!")