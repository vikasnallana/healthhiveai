import streamlit as st

from services.profile_service import (
    save_or_update_profile,
    get_latest_profile,
)

st.set_page_config(
    page_title="My Profile",
    page_icon="👤",
)

st.title("👤 My Health Profile")

st.write(
    "Update your personal information to receive personalized AI recommendations."
)

# =====================================================
# Load Existing Profile
# =====================================================

existing_profile = get_latest_profile()

if existing_profile is None:
    existing_profile = {}

# =====================================================
# Options
# =====================================================

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

# =====================================================
# Profile Form
# =====================================================

with st.form("profile_form"):

    name = st.text_input(
        "Full Name",
        value=existing_profile.get("full_name", ""),
    )

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=int(existing_profile.get("age", 18)),
        step=1,
    )

    gender = st.selectbox(
        "Gender",
        gender_options,
        index=gender_options.index(
            existing_profile.get("gender", "Male")
        ),
    )

    height = st.number_input(
        "Height (cm)",
        min_value=50,
        max_value=250,
        value=int(existing_profile.get("height", 170)),
        step=1,
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=20,
        max_value=300,
        value=int(existing_profile.get("weight", 60)),
        step=1,
    )

    goal = st.selectbox(
        "Fitness Goal",
        goal_options,
        index=goal_options.index(
            existing_profile.get("goal", "General Fitness")
        ),
    )

    activity = st.selectbox(
        "Activity Level",
        activity_options,
        index=activity_options.index(
            existing_profile.get("activity", "Sedentary")
        ),
    )

    food_preference = st.selectbox(
        "Food Preference",
        food_options,
        index=food_options.index(
            existing_profile.get("food_preference", "Vegetarian")
        ),
    )

    medical_conditions = st.text_area(
        "Medical Conditions (Optional)",
        value=existing_profile.get(
            "medical_conditions",
            "",
        ),
    )

    submitted = st.form_submit_button(
        "💾 Save Profile",
        use_container_width=True,
    )

    if submitted:

        profile = {
            "full_name": name.strip(),
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

            save_or_update_profile(profile)

            st.success("✅ Profile updated successfully!")

            st.rerun()

        except Exception as e:

            st.error(f"❌ {e}")

# =====================================================
# Display Profile
# =====================================================

st.divider()

profile = get_latest_profile()

if profile:

    st.subheader("📋 Current Profile")

    col1, col2 = st.columns(2)

    with col1:

        st.metric("👤 Name", profile["full_name"])
        st.metric("🎂 Age", profile["age"])
        st.metric("📏 Height", f"{profile['height']} cm")
        st.metric("⚖️ Weight", f"{profile['weight']} kg")

    with col2:

        st.metric("🎯 Goal", profile["goal"])
        st.metric("🏃 Activity", profile["activity"])
        st.metric("🥗 Food Preference", profile["food_preference"])
        st.metric(
            "⚕️ Medical Conditions",
            profile["medical_conditions"] or "None",
        )

else:

    st.info("No profile found. Please create your profile.")