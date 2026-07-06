import streamlit as st

from agents.manager_agent import manager_agent

from services.core_serive import (
    require_login,
    get_current_profile,
    is_profile_complete,
)

from services.chat_service import (
    save_chat,
    load_chat,
    clear_chat,
)

st.set_page_config(
    page_title="HealthHive AI",
    page_icon="🤖",
)

# ======================================================
# Authentication
# ======================================================

user = require_login()
profile = get_current_profile()

st.title("🤖 HealthHive AI Assistant")

st.write(
    f"Hello **{user['full_name']}** 👋\n\n"
    "Ask anything about nutrition, workouts, sleep, fitness or general health."
)

# ======================================================
# Check Profile Completion
# ======================================================

if not is_profile_complete(profile):

    st.warning(
        "⚠️ Please complete your health profile before chatting with HealthHive AI."
    )

    st.page_link(
        "pages/profile.py",
        label="👤 Complete Profile",
        icon="👤",
    )

    st.stop()

user_id = user["id"]

# ======================================================
# Initialize Session State
# ======================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# ======================================================
# Clear Chat
# ======================================================

col1, col2 = st.columns([8, 2])

with col2:

    if st.button(
        "🗑️ Clear Chat",
        use_container_width=True,
    ):

        clear_chat(user_id)

        st.session_state.messages = []

        st.rerun()

# ======================================================
# Load Chat History
# ======================================================

if len(st.session_state.messages) == 0:

    history = load_chat(user_id)

    st.session_state.messages = [

        {
            "role": chat["role"],
            "content": chat["message"],
        }

        for chat in history
    ]

# ======================================================
# Display Previous Messages
# ======================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# ======================================================
# Chat Input
# ======================================================

prompt = st.chat_input(
    "Ask HealthHive AI anything..."
)

if prompt:

    # ---------------- User Message ---------------- #

    st.session_state.messages.append(

        {
            "role": "user",
            "content": prompt,
        }

    )

    save_chat(
        user_id=user_id,
        role="user",
        message=prompt,
    )

    with st.chat_message("user"):

        st.markdown(prompt)

    # ---------------- AI Response ---------------- #

    with st.chat_message("assistant"):

        with st.spinner(
            "🧠 HealthHive AI is thinking..."
        ):

            response = manager_agent(
                user_query=prompt,
                profile=profile,
            )

            st.markdown(response)

    st.session_state.messages.append(

        {
            "role": "assistant",
            "content": response,
        }

    )

    save_chat(
        user_id=user_id,
        role="assistant",
        message=response,
    )

    st.rerun()