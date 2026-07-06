from datetime import date

from config.supabase_client import supabase


def get_today_brief(user_id: str):
    """
    Returns today's AI brief for the logged-in user.
    """

    response = (
        supabase
        .table("daily_briefs")
        .select("*")
        .eq("user_id", user_id)
        .eq("created_date", str(date.today()))
        .limit(1)
        .execute()
    )

    if response.data:
        return response.data[0]

    return None


def save_today_brief(user_id: str, brief: str):
    """
    Saves today's AI brief.
    """

    return (
        supabase
        .table("daily_briefs")
        .insert(
            {
                "user_id": user_id,
                "brief": brief,
            }
        )
        .execute()
    )