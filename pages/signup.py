import streamlit as st

from services.auth_services import signup_user
from config.supabase_client import supabase

st.title("📝 Create Your HealthHive Account")

with st.form("signup_form"):

    full_name = st.text_input("Full Name")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="password"
    )

    submitted = st.form_submit_button(
        "Create Account",
        use_container_width=True
    )

if submitted:

    # ---------------- Validation ---------------- #

    if not full_name.strip():
        st.error("Please enter your full name.")

    elif not username.strip():
        st.error("Please enter a username.")

    elif len(username) < 4:
        st.error("Username must contain at least 4 characters.")

    elif len(password) < 6:
        st.error("Password must contain at least 6 characters.")

    elif password != confirm_password:
        st.error("Passwords do not match.")

    else:

        success, result = signup_user(
            full_name=full_name,
            username=username,
            password=password,
        )

        if success:

            try:

                # Create empty profile

                supabase.table("profiles").insert(
                    {
                        "user_id": result["id"],
                        "age": None,
                        "gender": None,
                        "height": None,
                        "weight": None,
                        "goal": None,
                        "activity": None,
                        "food_preference": None,
                        "medical_conditions": None,
                    }
                ).execute()

                st.success("✅ Account created successfully!")

                st.info("You can now login.")

            except Exception as e:

                st.error(f"Profile creation failed: {e}")

        else:

            st.error(result)