import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
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

def load_data_gdp():
    # Load the dataset (adjust this path to your Excel file location)
    df = pd.read_excel('GDP_data.xlsx')
    df.drop(['Series Name', 'Series Code', 'Country Code'], axis=1, inplace=True)
    df_melted = df.melt(id_vars=['Country Name'], var_name='Year', value_name='GDP')
    df_melted['Year'] = df_melted['Year'].str.extract('(\d+)').astype(int)
    df_melted.dropna(inplace=True)
    return df_melted

data = load_data_gdp()
st.title('Country GDP Prediction')

# Country selection
country = st.selectbox('Select a Country', options=data['Country Name'].unique())

# Extract data for the selected country
country_data = data[data['Country Name'] == country]

# Polynomial Regression
X = country_data[['Year']]
y = country_data['GDP']

# Splitting the dataset (using all data for fitting in this example)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

degree = 3  # Degree of polynomial
polyreg = make_pipeline(PolynomialFeatures(degree), LinearRegression())
polyreg.fit(X_train, y_train)

# Predicting across the range of X for plotting
X_fit = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
y_pred = polyreg.predict(X_fit)

# Visualization with Seaborn
plt.figure(figsize=(10, 6))
sns.scatterplot(x=X['Year'], y=y, color='green', label='Actual GDP')
sns.lineplot(x=X_fit[:, 0], y=y_pred, color='red', label='Polynomial Regression Fit')
plt.title(f'GDP Trend for {country}',color='white')
plt.xlabel('Year', color="white")
plt.ylabel('GDP (current US$)', color="white")
plt.xticks(ha='right', color='white')  # Rotate x-axis labels for better visibility
plt.yticks(color='white')
plt.legend()

# Display plot in Streamlit
st.pyplot(plt.gcf(), transparent=True)

year = st.number_input('Enter the Year', min_value=1990, max_value=2030, step=1)
if st.button('Predict GDP'):
    # Ensure the year is in the correct format for prediction
    year_to_predict = np.array([[year]])

    # Predicting the GDP for the selected country and year
    predicted_gdp = polyreg.predict(year_to_predict)

    # Display the predicted GDP
    st.write(f"The predicted GDP for {country} in {year} is: ${predicted_gdp[0]:,.2f} (current US$)")
