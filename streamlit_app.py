import streamlit as st
from notebooks import home, utils


# Home Page
st.set_page_config(page_title="Sales Forecast App", layout="wide")

# Sidebar Navigation
# st.sidebar.title("Navigation")
# page = st.sidebar.radio("Go to", ["Home", "Map", "Charts"])

# # Conditional navigation
# if page == "Home":
#     home.main()  # Assuming home.py has a main() function
# elif page == "Map":
#     st.experimental_rerun()  # Redirects to 1_Map.py
# elif page == "Charts":
#     st.experimental_rerun()  # Redirects to 2_Chart.py

# # After some event (like a button click):
# if st.button("Go to Chart"):
#     st.experimental_rerun()  # This will rerun the entire app and should take you to 2_Chart.py if set up correctly

st.write("# Predicting Sales for Corporación Favorita")
#st.image("../images/imag1.jpg", caption="Sunrise by the mountains")
st.markdown(
    """
    ## Project Objective ##
To predict the unit sales for the next 16 days for thousands of items sold at various Corporación Favorita stores in Ecuador.

Business Problem
Corporación Favorita faces two primary challenges:

* Stock-outs: Popular items selling out quickly can lead to lost sales and customer dissatisfaction.
* Overstocks: Excess inventory can result in high storage costs and potential product spoilage.

### Solution ###
Accurate unit sales prediction can help mitigate these issues by:

* Optimizing logistical operations: Improved inventory management reduces both stock-outs and overstocks.
* Reducing costs: Minimizing lost sales and storage expenses leads to significant cost savings.
* By predicting future demand, Corporación Favorita can better align its supply chain and ensure product availability while avoiding excessive inventory.

**
👈 Select a viz type from the sidebar**
### Want to see the original source?
# 🧾 [Kaggle dataset](https://https://www.kaggle.com/competitions/store-sales-time-series-forecasting/data) 
    
"""
)