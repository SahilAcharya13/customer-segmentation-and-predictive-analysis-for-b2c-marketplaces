import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import plotly.express as px
# Load training data
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


def load_train_data():
    train_data = pd.read_csv("Walmart sales forecast/train.csv")
    train_data['Date'] = pd.to_datetime(train_data['Date'])
    train_data['IsHoliday'] = train_data['IsHoliday'].astype(int)
    return train_data

# Load test data

def load_test_data():
    test_data = pd.read_csv("Walmart sales forecast/test.csv")
    test_data['Date'] = pd.to_datetime(test_data['Date'])
    test_data['IsHoliday'] = test_data['IsHoliday'].astype(int)
    return test_data

# Train model

def train_model(train_data):
    X = train_data.drop(columns=['Weekly_Sales', 'Date'])
    y = train_data['Weekly_Sales']
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    return model, X_val, y_val

# Make predictions

def make_predictions(model, test_data):
    test_predictions = model.predict(test_data.drop(columns=['Date']))
    test_data['Predicted_Weekly_Sales'] = test_predictions
    return test_data

def main():
    st.title("Walmart Sales Prediction")

    # Load data
    train_data = load_train_data()
    test_data = load_test_data()

    # Train model
    st.subheader("Training Model")
    model, X_val, y_val = train_model(train_data)
    mae = mean_absolute_error(y_val, model.predict(X_val))
    st.write("Mean Absolute Error on Validation Data:", mae)

    # Make predictions
    st.subheader("Making Predictions on Test Data")
    test_predictions = make_predictions(model, test_data)
    st.write(test_predictions)
    test_predictions.sort_values(by='Date')
if __name__ == "__main__":
    main()
