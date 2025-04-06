import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
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

def load_data(file):
    if file is not None:
        file_type = file.name.split('.')[-1]
        if file_type.lower() == 'csv':
            return pd.read_csv(file)
        elif file_type.lower() in ['xlsx', 'xls']:
            return pd.read_excel(file)
    return None

def calculate_statistics(df):
    if df is not None:
        stats = df.describe()
        st.write("### Statistics")
        st.write(stats)

def find_null_columns(df):
    if df is not None:
        null_columns = df.columns[df.isnull().any()]
        st.write("### Null Columns")
        st.write(null_columns)

def find_total_null_values(df):
    if df is not None:
        total_null_values = df.isnull().sum().sum()
        st.write("### Total Null Values")
        st.write(total_null_values)
        if total_null_values > 0:
            st.write("### Locations of Null Values")
            st.write(df[df.isnull().any(axis=1)])

def show_data_analysis_tools(df):
    if df is not None:
        st.write("### Dataset Quick Look")
        if st.button("Show Head"):
            st.write(df.head())

        if st.button("Describe Data"):
            st.write(df.describe())

        if st.button("Show Shape"):
            st.write(df.shape)

        if st.button("Calculate Statistics"):
            calculate_statistics(df)

        if st.button("Find Null Columns"):
            find_null_columns(df)

        if st.button("Find Total Null Values"):
            find_total_null_values(df)

def main():
    st.title("Data Analysis")

    #File uploader
    data_file = st.file_uploader("Upload your CSV or Excel file", type=['csv', 'xlsx', 'xls'], accept_multiple_files=False)
    if data_file is not None:
    # Load and cache the data
        df = load_data(data_file)
        show_data_analysis_tools(df)

if __name__ == "__main__":
    main()