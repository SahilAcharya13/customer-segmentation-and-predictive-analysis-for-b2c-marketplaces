import streamlit as st
import pandas as pd
import re
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
def load_data():
    return pd.read_csv('zomato_data_cleaning.csv')

# Function to clean phone numbers using regular expressions
def clean_phone_numbers(df):
    # Regular expression pattern for phone numbers starting with +91
    pattern = r'^\+91[789]\d{9}$'

    # Regular expression pattern for phone numbers starting with 080
    pattern_080 = r'^080\d{8}$'

    # Apply regex to phone numbers column
    df['phone'] = df['phone'].astype(str)
    df['phone'] = df['phone'].apply(lambda x: re.sub(r'\D', '', x))  # Remove non-numeric characters
    df['phone'] = df['phone'].apply(lambda x: '+91' + x[-10:] if re.match(pattern, x[-10:]) else ('080' + x[-8:] if re.match(pattern_080, x[-8:]) else ''))

    return df

def main():
        st.title("Zomato Data Cleaning App")


        df = load_data()

        # Display data
        st.subheader("Check for Null Values")
        if df.isnull().sum().any():
            st.write("Null values found in the dataset.")
            null_counts = df.isnull().sum()
            st.write("Number of null values per column:")
            st.write(null_counts)
            cols_with_null = null_counts[null_counts > 0].index.tolist()
            st.write("Columns with null values:")
            st.write(cols_with_null)
        else:
            st.write("No null values found in the dataset.")

        # Cleaning phone numbers
        st.subheader("Cleaning Phone Numbers")
        if st.checkbox("Clean phone numbers"):
            df_phone  = clean_phone_numbers(df)
            st.write(df_phone.head(5))
            st.write("Phone numbers cleaned.")

        # Save cleaned data
        st.header("Save Cleaned Data")
        if st.button("Save cleaned data"):
            file_path = "cleaned_zomato_data.csv"
            df.to_csv(file_path, index=False)
            st.success(f"Cleaned data saved to {file_path}")

if __name__ == "__main__":
    main()
