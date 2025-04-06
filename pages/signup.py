# signin.py
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
# Function to validate email address
def validate_email(email):
    pattern = r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
    if re.match(pattern, email):
        return True
    else:
        return False

# Function to validate phone number
def validate_phone(phone):
    pattern = r"^\d{10}$"
    if re.match(pattern, phone):
        return True
    else:
        return False

# Function to validate password
def validate_password(password):
    if len(password) < 8:
        return False
    else:
        return True

def sign_up(full_name, email, phone, password, confirm_password):
    if password != confirm_password:
        st.error("Password and Confirm Password do not match")
        return

    if not validate_email(email):
        st.error("Invalid email address")
        return

    if not validate_phone(phone):
        st.error("Invalid phone number (10 digits only)")
        return

    if not validate_password(password):
        st.error("Password must be at least 8 characters long")
        return

    user_data = {
        "Full Name": [full_name],
        "Email": [email],
        "Phone Number": [phone],
        "Password": [password]
    }
    us = pd.DataFrame(user_data)
    us.to_csv("data.csv",index=False)

    st.success("You have successfully signed up!")

def main():
    st.title("Sign-up Page")
    st.write("Please sign up to continue.")

    full_name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Sign-up"):
        if full_name == "" or email == "" or phone == "" or password == "" or confirm_password == "":
            st.warning("All fields are required")
        else:
            sign_up(full_name, email, phone, password, confirm_password)

    st.markdown("Already have an account? [Log in here](/login)")

if __name__ == "__main__":
    main()
