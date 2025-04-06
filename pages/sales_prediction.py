import streamlit as st
import pandas as pd
import plotly.graph_objs as go
from prophet import Prophet
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
# Function to load and preprocess the data
def load_data(file_path):
    df = pd.read_csv(file_path)
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d-%m-%Y')
    monthly_data = df.resample('M', on='Order Date').sum()
    monthly_data.reset_index(inplace=True)
    monthly_data = monthly_data.rename(columns={'Order Date': 'ds', 'Sales': 'y'})
    return monthly_data

# Function to train the Prophet model and make predictions
def prophet_forecast(data_train, periods):
    model = Prophet()
    model.fit(data_train)
    future = model.make_future_dataframe(periods=periods, freq='M')
    forecast = model.predict(future)
    return forecast

# Main function to run the Streamlit app
def main():
    st.title("Sales Forecasting App")

    # Sidebar section for uploading file and setting parameters

    uploaded_file = "sales.csv"
    if uploaded_file is not None:
        data_train = load_data(uploaded_file)

        # Display uploaded data
        st.subheader("Uploaded Data")
        st.write(data_train)
        periods = st.slider("Number of months to forecast", min_value=1, max_value=36, value=12)

        # Train model and make predictions
        forecast = prophet_forecast(data_train, periods)

        # Plotting with Plotly
        fig = go.Figure()

        # Add actual sales data
        fig.add_trace(go.Scatter(x=data_train['ds'], y=data_train['y'], mode='lines', name='Actual Sales'))

        # Add forecasted sales data
        fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], mode='lines', name='Forecast'))

        # Add uncertainty interval
        fig.add_trace(go.Scatter(
            x=pd.concat([forecast['ds'], forecast['ds'][::-1]]),
            y=pd.concat([forecast['yhat_lower'], forecast['yhat_upper'][::-1]]),
            fill='toself',
            fillcolor='rgba(0,100,80,0.2)',
            line=dict(color='rgba(255,255,255,0)'),
            name='Uncertainty Interval'
        ))

        # Update layout
        fig.update_layout(title="Sales Forecast",
                          xaxis_title="Date",
                          yaxis_title="Sales",
                          legend=dict(x=0, y=1, traceorder="normal"),
                          plot_bgcolor='rgba(0,0,0,0)',
                          paper_bgcolor='rgba(0,0,0,0)',
                          )

        # Display plot
        st.plotly_chart(fig)

# Run the app
if __name__ == "__main__":
    main()
