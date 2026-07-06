from config.supabase_client import supabase


def save_chat(user_id: str, role: str, message: str):
    """
    Save one chat message for the logged-in user.
    """

    return (
        supabase
        .table("chat_history")
        .insert(
            {
                "user_id": user_id,
                "role": role,
                "message": message,
            }
        )
        .execute()
    )


def load_chat(user_id: str):
    """
    Load chat history of the logged-in user.
    """

    response = (
        supabase
        .table("chat_history")
        .select("*")
        .eq("user_id", user_id)
        .order("created_at")
        .execute()
    )

    return response.data


def clear_chat(user_id: str):
    """
    Delete all chats of the logged-in user.
    """

    return (
        supabase
        .table("chat_history")
        .delete()
        .eq("user_id", user_id)
        .execute()
    )