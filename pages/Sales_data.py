import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

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
sl = pd.read_csv('sales.csv')

import streamlit as st
st.header("Sales Dataset")
st.write(sl.head(5))

st.subheader("Sales Dataset Coloumn info")
st.write('Segment')
st.write(sl['Segment'].value_counts())
st.write('Region')
st.write(sl['Region'].value_counts())
st.write('Category')
st.write(sl['Category'].value_counts())
st.write('Sub-Category')
st.write(sl['Sub-Category'].value_counts())
st.write('Ship Mode')
st.write(sl['Ship Mode'].value_counts())

st.title('Sales in U.S.')
import plotly.graph_objects as go
from plotly.subplots import make_subplots

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
sl['Abbreviation'] = sl['State'].map(all_state_mapping)

# Group by state and calculate the sum of sales
sum_of_sales = sl.groupby('State')['Sales'].sum().reset_index()

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

st.title('Sales in U.S. Bar Graph')
# Group by state and calculate the sum of sales
sum_of_sales = sl.groupby('State')['Sales'].sum().reset_index()

# Sort the DataFrame by the 'Sales' column in descending order
sum_of_sales = sum_of_sales.sort_values(by='Sales', ascending=False)

# Create a horizontal bar graph
plt.figure(figsize=(10, 13))
ax = sns.barplot(x='Sales', y='State', data=sum_of_sales, ci=None)

plt.xlabel('Sales',color="white")
plt.ylabel('State',color="white")
plt.title('Total Sales by State',color="white")
plt.xticks(color="white")
plt.yticks(color="white")

st.pyplot(plt.gcf(), transparent=True)


st.header('Summary of Category and Sub-Category')
sl_summary = sl.groupby(['Category', 'Sub-Category'])['Sales'].sum().reset_index()
st.write(sl_summary)

import plotly.express as px
st.header('Pie of Category and Sub-Category')
# Create a nested pie chart
fig = px.sunburst(
    sl_summary,
    path=['Category', 'Sub-Category'],
    values='Sales',
)

st.write(fig)


