import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt

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

# Create a Streamlit interface for Region-wise data analysis

# Create a Streamlit interface
st.title('Region Wise Data Analysis')

# Statewise sales split
statewise_sales = df.groupby('State')['Sales'].sum().reset_index()

# Display statewise sales split in a table
st.header('Statewise Sales Split')
st.write(statewise_sales)

# Top 5 highest selling states
top_5_highest_selling = statewise_sales.nlargest(5, 'Sales')

# Plot bar graph for top 5 highest selling states
fig_top_5_highest = px.bar(top_5_highest_selling,
                            x='State',
                            y='Sales',
                            labels={'Sales': 'Total Sales ($)', 'State': 'State'},
                            title='Top 5 Highest Selling States')
st.plotly_chart(fig_top_5_highest)

# Top 5 lowest selling states
top_5_lowest_selling = statewise_sales.nsmallest(5, 'Sales')

# Plot bar graph for top 5 lowest selling states
fig_top_5_lowest = px.bar(top_5_lowest_selling,
                           x='State',
                           y='Sales',
                           labels={'Sales': 'Total Sales ($)', 'State': 'State'},
                           title='Top 5 Lowest Selling States')
st.plotly_chart(fig_top_5_lowest)




statewise_sales = df.groupby('State')['Sales'].sum().reset_index()

# Sort states by sales in descending order
statewise_sales_sorted = statewise_sales.sort_values(by='Sales', ascending=False)

# Extract top 5 states and sum of sales of other states
top_5_states = statewise_sales_sorted.head(5)
other_states_sales = statewise_sales_sorted.iloc[5:, :]['Sales'].sum()

# Create a DataFrame for top 5 states and the "Other" category
top_5_states_and_other = pd.concat([top_5_states, pd.DataFrame({'State': ['Other'], 'Sales': [other_states_sales]})])

# Plot pie chart for state-wise sales split
fig = px.pie(top_5_states_and_other,
             values='Sales',
             names='State',
             title='State-wise Sales Split',
             labels={'Sales': 'Total Sales ($)', 'State': 'State'},
             hole=0.3)

# Display the pie chart
st.plotly_chart(fig)

st.title("State wise Sales:")
# Initialize Plotly in Jupyter Notebook mode
import plotly.io as pio
pio.renderers.default = 'notebook_connected'


# Create a mapping for all 50 states
all_state_mapping = {
    "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR",
    "California": "CA", "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE",
    "Florida": "FL", "Georgia": "GA", "Hawaii": "HI", "Idaho": "ID", "Illinois": "IL",
    "Indiana": "IN", "Iowa": "IA", "Kansas": "KS", "Kentucky": "KY", "Louisiana": "LA",
    "Maine": "ME", "Maryland": "MD", "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN",
    "Mississippi": "MS", "Missouri": "MO", "Montana": "MT", "Nebraska": "NE", "Nevada": "NV",
    "New Hampshire": "NH", "New Jersey": "NJ", "New Mexico": "NM", "New York": "NY",
    "North Carolina": "NC", "North Dakota": "ND", "Ohio": "OH", "Oklahoma": "OK",
    "Oregon": "OR", "Pennsylvania": "PA", "Rhode Island": "RI", "South Carolina": "SC",
    "South Dakota": "SD", "Tennessee": "TN", "Texas": "TX", "Utah": "UT", "Vermont": "VT",
    "Virginia": "VA", "Washington": "WA", "West Virginia": "WV", "Wisconsin": "WI", "Wyoming": "WY"
}

# Add the Abbreviation column to the DataFrame
df['Abbreviation'] = df['State'].map(all_state_mapping)

# Group by state and calculate the sum of sales
sum_of_sales = df.groupby('State')['Sales'].sum().reset_index()

# Add Abbreviation to sum_of_sales
sum_of_sales['Abbreviation'] = sum_of_sales['State'].map(all_state_mapping)

# Create a choropleth map using Plotly
fig = go.Figure(data=go.Choropleth(
    locations=sum_of_sales['Abbreviation'],
    locationmode='USA-states',
    z=sum_of_sales['Sales'],
    hoverinfo='location+z',
     showscale=True
))

fig.update_geos(projection_type="albers usa")
fig.update_layout(
    geo_scope='usa',
    title='Total Sales by U.S. State'
)

st.write(fig)


# Create a Streamlit interface
st.title('DELIVERY PARTNER ANALYSIS')
# Convert Postal Code to string and remove '.0' from the end
df['Postal Code'] = df['Postal Code'].astype(str).str[:-2]

# Group data by Postal Code and count orders
postal_code_orders = df['Postal Code'].value_counts().reset_index()
postal_code_orders.columns = ['Postal Code', 'Orders Count']

# Sort postal codes by orders count
postal_code_orders_sorted = postal_code_orders.sort_values(by='Orders Count', ascending=False)

# Top 5 postal codes by orders count
top_5_postal_codes = postal_code_orders_sorted.head(5)

# Bottom 5 postal codes by orders count
bottom_5_postal_codes = postal_code_orders_sorted.tail(5)

# Create a color palette for the bar plots
colors = sns.color_palette("husl", n_colors=len(top_5_postal_codes))


# Display top 5 postal codes
st.header('Top 5 Postal Codes by Orders Count')
st.write(top_5_postal_codes)
# Plot bar graph for top 5 postal codes with transparent background
plt.figure(figsize=(10, 6))
sns.barplot(data=top_5_postal_codes, x='Postal Code', y='Orders Count', palette=colors, alpha=0.7)
plt.title('Top 5 Postal Codes by Orders Count',color='white')
plt.xlabel('Postal Code',color='white')
plt.ylabel('Orders Count',color='white')
plt.xticks(rotation=45, ha='right', color='white')
plt.yticks(color='white')
plt.gca().patch.set_alpha(0)  # Set the background transparency
st.pyplot(plt.gcf(), transparent=True)

# Display bottom 5 postal codes
st.header('Bottom 5 Postal Codes by Orders Count')
st.write(bottom_5_postal_codes)

# Plot bar graph for bottom 5 postal codes with transparent background
plt.figure(figsize=(10, 6))
sns.barplot(data=bottom_5_postal_codes, x='Postal Code', y='Orders Count', palette='husl', alpha=0.7)
plt.title('Bottom 5 Postal Codes by Orders Count',color='white')
plt.xlabel('Postal Code',color='white')
plt.ylabel('Orders Count',color='white')
plt.xticks(rotation=45, ha='right', color='white')
plt.yticks(color='white')
plt.gca().patch.set_alpha(0)  # Set the background transparency
st.pyplot(plt.gcf(), transparent=True)




# Calculate total sales for each region
region_sales = df.groupby('Region')['Sales'].sum().reset_index()

# Calculate total sales across all regions
total_sales = region_sales['Sales'].sum()

# Calculate percentage of total sales for each region
region_sales['Percentage of Total Sales'] = (region_sales['Sales'] / total_sales) * 100

# Plot pie chart showing percentage of total sales for each region
fig = px.pie(region_sales,
             values='Percentage of Total Sales',
             names='Region',
             title='Region-wise Sales Distribution',
             labels={'Percentage of Total Sales': 'Percentage of Total Sales (%)', 'Region': 'Region'},
             hole=0.3)

# Create a Streamlit interface
st.title('Region-wise Sales Distribution')

# Display the pie chart
st.plotly_chart(fig)

# Group data by City and count orders
city_orders = df['City'].value_counts().reset_index()
city_orders.columns = ['City', 'Orders Count']

# Limit the number of cities to 40 if there are more
if len(city_orders) > 40:
    city_orders = city_orders.head(40)

# Plot horizontal bar graph for city-wise orders count
fig = px.bar(city_orders,
             x='Orders Count',
             y='City',
             orientation='h',
             title='City-wise Orders Count',
             labels={'Orders Count': 'Orders Count', 'City': 'City'})

# Create a Streamlit interface
st.title('City-wise Orders Count')

# Display the bar graph
st.plotly_chart(fig)

