import streamlit as st
from agents.daily_breif_agent import daily_brief_agent
from services.profile_service import get_latest_profile
from utils.health_calculator import (
    calculate_bmi,
    bmi_category,
    daily_calories,
    daily_protein,
    daily_water,
)
from agents.daily_breif_agent import daily_brief_agent

from services.daily_breif_service import (
    get_today_brief,
    save_today_brief,
)
st.title("🏥 HealthHive AI Dashboard")

profile = get_latest_profile()

if not profile:
    st.warning("⚠️ Please create your profile first.")
    st.stop()

# ---------------- USER INFO ---------------- #

st.subheader(f"👋 Welcome, {profile['full_name']}")

st.write("Your personalized AI health dashboard.")

st.divider()

# ---------------- PROFILE SUMMARY ---------------- #

col1, col2, col3, col4 = st.columns(4)

col1.metric("⚖️ Weight", f"{profile['weight']} kg")
col2.metric("📏 Height", f"{profile['height']} cm")
col3.metric("🎯 Goal", profile["goal"])
col4.metric("🏃 Activity", profile["activity"])

st.divider()

# ---------------- HEALTH CALCULATIONS ---------------- #

bmi = calculate_bmi(
    profile["height"],
    profile["weight"],
)

category = bmi_category(bmi)

calories = daily_calories(
    profile["weight"],
    profile["height"],
    profile["age"],
    profile["gender"],
    profile["activity"],
)

protein = daily_protein(
    profile["weight"],
    profile["goal"],
)

water = daily_water(
    profile["weight"],
)

col1, col2, col3, col4 = st.columns(4)

col1.metric("❤️ BMI", bmi)
col2.metric("📊 BMI Status", category)
col3.metric("🔥 Calories", f"{calories} kcal")
col4.metric("💪 Protein", f"{protein} g/day")

st.divider()

col1, col2 = st.columns(2)

col1.metric("💧 Water Intake", f"{water} L/day")
col2.metric("🎂 Age", profile["age"])

st.divider()

# ---------------- AI SUMMARY ---------------- #

st.subheader("🤖 Today's AI Health Brief")

today_brief = get_today_brief(profile["id"])

if today_brief:

    st.success(today_brief["brief"])

else:

    with st.spinner("Generating today's AI brief..."):

        brief = daily_brief_agent(profile)

        save_today_brief(
            profile["id"],
            brief,
        )

    st.success(brief)