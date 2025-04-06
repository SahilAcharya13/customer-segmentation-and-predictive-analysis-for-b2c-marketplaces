import pandas as pd
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

# Load the dataset
df = pd.read_csv("Mall_Customers.csv")

# Function to print dataset
def print_dataset():
    st.write("### Dataset")
    st.dataframe(df)

# Function to print rows and columns
def print_rows_and_columns():
    st.write(f"### Rows: {df.shape[0]}, Columns: {df.shape[1]}")

# Function to print null values by columns
def print_null_values():
    st.write("### Null Values by Columns")
    st.write(df.isnull().sum())

# Function to print annual income & spending score
def print_annual_income_and_spending_score():
    st.write("### Annual Income & Spending Score")
    st.write(df[['Annual Income (k$)', 'Spending Score (1-100)']])

# Function to print data info


# Function to print gender value count
def print_gender_value_count():
    st.write("### Gender Value Count")
    st.write(df['Genre'].value_counts())

# Function to print age and annual income
def print_age_and_annual_income():
    st.write("### Age and Annual Income")
    st.write(df[['Age', 'Annual Income (k$)']])

# Function to print top 10 most spending score customers
def print_top_10_spending_customers():
    st.write("### Top 10 Most Spending Score Customers")
    st.write(df.nlargest(10, 'Spending Score (1-100)')[['CustomerID', 'Spending Score (1-100)']])

# Function to print top 10 highest income customers
def print_top_10_highest_income_customers():
    st.write("### Top 10 Highest Income Customers")
    st.write(df.nlargest(10, 'Annual Income (k$)')[['CustomerID', 'Annual Income (k$)']])

# Main function to run Streamlit app
def main():
    st.title("Mall Customer Data Analysis")

    print_dataset()
    print_rows_and_columns()
    print_null_values()
    print_annual_income_and_spending_score()

    print_gender_value_count()
    print_age_and_annual_income()
    print_top_10_spending_customers()
    print_top_10_highest_income_customers()

if __name__ == "__main__":
    main()
