import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }

        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
        footer {visibility: hidden;}
    [data-testid="collapsedControl"] {
        display: none
    }
    </style>
""", unsafe_allow_html=True)
st.title('Walmart sales visualization')
# Load features.csv
features_df = pd.read_csv("Walmart sales forecast/features.csv")

# Load stores.csv
stores_df = pd.read_csv("Walmart sales forecast/stores.csv")


holiday_pie_chart = px.pie(features_df, names='IsHoliday', title='Holiday Distribution')
st.plotly_chart(holiday_pie_chart)

# Histogram for store sizes
store_size_histogram = px.histogram(stores_df, x='Size', title='Store Size Distribution')
st.plotly_chart(store_size_histogram)

# Scatter plot for temperature vs. sales
temperature_sales_scatter = px.scatter(features_df, x='Temperature', y='Fuel_Price', title='Temperature vs. Fuel Price')
st.plotly_chart(temperature_sales_scatter)

# Merge features_df with stores_df to get the store type
merged_df = pd.merge(features_df, stores_df, on='Store')

# Calculate total sales for each store grouped by store type
total_sales_by_store_type = merged_df.groupby(['Type', 'Store'])['Temperature'].sum().reset_index()

# Find the store with the highest sales within each store type
highest_sales_store_by_type = total_sales_by_store_type.groupby('Type')['Temperature'].idxmax()

# Get the details of the stores with the highest sales within each store type
stores_with_highest_sales = total_sales_by_store_type.loc[highest_sales_store_by_type]

# Create a bar chart to visualize the stores with the highest sales within each store type
sales_by_store_type_bar_chart = px.bar(stores_with_highest_sales, x='Type', y='Temperature', color='Store', title='Stores with Highest Sales by Type')
st.plotly_chart(sales_by_store_type_bar_chart)



# Allow the user to select a store
selected_store = st.selectbox('Select a store:', stores_df['Store'])

# Filter the features dataframe for the selected store
selected_store_data = features_df[features_df['Store'] == selected_store]

# Create a line chart for unemployment over time for the selected store
unemployment_line_chart = px.line(selected_store_data, x='Date', y='Unemployment', title=f'Unemployment Over Time for Store {selected_store}')
st.plotly_chart(unemployment_line_chart)


