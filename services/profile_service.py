from config.supabase_client import supabase


def get_profile(user_id: str):
    """
    Returns the logged-in user's profile.
    """

    response = (
        supabase.table("profiles")
        .select("*")
        .eq("user_id", user_id)
        .limit(1)
        .execute()
    )

    if response.data:
        return response.data[0]

    return None


def save_or_update_profile(
    user_id: str,
    profile_data: dict,
):
    """
    Saves or updates the user's profile.
    """

    existing = get_profile(user_id)

    profile_data["user_id"] = user_id

    if existing:

        response = (
            supabase.table("profiles")
            .update(profile_data)
            .eq("user_id", user_id)
            .execute()
        )

    else:

        response = (
            supabase.table("profiles")
            .insert(profile_data)
            .execute()
        )

    return response


def update_profile(
    user_id: str,
    profile_data: dict,
):
    """
    Updates an existing profile.
    """

    return (
        supabase.table("profiles")
        .update(profile_data)
        .eq("user_id", user_id)
        .execute()
    )