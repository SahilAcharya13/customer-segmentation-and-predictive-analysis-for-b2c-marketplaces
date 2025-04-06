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
# Load the CSV file into a pandas DataFrame
df = pd.read_csv('train.csv')

# Convert the 'Order Date' column to datetime data type
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y')

# Extract year from 'Order Date' column and create a new column 'Year'
df['Year'] = df['Order Date'].dt.year

# Calculate yearly sales
yearly_sales = df.groupby('Year')['Sales'].sum().reset_index()

# Create a Streamlit interface
st.title('Year-wise Sales Analysis')

# User input for the year
year = st.number_input('Enter a year:', min_value=int(df['Order Date'].dt.year.min()),
                       max_value=int(df['Order Date'].dt.year.max()))

# Filter the DataFrame based on the user input year
filtered_data = df[df['Order Date'].dt.year == year]

# Display the filtered data in a table
st.write('Sales data for the year', year)
st.write(filtered_data)

# Display the yearly sales data in a table
st.write('Yearly Sales Data')
st.write(yearly_sales)

# Plot bar graph of yearly sales using Plotly
fig = px.bar(yearly_sales, x='Year', y='Sales', labels={'Year': 'Year', 'Sales': 'Total Sales ($)'},
             title='Year-wise Sales')
fig.update_xaxes(tickvals=[year for year in yearly_sales['Year'] if year not in [2014   , 2019]])

st.plotly_chart(fig)


# Group the data by Customer ID and calculate the total spending for each customer
customer_spending = df.groupby('Customer ID')['Sales'].sum().reset_index()

# Sort the customers by spending in descending order and select the top 5
top_5_spenders = customer_spending.nlargest(5, 'Sales')

# Extract customer names from Customer ID
customer_names = {}
for customer_id in top_5_spenders['Customer ID']:
    customer_names[customer_id] = df[df['Customer ID'] == customer_id]['Customer Name'].iloc[0]

# Create a DataFrame for top 5 highest spender customer IDs and names
top_5_spenders_with_names = pd.DataFrame({
    'Customer ID': top_5_spenders['Customer ID'],
    'Customer Name': [customer_names[customer_id] for customer_id in top_5_spenders['Customer ID']],
    'Total Spending ($)': top_5_spenders['Sales']
})

# Create a Streamlit interface
st.title('Top 5 Highest Spender Customers')

# Display the table of top 5 highest spender customers with their names and total spending
st.write(top_5_spenders_with_names)

# Plot horizontal bar graph of top 5 highest spender customers
fig = px.bar(top_5_spenders_with_names,
             x='Total Spending ($)',
             y='Customer Name',
             orientation='h',
             labels={'Total Spending ($)': 'Total Spending ($)', 'Customer Name': 'Customer Name'},
             title='Top 5 Highest Spender Customers')
st.plotly_chart(fig)


# Sort the customers by spending in ascending order and select the bottom 5
bottom_5_spenders = customer_spending.nsmallest(5, 'Sales')

# Extract customer names from Customer ID
customer_names = {}
for customer_id in bottom_5_spenders['Customer ID']:
    customer_names[customer_id] = df[df['Customer ID'] == customer_id]['Customer Name'].iloc[0]

# Create a DataFrame for bottom 5 lowest spender customer IDs and names
bottom_5_spenders_with_names = pd.DataFrame({
    'Customer ID': bottom_5_spenders['Customer ID'],
    'Customer Name': [customer_names[customer_id] for customer_id in bottom_5_spenders['Customer ID']],
    'Total Spending ($)': bottom_5_spenders['Sales']
})

# Create a Streamlit interface
st.title('Bottom 5 Lowest Spender Customers')

# Display the table of bottom 5 lowest spender customers with their names and total spending
st.write(bottom_5_spenders_with_names)

# Plot horizontal bar graph of bottom 5 lowest spender customers
fig = px.bar(bottom_5_spenders_with_names,
             x='Total Spending ($)',
             y='Customer Name',
             orientation='h',
             labels={'Total Spending ($)': 'Total Spending ($)', 'Customer Name': 'Customer Name'},
             title='Bottom 5 Lowest Spender Customers')
st.plotly_chart(fig)