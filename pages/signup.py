import streamlit as st
from services.auth_services import signup_user

st.title("📝 Create Your HealthHive Account")

with st.form("signup_form"):

    full_name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    submitted = st.form_submit_button("Sign Up")

    if submitted:

        full_name = full_name.strip()
        email = email.strip().lower()

        if not full_name or not email or not password or not confirm_password:
            st.error("Please fill in all fields.")

        elif password != confirm_password:
            st.error("Passwords do not match.")

        elif len(password) < 6:
            st.error("Password must be at least 6 characters long.")

        else:
            success, message = signup_user(email, password)

            if success:
                st.success(message)
            else:
                st.error(message)