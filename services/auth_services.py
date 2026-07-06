from config.supabase_client import supabase


def signup_user(email: str, password: str):
    try:
        supabase.auth.sign_up(
            {
                "email": email,
                "password": password,
            }
        )

        return (
            True,
            "Account created successfully! Please check your email to verify your account.",
        )

    except Exception as e:
        return False, str(e)


def login_user(email: str, password: str):
    try:
        response = supabase.auth.sign_in_with_password(
            {
                "email": email,
                "password": password,
            }
        )

        return True, response.user

    except Exception as e:
        return False, str(e)


def logout_user():
    try:
        supabase.auth.sign_out()
        return True, "Logged out successfully."

    except Exception as e:
        return False, str(e)