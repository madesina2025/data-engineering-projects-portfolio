
# 🛡️ Credit Card Fraud Detection Dashboard

A full end-to-end machine learning project for detecting fraudulent transactions using multiple models, real-time visual insights, and containerized deployment.

## Project Overview

This project demonstrates a complete fraud detection pipeline built with Python, Scikit-learn, Plotly Dash, and Docker. It includes:

- Data preprocessing and handling class imbalance
- Model training and evaluation (XGBoost, Random Forest, Logistic Regression, etc.)
- Saving the best model as `.pkl` for inference
- Real-time fraud flagging with probability thresholds
- Interactive Dash dashboard for monitoring predictions
- Dockerized setup for portable deployment


## ⚙️ Features

✅ Multiple ML model training and evaluation 
✅ Confusion matrix, ROC, Precision, Recall, and F1-score 
✅ Visual fraud trends and class distribution 
✅ Probability threshold filter and date range selector 
✅ Downloadable filtered fraud data 
✅ Easily deployable using Docker Compose 


## Getting Started

	### 1. Clone the Repository

```bash
git clone https://github.com/madesina2025/data-projects-portfolio.git
cd credit_card_fraud_project

### 2. Build and Run with Docker
docker-compose up --build

Then visit: http://localhost:8050

| Class Distribution          | Fraud Trends Over Time       |
| --------------------------- | ---------------------------- |
| ![](reports/class_dist.png) | ![](reports/fraud_trend.png) |


📦 Dependencies
Python 3.10+

Scikit-learn

XGBoost

Pandas, NumPy

Plotly, Dash

Docker & Docker Compose


📁 Notes
Large files (e.g., full datasets, model binaries) are excluded from GitHub. You can generate them using the provided notebook or scripts.

Git LFS is recommended if you want to version-control large files.

✍️ Author
Mukaila Adesina
📫 GitHub | 🧠 MSc Data Science & Analytics | 🇬🇧 UK-Based Data Engineer

📃 License
MIT License – see LICENSE.md for details.


Would you like me to save this as a `README.md` file in your project or modify it for GitHub Pages presentation?




||||||| parent of 28255511 (Add README.md to project)


# Credit Card Fraud Detection Project

This is a complete end-to-end project for detecting fraudulent credit card transactions using machine learning. It includes data preprocessing, training multiple models, evaluating performance, real-time inference setup, and dashboards for monitoring results.

## Project Structure


credit_card_fraud_project/
├── data/                    # Raw and processed datasets (ignored in GitHub)
├── models_all/              # Trained models
├── dashboard/               # Dash (Python) dashboard files
├── Dockerfile               # Docker configuration for containerized setup
├── docker-compose.yml       # Docker orchestration
├── dash_app.py              # Main dashboard app
├── requirements.txt         # Python dependencies
└── CreditcardFraud_ML.ipynb # Full exploratory notebook


## Key Features

- Preprocessing and class balancing using SMOTE
- Trained models: Logistic Regression, Random Forest, SVM, KNN, Naive Bayes, XGBoost
- Evaluation metrics: Accuracy, Recall, Precision, F1, AUC
- Real-time scoring API ready via Docker
- Interactive dashboard with filters, plots, confusion matrix, and fraud trends
- Downloadable filtered predictions for BI use (Power BI/Tableau)

## 🐳 Run with Docker

```bash
docker-compose up --build
```

Then navigate to `http://localhost:8050` in your browser to use the dashboard.

## Dashboard Features

- Model Performance Summary
- Confusion Matrix
- Class Distribution
- Fraud Trends Over Time
- Fraud Loss Amount
- Filters: Model selection, date range, threshold slider
- CSV Download Button

## 📦 Requirements

- Python 3.10+
- Dash / Plotly / scikit-learn / pandas / joblib
- Docker + Docker Compose

## 🧠 Future Enhancements

- Integrate Kafka for live streaming
- Add Explainable AI (SHAP)
- Upload to Streamlit Cloud / Heroku / GCP for public demo



> **Author:** Mukaila Adesina  
> **Repo:** [GitHub Portfolio](https://github.com/madesina2025/data-projects-portfolio)

