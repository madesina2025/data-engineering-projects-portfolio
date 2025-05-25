import os
import pandas as pd
import joblib
from datetime import timedelta
from dash import Dash, dcc, html, dash_table, Input, Output
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import plotly.express as px
import plotly.graph_objects as go

# Load data
X_test = pd.read_csv("/app/data/X_test.csv")
y_test = pd.read_csv("/app/data/y_test.csv").values.ravel()
transactions = pd.read_csv("/app/dashboard/flagged_transactions.csv")

# Generate synthetic datetime from 'Time'
if "Time" in transactions.columns:
    transactions["date"] = pd.to_datetime("2023-01-01") + pd.to_timedelta(transactions["Time"], unit='s')
else:
    transactions["date"] = pd.to_datetime("2023-01-01")

# Evaluate models
model_dir = "/app/models_all"
results = []
for file in os.listdir(model_dir):
    if file.endswith(".pkl"):
        model_name = file.replace("_fraud_model.pkl", "").replace("_", " ").title()
        model_path = os.path.join(model_dir, file)
        model = joblib.load(model_path)
        y_pred = model.predict(X_test)
        tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
        results.append({
            "Model": model_name,
            "Accuracy (%)": round(accuracy_score(y_test, y_pred) * 100, 2),
            "Precision (%)": round(precision_score(y_test, y_pred) * 100, 2),
            "Recall (%)": round(recall_score(y_test, y_pred) * 100, 2),
            "F1 Score (%)": round(f1_score(y_test, y_pred) * 100, 2),
            "TN": tn, "FP": fp, "FN": fn, "TP": tp
        })

summary_df = pd.DataFrame(results)

# Initialize Dash app
app = Dash(__name__)
app.title = "Credit Card Fraud Dashboard"

app.layout = html.Div([
    html.H1("Credit Card Fraud Detection Dashboard", style={"textAlign": "center", "color": "#003366"}),

    html.Div([
        html.Label("Select Model:"),
        dcc.Dropdown(
            options=[{"label": m, "value": m} for m in summary_df["Model"]],
            value=None,
            id="model-filter",
            placeholder="Select model"
        ),

        html.Label("Date Range:"),
        dcc.DatePickerRange(
            id="date-filter",
            min_date_allowed=transactions["date"].min(),
            max_date_allowed=transactions["date"].max(),
            start_date=transactions["date"].min(),
            end_date=transactions["date"].max()
        ),

        html.Label("Probability Threshold:"),
        dcc.Slider(
            id="threshold-filter",
            min=0.0,
            max=1.0,
            step=0.01,
            value=0.5,
            marks={0.0: "0.0", 0.5: "0.5", 1.0: "1.0"}
        )
    ], style={"width": "80%", "margin": "auto"}),

    html.H3("Model Performance Summary", style={"textAlign": "center"}),
    dash_table.DataTable(
        id="performance-table",
        columns=[{"name": i, "id": i} for i in summary_df.columns],
        data=summary_df.to_dict("records"),
        style_table={"overflowX": "auto"},
        style_cell={"textAlign": "center"},
        style_header={"backgroundColor": "black", "color": "white"},
        page_size=10
    ),

    html.Br(),
    html.Div([
        dcc.Graph(id="class-dist"),
        dcc.Graph(id="fraud-trend"),
        dcc.Graph(id="conf-matrix"),
        html.Div(id="fraud-loss-summary", style={"textAlign": "center", "fontSize": 20, "color": "#990000"}),
        html.Button("Download Filtered Data", id="download-btn"),
        dcc.Download(id="download-data")
    ], style={"width": "90%", "margin": "auto"})
])

@app.callback(
    Output("class-dist", "figure"),
    Output("fraud-trend", "figure"),
    Output("conf-matrix", "figure"),
    Output("fraud-loss-summary", "children"),
    Output("download-data", "data"),
    Input("model-filter", "value"),
    Input("date-filter", "start_date"),
    Input("date-filter", "end_date"),
    Input("threshold-filter", "value"),
    Input("download-btn", "n_clicks")
)
def update_dashboard(model_name, start_date, end_date, threshold, n_clicks):
    df_filtered = transactions.copy()
    if model_name:
        df_filtered = df_filtered[df_filtered["model_name"] == model_name]
    df_filtered = df_filtered[
        (df_filtered["date"] >= pd.to_datetime(start_date)) &
        (df_filtered["date"] <= pd.to_datetime(end_date)) &
        (df_filtered["probability"] >= threshold)
    ]

    if not df_filtered.empty and "Predicted_Class" in df_filtered.columns and "Actual_Class" in df_filtered.columns:
        class_fig = px.histogram(df_filtered, x="Predicted_Class", color="Actual_Class", barmode="group")
        fraud_trend = df_filtered[df_filtered["Predicted_Class"] == 1].groupby(df_filtered["date"].dt.date)["Amount"].sum()
        trend_fig = px.line(fraud_trend, title="Fraud Amount Over Time")

        cm = confusion_matrix(df_filtered["Actual_Class"], df_filtered["Predicted_Class"])
        cm_fig = go.Figure(data=go.Heatmap(z=cm, x=["Not Fraud", "Fraud"],
                                           y=["Not Fraud", "Fraud"], colorscale="Blues"))
        cm_fig.update_layout(title="Confusion Matrix")

        total_loss = df_filtered[df_filtered["Predicted_Class"] == 1]["Amount"].sum()
        loss_summary = f"Total Fraud Amount Flagged: ${total_loss:,.2f}"
    else:
        class_fig = trend_fig = cm_fig = go.Figure()
        loss_summary = "No data available for selected filters."

    download = dcc.send_data_frame(df_filtered.to_csv, "filtered_fraud.csv") if n_clicks else None
    return class_fig, trend_fig, cm_fig, loss_summary, download

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
