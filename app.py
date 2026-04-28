# app.py (MULTI-MODULE PROFESSIONAL DASHBOARD)

import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load model
model = joblib.load("fraud_model.pkl")

# Page config
st.set_page_config(page_title="Financial Fraud Detection System", layout="wide")

# Title
st.title("💸 Financial Fraud Detection Dashboard")

# Sidebar module selection
st.sidebar.title("📂 Select Module")

module = st.sidebar.selectbox(
    "Choose Financial Module",
    [
        "Credit Card Fraud Detection",
        "Loan Default Prediction",
        "Customer Risk Scoring",
        "Transaction Anomaly Detection",
        "Spending Pattern Clustering"
    ]
)

# -------------------------
# CREDIT CARD FRAUD
# -------------------------
if module == "Credit Card Fraud Detection":

    st.header("💳 Credit Card Fraud Detection")

    amount = st.sidebar.number_input("Transaction Amount", min_value=0.0, value=1000.0)
    time = st.sidebar.slider("Transaction Hour", 0, 23, 12)
    location = st.sidebar.slider("Location Code", 1, 10, 1)
    merchant = st.sidebar.slider("Merchant Code", 1, 10, 1)

    input_data = pd.DataFrame({
        "amount": [amount],
        "time": [time],
        "location": [location],
        "merchant": [merchant]
    })

    st.write("### Entered Transaction Data")
    st.write(input_data)

    if st.button("Predict Fraud Status"):

        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0]

        genuine_prob = probability[0] * 100
        fraud_prob = probability[1] * 100

        if prediction == 1:
            st.error(f"🚨 Fraudulent Transaction Detected! Fraud Probability: {fraud_prob:.2f}%")
        else:
            st.success(f"✅ Genuine Transaction. Genuine Probability: {genuine_prob:.2f}%")

        labels = ["Genuine", "Fraud"]
        values = [genuine_prob, fraud_prob]

        fig, ax = plt.subplots()
        ax.bar(labels, values)
        ax.set_ylabel("Probability (%)")
        ax.set_title("Fraud Detection Analysis")
        st.pyplot(fig)

# -------------------------
# LOAN DEFAULT
# -------------------------
elif module == "Loan Default Prediction":

    st.header("🏦 Loan Default Prediction")

    income = st.sidebar.number_input("Monthly Income", min_value=0)
    loan_amount = st.sidebar.number_input("Loan Amount", min_value=0)
    credit_score = st.sidebar.slider("Credit Score", 300, 900, 650)

    risk = "High Risk" if credit_score < 500 or loan_amount > income * 10 else "Low Risk"

    if st.button("Predict Loan Status"):
        if risk == "High Risk":
            st.error("🚨 High Chance of Loan Default")
        else:
            st.success("✅ Low Risk Customer")

# -------------------------
# CUSTOMER RISK
# -------------------------
elif module == "Customer Risk Scoring":

    st.header("📊 Customer Risk Scoring")

    missed_payments = st.sidebar.slider("Missed Payments", 0, 20, 2)
    credit_score = st.sidebar.slider("Credit Score", 300, 900, 650)

    score = (missed_payments * 5) + (700 - credit_score)

    if st.button("Generate Risk Score"):
        st.warning(f"⚠️ Customer Risk Score: {score}")

# -------------------------
# ANOMALY DETECTION
# -------------------------
elif module == "Transaction Anomaly Detection":

    st.header("🔎 Transaction Anomaly Detection")

    amount = st.sidebar.number_input("Transaction Amount", min_value=0)

    if st.button("Detect Anomaly"):
        if amount > 25000:
            st.error("🚨 Suspicious Transaction Detected")
        else:
            st.success("✅ Normal Transaction")

# -------------------------
# SPENDING CLUSTERING
# -------------------------
elif module == "Spending Pattern Clustering":

    st.header("📈 Spending Pattern Clustering")

    monthly_spend = st.sidebar.number_input("Monthly Spending", min_value=0)

    if st.button("Analyze Spending"):
        if monthly_spend < 5000:
            st.success("💰 Saver Category")
        elif monthly_spend < 20000:
            st.warning("🛒 Moderate Spender")
        else:
            st.error("🔥 High Spender")