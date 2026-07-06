import streamlit as st

from services.auth_services import login_user

st.title("🔐 Login")

st.write("Login to your HealthHive account.")

with st.form("login_form"):

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password",
    )

    submitted = st.form_submit_button(
        "Login",
        use_container_width=True,
    )

if submitted:

    if not username.strip():

        st.error("Please enter your username.")

    elif not password:

        st.error("Please enter your password.")

    else:

        success, result = login_user(
            username=username,
            password=password,
        )

        if success:

            st.success("✅ Login Successful!")

            st.rerun()

        else:

            st.error(result)