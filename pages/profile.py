import streamlit as st

from services.core_serive import (
    require_login,
    get_current_profile,
)

from services.profile_service import save_or_update_profile

st.set_page_config(
    page_title="My Profile",
    page_icon="👤",
)

user = require_login()
profile = get_current_profile()

if profile is None:
    profile = {}

st.title("👤 My Health Profile")

st.write(
    "Update your personal information to receive personalized AI recommendations."
)

st.info(f"Logged in as: **{user['full_name']}** (@{user['username']})")

gender_options = [
    "Male",
    "Female",
    "Other",
]

goal_options = [
    "Weight Loss",
    "Muscle Gain",
    "Maintain Weight",
    "General Fitness",
]

activity_options = [
    "Sedentary",
    "Lightly Active",
    "Moderately Active",
    "Very Active",
]

food_options = [
    "Vegetarian",
    "Non-Vegetarian",
    "Vegan",
]

with st.form("profile_form"):

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=int(profile.get("age") or 18),
    )

    gender = st.selectbox(
        "Gender",
        gender_options,
        index=gender_options.index(
            profile.get("gender") or "Male"
        ),
    )

    height = st.number_input(
        "Height (cm)",
        min_value=50,
        max_value=250,
        value=int(profile.get("height") or 170),
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=20,
        max_value=300,
        value=int(profile.get("weight") or 60),
    )

    goal = st.selectbox(
        "Goal",
        goal_options,
        index=goal_options.index(
            profile.get("goal") or "General Fitness"
        ),
    )

    activity = st.selectbox(
        "Activity Level",
        activity_options,
        index=activity_options.index(
            profile.get("activity") or "Sedentary"
        ),
    )

    food_preference = st.selectbox(
        "Food Preference",
        food_options,
        index=food_options.index(
            profile.get("food_preference") or "Vegetarian"
        ),
    )

    medical_conditions = st.text_area(
        "Medical Conditions",
        value=profile.get("medical_conditions") or "",
    )

    submitted = st.form_submit_button(
        "💾 Save Profile",
        use_container_width=True,
    )

if submitted:

    profile_data = {
        "age": age,
        "gender": gender,
        "height": height,
        "weight": weight,
        "goal": goal,
        "activity": activity,
        "food_preference": food_preference,
        "medical_conditions": medical_conditions.strip(),
    }

    try:

        save_or_update_profile(
            user["id"],
            profile_data,
        )

        st.success("✅ Profile Updated Successfully!")

        st.rerun()

    except Exception as e:

        st.error(e)

st.divider()

st.subheader("📋 Current Profile")

col1, col2 = st.columns(2)

with col1:

    st.metric("👤 Name", user["full_name"])
    st.metric("🎂 Age", profile.get("age") or "-")
    st.metric("📏 Height", f"{profile.get('height') or '-'} cm")
    st.metric("⚖️ Weight", f"{profile.get('weight') or '-'} kg")

with col2:

    st.metric("🎯 Goal", profile.get("goal") or "-")
    st.metric("🏃 Activity", profile.get("activity") or "-")
    st.metric("🥗 Food Preference", profile.get("food_preference") or "-")
    st.metric(
        "⚕️ Medical Conditions",
        profile.get("medical_conditions") or "None",
    )