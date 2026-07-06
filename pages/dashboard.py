import streamlit as st

from services.core_serive import (
    require_login,
    get_current_profile,
    is_profile_complete,
)

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

st.set_page_config(
    page_title="Dashboard",
    page_icon="🏥",
)

# ======================================================
# Authentication
# ======================================================

user = require_login()
profile = get_current_profile()

st.title("🏥 HealthHive AI Dashboard")
st.write(f"Welcome back, **{user['full_name']}** 👋")

# ======================================================
# Profile Completion Check
# ======================================================

if not is_profile_complete(profile):

    st.warning(
        "⚠️ Please complete your health profile before using the dashboard."
    )

    st.page_link(
        "pages/profile.py",
        label="👤 Complete Profile",
        icon="👤",
    )

    st.stop()

# ======================================================
# Profile Summary
# ======================================================

st.subheader("📋 Profile Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric("⚖️ Weight", f"{profile['weight']} kg")
col2.metric("📏 Height", f"{profile['height']} cm")
col3.metric("🎯 Goal", profile["goal"])
col4.metric("🏃 Activity", profile["activity"])

st.divider()

# ======================================================
# Health Metrics
# ======================================================

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

st.subheader("📊 Health Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("❤️ BMI", bmi)
col2.metric("📈 BMI Status", category)
col3.metric("🔥 Daily Calories", f"{calories} kcal")
col4.metric("💪 Protein", f"{protein} g/day")

col1, col2 = st.columns(2)

col1.metric("💧 Water Intake", f"{water} L/day")
col2.metric("🎂 Age", profile["age"])

st.divider()

# ======================================================
# Daily AI Brief
# ======================================================

st.subheader("🧠 Today's AI Health Brief")

today_brief = get_today_brief(user["id"])

if today_brief:

    st.success(today_brief["brief"])

else:

    with st.spinner("Generating today's personalized AI brief..."):

        brief = daily_brief_agent(
            user=user,
            profile=profile,
        )

        save_today_brief(
            user["id"],
            brief,
        )

    st.success(brief)