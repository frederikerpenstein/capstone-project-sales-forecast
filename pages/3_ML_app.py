import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import xgboost as xgb
from sklearn.metrics import mean_squared_log_error

# Load the test dataset (for demonstration, simulate loading the processed CSV)
df_test = pd.read_csv('notebooks/df_test_pred.csv')  # Assuming this is the saved output with predictions

# Display basic information to users
st.title("Sales Prediction Dashboard")

st.markdown("""
Welcome to the sales prediction dashboard. This tool allows you to view the predictions of our sales forecasting model.
Below, you'll find visualizations comparing actual and predicted sales, as well as insights into which factors were most influential in making these predictions.
""")

# 1. Sales Prediction Plot (Actual vs. Predicted Sales)
st.header("Sales Prediction vs. Actual Sales")

# Assuming df_test contains columns 'transactions', 'sales' (actual) and 'sales_pred' (predicted)
fig = go.Figure()
fig.add_trace(go.Scatter(x=df_test['transactions'], y=df_test['sales'], mode='markers', name='Actual Sales', marker=dict(color='red')))
fig.add_trace(go.Scatter(x=df_test['transactions'], y=df_test['sales_pred'], mode='markers', name='Predicted Sales', marker=dict(color='green')))

# Calculate Mean Squared Log Error (MSLE)
msle = mean_squared_log_error(df_test['sales'], df_test['sales_pred'])

fig.update_layout(
    title='Sales Prediction vs Actual Sales',
    xaxis_title='Transactions',
    yaxis_title='Sales',
    annotations=[go.layout.Annotation(x=40, y=df_test['sales'].max(), 
                                      text=f"Mean Squared Log Error (MSLE): {msle:.4f}",
                                      showarrow=False)]
)

st.plotly_chart(fig)

# 2. Feature Importance Plot
st.header("Top Features Influencing Sales Predictions")

# Simulate feature importance data (assuming this is generated from the XGBoost model)
# Here, we're assuming some feature importances; replace this with actual values from the model if available
feature_importances = {
    'transactions': 0.45,
    'oil_price': 0.25,
    'store_type': 0.15,
    'holiday': 0.10,
    'promo': 0.05
}

# Create a bar chart using Plotly Express
importance_fig = px.bar(
    x=list(feature_importances.keys()), 
    y=list(feature_importances.values()), 
    labels={'x': 'Feature', 'y': 'Importance'},
    title="Feature Importances"
)

st.plotly_chart(importance_fig)

# 3. Data Preview (Actual and Predicted Sales)
st.header("Sample Data (Actual vs. Predicted Sales)")

# Display the first few rows of the dataset for clarity
st.dataframe(df_test[['date', 'store_nbr', 'sales', 'sales_pred']].head())

st.markdown("This table shows a sample of the actual sales alongside the model's predictions. The model uses transaction data, store information, and other factors to make these predictions.")

# Final message
st.write("This dashboard is a simple overview of the model's performance and key insights.")
