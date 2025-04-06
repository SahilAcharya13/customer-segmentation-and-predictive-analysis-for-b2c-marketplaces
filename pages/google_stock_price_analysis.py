import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
# Load CSV data into a pandas DataFrame
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
def load_data():
    data = pd.read_csv("google_stock_price.csv")
    return data

# Function to create a line chart of daily stock prices
def plot_daily_stock_prices(data):
    fig = px.line(data, x='Date', y='Close', title='Daily Stock Prices')
    st.plotly_chart(fig)

# Function to create a bar graph of details for a specific date
def plot_details_for_date(data, selected_date):
    selected_data = data[data['Date'] == selected_date]
    if len(selected_data) == 0:
        st.write("No data available for selected date.")
    else:
        fig = px.bar(selected_data, x=['Open', 'High', 'Low', 'Close'],
                     title=f'Details for {selected_date}')
        st.plotly_chart(fig)

def main():
    st.title("Google Stock Price Analysis")

    # Load data
    data = load_data()
    st.subheader('Data in the file:')
    st.dataframe(data.head())
    # Display daily stock prices graph
    st.subheader('Stock price graph:')
    plot_daily_stock_prices(data)

    # Input field for user to enter a date
    selected_date = st.text_input("Enter a date (YYYY-MM-DD):")

    # Plot details for the selected date
    if selected_date:
        selected_data = data[data['Date'] == selected_date]
        if len(selected_data) == 0:
            st.write("No data available for selected date.")
        else:
            fig = go.Figure(data=[
                go.Bar(name='Open', x=['Open'], y=[selected_data['Open'].values[0]]),
                go.Bar(name='High', x=['High'], y=[selected_data['High'].values[0]]),
                go.Bar(name='Low', x=['Low'], y=[selected_data['Low'].values[0]]),
                go.Bar(name='Close', x=['Close'], y=[selected_data['Close'].values[0]])
            ])
            fig.update_layout(title=f'Details for {selected_date}',
                              xaxis_title='Price Type',
                              yaxis_title='Price')
            st.plotly_chart(fig)

if __name__ == "__main__":
    main()
