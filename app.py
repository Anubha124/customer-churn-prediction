import streamlit as st
import requests

st.title("Customer Churn Prediction Dashboard")

tenure = st.number_input(
    "Tenure (Months)",
    min_value=0,
    value=12
)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=75.5
)

contract = st.selectbox(
    "Contract Type",
    [
        "Month-to-month",
        "One year",
        "Two year"
    ]
)

internet_service = st.selectbox(
    "Internet Service",
    [
        "DSL",
        "Fiber optic",
        "No"
    ]
)

online_security = st.selectbox(
    "Online Security",
    [
        "Yes",
        "No",
        "No internet service"
    ]
)

tech_support = st.selectbox(
    "Tech Support",
    [
        "Yes",
        "No",
        "No internet service"
    ]
)

partner = st.selectbox(
    "Partner",
    [
        "Yes",
        "No"
    ]
)

dependents = st.selectbox(
    "Dependents",
    [
        "Yes",
        "No"
    ]
)

paperless_billing = st.selectbox(
    "Paperless Billing",
    [
        "Yes",
        "No"
    ]
)

payment_method = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

if st.button("Predict Churn"):

    data = {
        "tenure": int(tenure),
        "monthly_charges": float(monthly_charges),
        "contract": contract,
        "internet_service": internet_service,
        "online_security": online_security,
        "tech_support": tech_support,
        "partner": partner,
        "dependents": dependents,
        "paperless_billing": paperless_billing,
        "payment_method": payment_method
    }

    response = requests.post(
    "https://customer-churn-prediction-wgro.onrender.com/predict",
    json=data
    )

    result = response.json()

    prediction = result["prediction"]
    probability = result["churn_probability_percent"]

    st.subheader("Prediction Result")

    if prediction == "Will Churn":
        st.error("⚠️ High Risk Customer")
    else:
        st.success("✅ Low Risk Customer")

    st.write("Prediction:", prediction)
    st.write("Churn Probability:", f"{probability}%")

    st.progress(min(int(probability), 100))

    if probability >= 70:
        st.warning(
            "Customer has a high churn risk. Consider retention offers or proactive engagement."
        )
    elif probability >= 40:
        st.info(
            "Customer has a moderate churn risk. Monitor engagement and satisfaction."
        )
    else:
        st.success(
            "Customer has a low churn risk."
        )