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

# Function for interactive map or plot with date filter
def interactive_map_with_date_filter(df):
    st.write("### Interactive Data Exploration with Date Filter")
    
    # Ensure that the dataframe has a date column
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])  # Convert to datetime format if not already

        # Get min and max dates from the data
        min_date = df['date'].min()
        max_date = df['date'].max()

        # Date range selection with Streamlit's date_input widget
        start_date, end_date = st.date_input("Select date range", [min_date, max_date], min_value=min_date, max_value=max_date)

        # Filter data based on the selected date range
        df_filtered = df[(df['date'] >= pd.to_datetime(start_date)) & (df['date'] <= pd.to_datetime(end_date))]

        # Create dropdowns for column selection
        numeric_columns = df_filtered.select_dtypes(include=['float', 'int']).columns.tolist()
        categorical_columns = df_filtered.select_dtypes(include=['object', 'category']).columns.tolist()

        # Interactive selection of X and Y axes for plotting
        x_axis = st.selectbox("Select X-axis", numeric_columns + categorical_columns)
        y_axis = st.selectbox("Select Y-axis", numeric_columns)

        # Allow the user to filter by a categorical column
        if categorical_columns:
            category = st.selectbox("Select a category to filter by", categorical_columns)
            unique_values = df_filtered[category].unique().tolist()
            selected_values = st.multiselect(f"Select {category} values to filter", unique_values, default=unique_values)
            df_filtered = df_filtered[df_filtered[category].isin(selected_values)]

        # Plot the selected data
        fig = px.scatter(df_filtered, x=x_axis, y=y_axis, color=category if categorical_columns else None, title=f"{y_axis} vs {x_axis}")
        st.plotly_chart(fig)
    else:
        st.write("The dataset does not contain a 'date' column.")

# Main app
def main():
    st.title("Interactive EDA App with Date Filter")
    
    # Sidebar for dataset selection
    st.sidebar.title("Options")
    dataset = st.sidebar.selectbox("Select Dataset", ["Holidays", "Oil", "Stores", "Test", "Train", "Transactions"])
    
    # Load the corresponding dataset
    if dataset == "Holidays":
        df = pd.read_csv("../data/holidays_events.csv")
    elif dataset == "Oil":
        df = pd.read_csv("../data/oil.csv")
    elif dataset == "Stores":
        df = pd.read_csv("../data/stores.csv")
    elif dataset == "Test":
        df = pd.read_csv("../data/test.csv")
    elif dataset == "Train":
        df = pd.read_csv("../data/train.csv")
    elif dataset == "Transactions":
        df = pd.read_csv("../data/transactions.csv")
    
    # Display the overview of the dataset
    display_data_overview(df)
    
    # Interactive plot with date filter
    interactive_map_with_date_filter(df)

if __name__ == "__main__":
    main()
