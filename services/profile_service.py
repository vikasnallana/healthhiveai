import streamlit as st


def save_profile(profile_data: dict):
    """
    Saves the user's profile in Streamlit Session State.
    """

    st.session_state["profile"] = profile_data


def get_profile():
    """
    Returns the user's profile.
    """

    return st.session_state.get("profile", None)