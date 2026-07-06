from config.supabase_client import supabase


def get_latest_profile():
    """
    Returns the most recently saved profile.
    """

    response = (
        supabase
        .table("profiles")
        .select("*")
        .order("created_at", desc=True)
        .limit(1)
        .execute()
    )

    if response.data:
        return response.data[0]

    return None


def save_or_update_profile(profile_data: dict):
    """
    Inserts a new profile if none exists,
    otherwise updates the existing profile.
    """

    existing = get_latest_profile()

    if existing:

        response = (
            supabase
            .table("profiles")
            .update(profile_data)
            .eq("id", existing["id"])
            .execute()
        )

    else:

        response = (
            supabase
            .table("profiles")
            .insert(profile_data)
            .execute()
        )

    return response