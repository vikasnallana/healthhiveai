import streamlit as st

from services.auth_services import get_current_user

st.set_page_config(
    page_title="HealthHive AI",
    page_icon="🏥",
    layout="wide",
)

# ---------------- Public Pages ---------------- #

home_page = st.Page(
    "pages/home.py",
    title="Home",
    icon="🏠",
    default=True,
)

signup_page = st.Page(
    "pages/signup.py",
    title="Signup",
    icon="📝",
)

login_page = st.Page(
    "pages/login.py",
    title="Login",
    icon="🔑",
)

# ---------------- Private Pages ---------------- #

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
    title="AI Chat",
    icon="🤖",
)

logout_page = st.Page(
    "pages/logout.py",
    title="Logout",
    icon="🚪",
)

# ---------------- Authentication ---------------- #

user = get_current_user()

if user:

    pages = [
        dashboard_page,
        profile_page,
        chat_page,
        logout_page,
    ]

else:

    pages = [
        home_page,
        signup_page,
        login_page,
    ]

pg = st.navigation(pages)

pg.run()