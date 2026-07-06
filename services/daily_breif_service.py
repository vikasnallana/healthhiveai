from datetime import date

from config.supabase_client import supabase


def get_today_brief(profile_id: str):

    response = (
        supabase
        .table("daily_briefs")
        .select("*")
        .eq("profile_id", profile_id)
        .eq("created_date", str(date.today()))
        .limit(1)
        .execute()
    )

    if response.data:
        return response.data[0]

    return None


def save_today_brief(profile_id: str, brief: str):

    return (
        supabase
        .table("daily_briefs")
        .insert(
            {
                "profile_id": profile_id,
                "brief": brief,
            }
        )
        .execute()
    )