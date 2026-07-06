import streamlit as st
from agents.manager_agent import manager_agent
st.set_page_config(
    page_title="Dashboard",
    page_icon="🏥",
    layout="wide"
)

# ---------------- HEADER ---------------- #

st.title("🏥 HealthHive AI")

st.markdown("### 👋 Good Afternoon!")

st.write("Welcome back to your Personal AI Health Coach.")

st.divider()

# ---------------- TODAY'S AI BRIEF ---------------- #

st.subheader("🤖 Today's AI Brief")

col1, col2 = st.columns(2)

with col1:
    st.info("🥣 **Breakfast**\n\nOats + Milk + Banana")

    st.info("🍛 **Lunch**\n\nRice + Chicken + Vegetables")

    st.info("🍎 **Evening Snack**\n\nApple + Nuts")

with col2:
    st.info("🏋 **Workout**\n\nPush Day - 45 Minutes")

    st.info("💧 **Water Goal**\n\nDrink 3 Litres")

    st.info("😴 **Sleep Goal**\n\nSleep before 11 PM")

st.divider()

# ---------------- AI CHAT ---------------- #



st.divider()

st.subheader("💬 AI Health Chat")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask your health question..."):

    # User message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # AI Response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = manager_agent(prompt)
            st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )
st.divider()

# ---------------- QUICK SUGGESTIONS ---------------- #

# st.subheader("✨ Today's Health Suggestions")

# st.success("🥗 Eat at least 120g of protein today.")

# st.success("🚶 Walk at least 6000 steps.")

# st.success("💧 Drink 3 litres of water.")

# st.success("😴 Sleep for 7–8 hours.")

# st.success("🏋 Complete today's workout.")

# st.divider()

# ---------------- FOOTER ---------------- #

st.caption("HealthHive AI • Powered by Gemini + CrewAI + RAG")