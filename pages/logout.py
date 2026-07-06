import streamlit as st

from services.auth_services import logout_user

st.title("🚪 Logout")

st.write("Click below to logout.")

if st.button(
    "Logout",
    use_container_width=True,
):

    logout_user()

    st.success("Logged out successfully.")

    st.rerun()