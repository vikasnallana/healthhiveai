import streamlit as st
from services.auth_services import login_user

st.title("🔐 Login to HealthHive AI")

with st.form("login_form"):

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    submitted = st.form_submit_button("Login")

    if submitted:

        email = email.strip().lower()

        if not email or not password:
            st.error("Please fill in all fields.")

        else:
            success, result = login_user(email, password)

            if success:
                st.session_state.logged_in = True
                st.session_state.user = result

                st.success("Login successful!")

                st.rerun()

            else:
                st.error(result)