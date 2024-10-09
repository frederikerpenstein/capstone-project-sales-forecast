import streamlit as st
import pandas as pd
import plotly.express as px

# Helper function to display dataset info
def display_data_overview(df):
    st.write("### Data Overview")
    st.write(df.head())
    st.write("### Summary Statistics")
    st.write(df.describe())
    st.write("### Missing Values")
    st.write(df.isnull().sum())

# Function for interactive visualizations
def visualize_data(df):
    st.write("### Visualizations")
    
    # Numeric columns
    numeric_columns = df.select_dtypes(include=['float', 'int']).columns.tolist()
    if numeric_columns:
        col = st.selectbox("Select a numeric column for histogram", numeric_columns)
        fig = px.histogram(df, x=col, title=f"Histogram of {col}")
        st.plotly_chart(fig)
    
    # Categorical columns
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns.tolist()
    if categorical_columns:
        col = st.selectbox("Select a categorical column for bar plot", categorical_columns)
        fig = px.bar(df, x=col, title=f"Bar Plot of {col}")
        st.plotly_chart(fig)

# Main app
def main():
    st.title("EDA App with Streamlit")
    
    # Sidebar for dataset selection
    st.sidebar.title("Options")
    dataset = st.sidebar.selectbox("Select Dataset", ["Holidays", "Oil", "Stores", "Test", "Train", "Transactions"])
    
    # Load the corresponding dataset
    if dataset == "Holidays":
        df = pd.read_csv("../data//holidays_events.csv")
    elif dataset == "Oil":
        df = pd.read_csv("../data//oil.csv")
    elif dataset == "Stores":
        df = pd.read_csv("../data/stores.csv")
    elif dataset == "Test":
        df = pd.read_csv("../data/test.csv")
    elif dataset == "Train":
        df = pd.read_csv("../data//train.csv")
    elif dataset == "Transactions":
        df = pd.read_csv("../data/transactions.csv")
    
    # Display the overview of the dataset
    display_data_overview(df)
    
    # Visualize data
    visualize_data(df)

if __name__ == "__main__":
    main()
