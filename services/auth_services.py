import streamlit as st

from config.supabase_client import supabase
from utils.password_utils import (
    hash_password,
    verify_password,
)


def signup_user(
    full_name: str,
    username: str,
    password: str,
):
    """
    Create a new HealthHive user.
    """

    username = username.strip().lower()

    existing = (
        supabase.table("users")
        .select("id")
        .eq("username", username)
        .execute()
    )

    if existing.data:
        return False, "Username already exists."

    password_hash = hash_password(password)

    response = (
        supabase.table("users")
        .insert(
            {
                "full_name": full_name,
                "username": username,
                "password_hash": password_hash,
            }
        )
        .execute()
    )

    return True, response.data[0]


def login_user(
    username: str,
    password: str,
):
    """
    Login existing user.
    """

    username = username.strip().lower()

    response = (
        supabase.table("users")
        .select("*")
        .eq("username", username)
        .execute()
    )

    if not response.data:
        return False, "User not found."

    user = response.data[0]

    if not verify_password(
        password,
        user["password_hash"],
    ):
        return False, "Incorrect password."

    st.session_state.logged_in = True
    st.session_state.user = user
    st.session_state.user_id = user["id"]

    return True, user


def logout_user():
    """
    Logout current user.
    """

    keys = [
        "logged_in",
        "user",
        "user_id",
    ]

    for key in keys:

        if key in st.session_state:
            del st.session_state[key]


def get_current_user():
    """
    Returns logged in user.
    """

    return st.session_state.get("user")


def is_logged_in():
    """
    Returns authentication status.
    """

    return st.session_state.get(
        "logged_in",
        False,
    )