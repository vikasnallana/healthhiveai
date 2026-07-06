import streamlit as st

from services.auth_services import get_current_user
from services.profile_service import get_profile


def require_login():
    """
    Redirects the user if not logged in.
    """

    user = get_current_user()

    if not user:
        st.warning("⚠️ Please login first.")
        st.stop()

    return user


def get_current_profile():
    """
    Returns the logged-in user's profile.
    """

    user = require_login()

    profile = get_profile(user["id"])

    return profile


def is_profile_complete(profile: dict | None) -> bool:
    """
    Checks whether the user's profile has all required fields.
    """

    if profile is None:
        return False

    required_fields = [
        "age",
        "gender",
        "height",
        "weight",
        "goal",
        "activity",
        "food_preference",
    ]

    for field in required_fields:

        if profile.get(field) in [None, "", 0]:
            return False

    return True