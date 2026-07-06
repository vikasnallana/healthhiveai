from config.supabase_client import supabase


def save_chat(profile_id: str, role: str, message: str):
    """
    Save one chat message.
    """

    return (
        supabase
        .table("chat_history")
        .insert(
            {
                "profile_id": profile_id,
                "role": role,
                "message": message,
            }
        )
        .execute()
    )


def load_chat(profile_id: str):
    """
    Load all chats for a user.
    """

    response = (
        supabase
        .table("chat_history")
        .select("*")
        .eq("profile_id", profile_id)
        .order("created_at")
        .execute()
    )

    return response.data


def clear_chat(profile_id: str):
    """
    Delete all chats for a user.
    """

    return (
        supabase
        .table("chat_history")
        .delete()
        .eq("profile_id", profile_id)
        .execute()
    )