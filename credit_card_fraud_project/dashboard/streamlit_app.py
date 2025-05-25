# streamlit_app.py — Advanced Credit Card Fraud Detection Dashboard

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, roc_auc_score, roc_curve

st.set_page_config(page_title="Fraud Detection Dashboard", layout="wide")

# --- Load Data ---
@st.cache_data
def load_data():
    return pd.read_csv("dashboard/flagged_transactions.csv")

df = load_data()

# --- Sidebar Filters ---
st.sidebar.header("Filter Predictions")
threshold = st.sidebar.slider("Prediction Probability Threshold", 0.0, 1.0, 0.5, 0.01)

filtered_df = df.copy()
if "probability" in df.columns:
    filtered_df = filtered_df[filtered_df["probability"] >= threshold]

st.sidebar.write(f"Showing {len(filtered_df):,} transactions above threshold")

# --- KPI Metrics ---
total_txns = len(df)
total_frauds = df["Predicted_Class"].sum()
fraud_pct = total_frauds / total_txns * 100 if total_txns > 0 else 0

col1, col2, col3 = st.columns(3)
col1.metric("Total Transactions", f"{total_txns:,}")
col2.metric("Predicted Frauds", f"{total_frauds:,}")
col3.metric("Fraud Rate", f"{fraud_pct:.2f}%")

# --- Visualizations ---
st.markdown("### 📊 Visual Insights")

col4, col5 = st.columns(2)

with col4:
    st.subheader("Fraud vs Non-Fraud")

    pie_data = df["Predicted_Class"].value_counts().sort_index()

    if pie_data.size < 2:
        st.warning("⚠️ Cannot plot pie chart — only one class (either all fraud or all non-fraud).")
    else:
        values = [pie_data.get(0, 0), pie_data.get(1, 0)]
        labels = ["Non-Fraud", "Fraud"]
        colors = ["#4caf50", "#e74c3c"]

        fig1, ax1 = plt.subplots()
        ax1.pie(values, labels=labels, autopct="%1.1f%%", startangle=90, colors=colors)
        ax1.axis("equal")
        st.pyplot(fig1)



with col5:
    if "probability" in df.columns:
        st.subheader("Probability Score Distribution")
        fig2, ax2 = plt.subplots()
        sns.histplot(df[df["Predicted_Class"] == 1]["probability"], kde=True, color="red", bins=20, ax=ax2)
        ax2.set_title("Predicted Fraud Probability")
        st.pyplot(fig2)

# --- Confusion Matrix (if available) ---
if "Actual_Class" in df.columns:
    st.subheader("Confusion Matrix")
    cm = confusion_matrix(df["Actual_Class"], df["Predicted_Class"])
    fig_cm, ax_cm = plt.subplots()
    sns.heatmap(cm, annot=True, fmt='d', cmap="Blues", xticklabels=["Non-Fraud", "Fraud"], yticklabels=["Non-Fraud", "Fraud"])
    st.pyplot(fig_cm)

# --- Flagged Transactions Table ---
st.markdown("### 🧾 Flagged Transactions")
st.dataframe(filtered_df, use_container_width=True)

# --- File Download ---
st.download_button("📥 Download Filtered CSV", data=filtered_df.to_csv(index=False), file_name="flagged_frauds_filtered.csv")

# --- ROC Curve (if available) ---
if "probability" in df.columns and "Actual_Class" in df.columns:
    st.subheader("ROC Curve")
    fpr, tpr, _ = roc_curve(df["Actual_Class"], df["probability"])
    auc = roc_auc_score(df["Actual_Class"], df["probability"])
    fig_roc, ax_roc = plt.subplots()
    ax_roc.plot(fpr, tpr, label=f"AUC = {auc:.2f}")
    ax_roc.plot([0, 1], [0, 1], linestyle='--')
    ax_roc.set_xlabel("False Positive Rate")
    ax_roc.set_ylabel("True Positive Rate")
    ax_roc.set_title("ROC Curve")
    ax_roc.legend()
    st.pyplot(fig_roc)

st.caption("📌 Built with ❤️ by Mukaila Adesina — Real-time Credit Card Fraud Detection Dashboard")


