# login.py
import streamlit as st
import pandas as pd
import time
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

# Function to check if user exists in CSV file
def is_user(email, password):
    df = pd.read_csv("data.csv")
    if (df['Email'] == email).any() and (df['Password'] == password).any():
        return True
    else:
        return False

def main():
    st.title("Login Page")
    st.write("Please log in to continue.")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if is_user(email, password):
            st.success("Login successful!")
            st.write("Redirecting to the dashboard...")
            st.markdown(f'<meta http-equiv="refresh" content="2;url=http://localhost:8501/dashboard">', unsafe_allow_html=True)
        else:
            st.error("Invalid email or password")

    st.markdown("Don't have an account? [Sign up here](/signup)")

if __name__ == "__main__":
    main()
