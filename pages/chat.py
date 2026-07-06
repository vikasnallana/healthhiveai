import streamlit as st

from agents.manager_agent import manager_agent
from services.profile_service import get_latest_profile
from services.chat_service import (
    save_chat,
    load_chat,
    clear_chat,
)

st.set_page_config(
    page_title="HealthHive AI",
    page_icon="🤖",
)

st.title("🤖 HealthHive AI Assistant")

st.write(
    "Ask anything about nutrition, workouts, sleep, fitness, or general health."
)

# ======================================================
# Load User Profile
# ======================================================

if "profile" not in st.session_state:
    st.session_state.profile = get_latest_profile()

profile = st.session_state.profile

if not profile:
    st.warning("⚠️ Please complete your profile first.")
    st.stop()

profile_id = profile["id"]

# ======================================================
# Clear Chat
# ======================================================

col1, col2 = st.columns([8, 2])

with col2:

    if st.button("🗑️ Clear Chat", use_container_width=True):

        clear_chat(profile_id)

        st.session_state.messages = []

        st.rerun()

# ======================================================
# Load Chat History (Only Once)
# ======================================================

if "messages" not in st.session_state:

    history = load_chat(profile_id)

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

prompt = st.chat_input("Ask HealthHive AI anything...")

if prompt:

    # ---------------- User Message ---------------- #

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    save_chat(
        profile_id=profile_id,
        role="user",
        message=prompt,
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # ---------------- AI Response ---------------- #

    with st.chat_message("assistant"):

        with st.spinner("🧠 HealthHive AI is thinking..."):

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
        profile_id=profile_id,
        role="assistant",
        message=response,
    )

    st.rerun()