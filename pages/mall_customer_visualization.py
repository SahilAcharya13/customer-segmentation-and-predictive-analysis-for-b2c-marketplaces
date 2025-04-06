import pandas as pd
import streamlit as st
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

# Load the dataset
df = pd.read_csv("Mall_Customers.csv")

# Function to plot histogram of age
def plot_age_histogram():
    st.write("### Histogram of Age")
    fig = px.histogram(df, x="Age", nbins=20, title="Histogram of Age")
    st.plotly_chart(fig)

# Function to plot scatter graph of Annual income and spending score
def plot_income_spending_scatter():
    st.write("### Scatter Graph of Annual Income and Spending Score")
    fig = px.scatter(df, x='Annual Income (k$)', y='Spending Score (1-100)', title="Scatter Graph of Annual Income and Spending Score")
    st.plotly_chart(fig)

# Function to plot bar graph of gender and spending score
def plot_gender_spending_bar():
    st.write("### Bar Graph of Gender and Spending Score")
    gender_spending = df.groupby('Genre')['Spending Score (1-100)'].mean().reset_index()
    fig = px.bar(gender_spending, x='Genre', y='Spending Score (1-100)', title="Bar Graph of Gender and Spending Score")
    st.plotly_chart(fig)

# Function to plot bar graph of top 10 highest income customers
def plot_top_10_income_bar():
    st.write("### Bar Graph of Top 10 Highest Income Customers")
    top_10_income = df.nlargest(10, 'Annual Income (k$)')
    fig = px.bar(top_10_income, x='CustomerID', y='Annual Income (k$)', title="Bar Graph of Top 10 Highest Income Customers")
    st.plotly_chart(fig)

# Function to plot pie chart graph of top 10 highest spending customers
def plot_top_10_spending_pie():
    st.write("### Pie Chart of Top 10 Highest Spending Customers")
    top_10_spending = df.nlargest(10, 'Spending Score (1-100)')
    fig = px.pie(top_10_spending, values='Spending Score (1-100)', names='CustomerID', title="Pie Chart of Top 10 Highest Spending Customers")
    st.plotly_chart(fig)

# Function to plot bar graph Age Groups and Spending Scores
def plot_age_groups_spending_bar():
    st.write("### Bar Graph of Age Groups and Spending Scores")
    df['Age Group'] = pd.cut(df['Age'], bins=[0, 20, 40, 60, 80, 100], labels=['0-20', '21-40', '41-60', '61-80', '81-100'])
    age_groups_spending = df.groupby('Age Group')['Spending Score (1-100)'].mean().reset_index()
    fig = px.bar(age_groups_spending, x='Age Group', y='Spending Score (1-100)', title="Bar Graph of Age Groups and Spending Scores")
    st.plotly_chart(fig)

# Main function to run Streamlit app
def main():
        st.title("Mall Customer Data Visualization")

        # Navigation sidebar

        plot_age_histogram()
        plot_income_spending_scatter()
        plot_gender_spending_bar()
        plot_top_10_income_bar()
        plot_top_10_spending_pie()
        plot_age_groups_spending_bar()

if __name__ == "__main__":
    main()
