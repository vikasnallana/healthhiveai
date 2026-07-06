import streamlit as st

from services.profile_service import save_profile, get_profile

st.title("👤 My Health Profile")

st.write("Fill in your details to receive personalized health recommendations.")

with st.form("profile_form"):

    name = st.text_input("Full Name")

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        step=1
    )

    gender = st.selectbox(
        "Gender",
        [
            "Male",
            "Female",
            "Other"
        ]
    )

    height = st.number_input(
        "Height (cm)",
        min_value=50,
        max_value=250,
        step=1
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=20,
        max_value=300,
        step=1
    )

    goal = st.selectbox(
        "Fitness Goal",
        [
            "Weight Loss",
            "Muscle Gain",
            "Maintain Weight",
            "General Fitness"
        ]
    )

    activity = st.selectbox(
        "Activity Level",
        [
            "Sedentary",
            "Lightly Active",
            "Moderately Active",
            "Very Active"
        ]
    )

    food_preference = st.selectbox(
        "Food Preference",
        [
            "Vegetarian",
            "Non-Vegetarian",
            "Vegan"
        ]
    )

    medical_conditions = st.text_area(
        "Medical Conditions (Optional)"
    )

    submitted = st.form_submit_button("💾 Save Profile")

    if submitted:

        profile = {
            "name": name,
            "age": age,
            "gender": gender,
            "height": height,
            "weight": weight,
            "goal": goal,
            "activity": activity,
            "food_preference": food_preference,
            "medical_conditions": medical_conditions,
        }

        save_profile(profile)

        st.success("✅ Profile saved successfully!")

st.divider()

st.subheader("📋 Saved Profile")

profile = get_profile()

if profile:
    st.json(profile)
else:
    st.info("No profile saved yet.")