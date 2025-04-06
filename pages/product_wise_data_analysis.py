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

# Category-wise orders analysis
category_orders = df['Category'].value_counts().reset_index()
category_orders.columns = ['Category', 'Orders Count']

# Pie chart showing count of orders for each category
fig = px.pie(category_orders,
             values='Orders Count',
             names='Category',
             title='Category-wise Orders Analysis',
             labels={'Orders Count': 'Orders Count', 'Category': 'Category'},
             hole=0.3)

# Create a Streamlit interface
st.title('Product Wise Data Analysis')

# Display category-wise orders analysis
st.header('Category-wise Orders Analysis')
st.write(category_orders)

# Display the pie chart
st.plotly_chart(fig)


st.header("Highest selling products")
# Calculate total sales for each product
product_sales = df.groupby('Product ID')['Sales'].sum().reset_index()

# Sort products by total sales in descending order
top_selling_products = product_sales.sort_values(by='Sales', ascending=False).head(10)

# Get the names of the top selling products
top_selling_products_names = df[df['Product ID'].isin(top_selling_products['Product ID'])][['Product ID', 'Product Name']].drop_duplicates()

# Display the highest selling products in a table
st.title('Highest Selling Products (Table)')
st.write(top_selling_products.merge(top_selling_products_names, on='Product ID'))

# Plot the highest selling products in a graph
fig = px.bar(top_selling_products.merge(top_selling_products_names, on='Product ID'),
             x='Product Name', y='Sales', text='Sales',
             title='Highest Selling Products (Graph)',
             labels={'Sales': 'Total Sales ($)', 'Product Name': 'Product Name'})
fig.update_traces(textposition='outside')
st.plotly_chart(fig)


# Sort products by total sales in ascending order to get lowest selling products
lowest_selling_products = product_sales.sort_values(by='Sales', ascending=True).head(10)

# Get the names of the lowest selling products
lowest_selling_products_names = df[df['Product ID'].isin(lowest_selling_products['Product ID'])][['Product ID', 'Product Name']].drop_duplicates()

# Display the lowest selling products in a table
st.title('Lowest Selling Products (Table)')
st.write(lowest_selling_products.merge(lowest_selling_products_names, on='Product ID'))

# Plot the lowest selling products in a graph
fig = px.bar(lowest_selling_products.merge(lowest_selling_products_names, on='Product ID'),
             x='Product Name', y='Sales', text='Sales',
             title='Lowest Selling Products (Graph)',
             labels={'Sales': 'Total Sales ($)', 'Product Name': 'Product Name'})
fig.update_traces(textposition='outside')
st.plotly_chart(fig)

# Get unique categories
categories = df['Category'].unique()

# Create a Streamlit interface
st.title('Category-wise Subcategory Distribution')

# Dropdown to select a category
selected_category = st.selectbox('Select a category', categories)

# Filter dataframe based on selected category
filtered_df = df[df['Category'] == selected_category]

# Calculate count of subcategories
subcategory_count = filtered_df['Sub-Category'].value_counts().reset_index()
subcategory_count.columns = ['Sub-Category', 'Count']

# Plot pie chart for subcategory distribution
fig = px.pie(subcategory_count,
             values='Count',
             names='Sub-Category',
             title=f'Subcategory Distribution for {selected_category}',
             labels={'Count': 'Count', 'Sub-Category': 'Sub-Category'},
             hole=0.3)

# Display the pie chart
st.plotly_chart(fig)