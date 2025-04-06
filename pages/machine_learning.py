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


import streamlit as st

# Example function placeholders for prediction. Define your own model logic here.
def predict_property_price(features):
    # Insert your property price prediction model logic here
    # For demonstration, return a fixed value
    return 100000

def predict_insurance_premium(features):
    # Insert your insurance premium prediction model logic here
    # For demonstration, return a fixed value
    return 500
def load_data_insurance():
    url = "https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv"
    df = pd.read_csv(url)
    return df
def load_data():
    df = pd.read_csv("prices.csv")
    return df
def load_data_gdp():
    # Load the dataset (adjust this path to your Excel file location)
    df = pd.read_excel('GDP_data.xlsx')
    df.drop(['Series Name', 'Series Code', 'Country Code'], axis=1, inplace=True)
    df_melted = df.melt(id_vars=['Country Name'], var_name='Year', value_name='GDP')
    df_melted['Year'] = df_melted['Year'].str.extract('(\d+)').astype(int)
    df_melted.dropna(inplace=True)
    return df_melted

def load_data_app():
    # Load the dataset from the Excel file
    df = pd.read_excel("applications.xlsx")
    return df

def save_data(df, filename):
    # Save the updated dataset to the Excel file
    df.to_excel(filename, index=False)

def perform_kmeans(df):
    # Perform KMeans clustering on the dataset
    kmeans = KMeans(n_clusters=2)
    kmeans.fit(df[['Points', 'Percentage']])
    df['Cluster'] = kmeans.labels_
    return df

def main():
    # Streamlit page configuration
    st.title("Machine Learning Predictions")

    # Dropdown menu for prediction options
    prediction_option = st.selectbox("Choose a prediction model:", ("Property Price", "Insurance Premium", "Insurance Premium(Based on the multiple values)","Eligibility for studying abroad"))

    # Assuming some input fields are common or you have a way to dynamically adjust input fields based on the model
    # For demonstration, using generic input. Adjust according to your model's input requirements.

    if prediction_option == "Property Price":
            df = load_data()

            # Splitting the dataset into the Training set and Test set
            X = df[['area']].values
            y = df['price'].values

            # Training the Simple Linear Regression model on the Training set
            regressor = LinearRegression()
            regressor.fit(X, y)

            # Streamlit app
            st.title("Property Price Prediction")

            # Display Linear Regression Graph
            st.write("Linear Regression Graph")
            fig, ax = plt.subplots()
            ax.scatter(X, y, color='blue', label='Actual Price',)
            ax.plot(X, regressor.predict(X), color='red', linewidth=2, label='Predicted Price')
            plt.xlabel('Area', color="white")
            plt.ylabel('Price', color="white")
            plt.xticks(ha='right', color='white')  # Rotate x-axis labels for better visibility
            plt.yticks(color='white')
            plt.title('Property Price vs. Area')
            plt.legend()
            st.pyplot(plt.gcf(), transparent=True)

            # Predicting a new result
            user_area = st.number_input("Enter the area (sqft):", min_value=0.0, format='%f')
            if st.button("Predict"):
                predicted_price = regressor.predict([[user_area]])
                st.subheader(f"The predicted property price for {user_area} sqft is: ${predicted_price[0]:,.2f}")
    elif prediction_option == "Insurance Premium":
        df = load_data_insurance()

        # Splitting the dataset into the Training set and Test set
        X = df[['age']].values
        y = df['charges'].values

        # Training the Simple Linear Regression model on the Training set
        regressor = LinearRegression()
        regressor.fit(X, y)

        # Streamlit app
        st.title("Insurance Charges Prediction")

        # Display Linear Regression Graph
        st.write("Linear Regression Graph")
        fig, ax = plt.subplots()
        ax.scatter(X, y, color='blue', label='Actual Charges')
        ax.plot(X, regressor.predict(X), color='red', linewidth=2, label='Predicted Charges')
        plt.xlabel('Age', color="white")
        plt.ylabel('Charges', color="white")
        plt.title('Insurance Charges vs. Age')
        plt.xticks(ha='right', color='white')  # Rotate x-axis labels for better visibility
        plt.yticks(color='white')
        plt.legend()
        st.pyplot(plt.gcf(), transparent=True)

        # Predicting a new result
        user_age = st.number_input("Enter the age:", min_value=0, value=30)
        if st.button("Predict"):
            predicted_charges = regressor.predict([[user_age]])
            st.subheader(f"The predicted insurance charges for age {user_age} is: ${predicted_charges[0]:,.2f}")
    elif prediction_option == "Insurance Premium(Based on the multiple values)":
        df = load_data_insurance()
        df['smoker'] = df['smoker'].map({'yes': 1, 'no': 0})
        X = df[['age', 'bmi', 'children', 'smoker']].values
        y = df['charges'].values

        # Splitting the dataset into the Training set and Test set
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

        # Training the Multiple Linear Regression model
        regressor = LinearRegression()
        regressor.fit(X_train, y_train)

        # Streamlit app
        st.title("Insurance Charges Prediction")

        # User input for independent variables
        age = st.number_input("Enter age:")
        bmi = st.number_input("Enter BMI:")
        children = st.number_input("Enter number of children:")
        smoker = st.radio("Smoker (Yes/No):", ['Yes', 'No'])

        # Convert smoker input to binary
        smoker_binary = 1 if smoker == 'Yes' else 0
        if st.button("Predict"):
            predicted_charges = regressor.predict([[age, bmi, children, smoker_binary]])
            st.write(f"The predicted insurance charges based on the input variables are: ${predicted_charges[0]:,.2f}")
    # Implement the actual logic for `predict_property_price` and `predict_insurance_premium` based on your ML models.
    elif prediction_option == "GDP prediction":
        data = load_data_gdp()
        st.title('Country GDP Analysis')

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
        sns.scatterplot(x=X['Year'], y=y, color='blue', label='Actual GDP')
        sns.lineplot(x=X_fit[:, 0], y=y_pred, color='red', label='Polynomial Regression Fit')
        plt.title(f'GDP Trend for {country}')
        plt.xlabel('Year', color="white")
        plt.ylabel('GDP (current US$)', color="white")
        plt.xticks(ha='right', color='white')  # Rotate x-axis labels for better visibility
        plt.yticks(color='white')
        plt.legend()

        # Display plot in Streamlit
        st.pyplot(plt)

        year = st.number_input('Enter the Year', min_value=1990, max_value=2030, step=1)
        if st.button('Predict GDP'):
            # Ensure the year is in the correct format for prediction
            year_to_predict = np.array([[year]])

            # Predicting the GDP for the selected country and year
            predicted_gdp = polyreg.predict(year_to_predict)

            # Display the predicted GDP
            st.write(f"The predicted GDP for {country} in {year} is: ${predicted_gdp[0]:,.2f} (current US$)")

    elif prediction_option == "Fish Weight prediction":
        df_fish = pd.read_csv('Fish.csv')

        # Streamlit app
        st.title('Fish Weight Prediction')
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df_fish, x='Weight', y='Length1', hue='Species', palette='Set1', color="white")
        plt.title('Relationship between Fish Weight and Length1')
        plt.xlabel('Weight', color="white")
        plt.ylabel('Length1', color="white")
        plt.xticks(ha='right', color='white')  # Rotate x-axis labels for better visibility
        plt.yticks(color='white')
        st.pyplot(plt.gcf(), transparent=True)
        selected_species = st.selectbox('Select Species', options=df_fish['Species'].unique())
        # Input fields for fish features
        length1 = st.number_input('Enter Length1', min_value=0.0)
        length2 = st.number_input('Enter Length2', min_value=0.0)
        length3 = st.number_input('Enter Length3', min_value=0.0)
        height = st.number_input('Enter Height', min_value=0.0)
        width = st.number_input('Enter Width', min_value=0.0)

        # Predict button
        if st.button('Predict Weight'):
            # Prepare input data for prediction
            input_data = np.array([[length1, length2, length3, height, width]])

            # Create a polynomial regression model for each species
            species_models = {}
            for species in df_fish['Species'].unique():
                species_data = df_fish[df_fish['Species'] == species]
                X = species_data[['Length1', 'Length2', 'Length3', 'Height', 'Width']]
                y = species_data['Weight']
                degree = 3  # You can adjust the degree of the polynomial
                polyreg = make_pipeline(PolynomialFeatures(degree), LinearRegression())
                polyreg.fit(X, y)
                species_models[species] = polyreg

            # Predict the weight using the appropriate model for the selected species

            predicted_weight = species_models[selected_species].predict(input_data)

            # Display the predicted weight
            st.write(f"The predicted weight of the fish is: {predicted_weight[0]:,.2f} units")

        # Seaborn scatterplot to visualize the relationship between fish weight and its features

    elif prediction_option == "Eligibility for studying abroad":
        st.title("Student Analysis")

        # Load the dataset
        df = load_data_app()

        # Display the form for adding a new student
        st.write("## Add New Student")
        name = st.text_input("Name")
        mobile = st.text_input("Mobile")
        email = st.text_input("Email")
        points = st.number_input("Points")
        percentage = st.number_input("Percentage")

        if st.button("Add Student"):
            new_student = pd.DataFrame({'Name': [name], 'Mobile': [mobile], 'Email': [email], 'Points': [points], 'Percentage': [percentage]})
            df = pd.concat([df, new_student], ignore_index=True)
            save_data(df, "applications.xlsx")
            st.success("Student added successfully!")

        # Perform KMeans clustering
        df = perform_kmeans(df)

        # Save cluster information to a new CSV file
        df.to_csv("cluster_info.csv", index=False)

        # Determine if student can go abroad based on clustering
        st.write("## Student Analysis")
        student_index = len(df) - 1
        student_cluster = df.iloc[student_index]['Cluster']


        # Seaborn graph

        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x='Points', y='Percentage', hue='Cluster', ax=ax)
        plt.title("Scores vs Percentage",color="white")
        plt.xlabel("Points",color="white")
        plt.ylabel("Percentage",color="white")
        plt.xticks(ha='right', color='white')  # Rotate x-axis labels for better visibility
        plt.yticks(color='white')
        plt.legend()
        st.pyplot(plt.gcf(), transparent=True)
        if st.button("Predict"):
            data = pd.read_csv('cluster_info.csv')
            if data['Cluster'].iloc[-1] == 1:
                st.success("Student can go abroad!")
            else:
                st.error("Student cannot go abroad.")

if __name__ == "__main__":
    main()