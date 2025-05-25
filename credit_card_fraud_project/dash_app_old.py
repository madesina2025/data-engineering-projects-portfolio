# dash_app.py - Credit Card Fraud Dashboard (Dash Version)

import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

# Load filtered fraud data
df = pd.read_csv("dashboard/flagged_transactions.csv")

app = Dash(__name__)
app.title = "Fraud Detection Dashboard"

# KPI Metrics
total = len(df)
frauds = df["Predicted_Class"].sum()
fraud_rate = (frauds / total) * 100 if total > 0 else 0

app.layout = html.Div([
    html.H1("📊 Credit Card Fraud Detection Dashboard", style={"textAlign": "center"}),

    html.Div([
        html.Div([
            html.H3("Total Transactions"),
            html.P(f"{total:,}")
        ], style={"padding": 10, "width": "30%", "display": "inline-block"}),

        html.Div([
            html.H3("Predicted Frauds"),
            html.P(f"{frauds:,}")
        ], style={"padding": 10, "width": "30%", "display": "inline-block"}),

        html.Div([
            html.H3("Fraud Rate"),
            html.P(f"{fraud_rate:.2f}%")
        ], style={"padding": 10, "width": "30%", "display": "inline-block"})
    ]),

    html.Hr(),

    dcc.Graph(
        id='fraud-distribution',
        figure=px.pie(
            df,
            names='Predicted_Class',
            title='Fraud vs Non-Fraud',
            color='Predicted_Class',
            color_discrete_map={0: "green", 1: "red"},
            category_orders={"Predicted_Class": [0, 1]},
        ).update_traces(pull=[0, 0.1])
    ),

    html.Hr(),

    dcc.Graph(
        id='fraud-amount-histogram',
        figure=px.histogram(
            df[df["Predicted_Class"] == 1],
            x="Amount",
            nbins=50,
            title="Fraud Amount Distribution",
            color_discrete_sequence=["crimson"]
        )
    )
])

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8050, debug=True)	
