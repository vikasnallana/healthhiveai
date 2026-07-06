import streamlit as st

st.set_page_config(
    page_title="HealthHive AI",
    page_icon="🏥",
    layout="wide"
)

home_page = st.Page(
    "pages/home.py",
    title="Home",
    icon="🏠",
    default=True,
)

dashboard_page = st.Page(
    "pages/dashboard.py",
    title="Dashboard",
    icon="📊",
)

profile_page = st.Page(
    "pages/profile.py",
    title="Profile",
    icon="👤",
)
chat_page = st.Page(
    "pages/chat.py",
    title="AI Chat + RAG",
    icon="🤖",
)

pg = st.navigation([
    home_page,
    dashboard_page,
    profile_page,
    chat_page,
])

pg.run()