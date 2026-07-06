from rag.rag_service import ask_rag


def workout_agent(
    user_query: str,
    profile: dict | None = None,
) -> str:
    """
    Handles workout and fitness-related questions
    using the Workout RAG knowledge base.
    """

    response = ask_rag(
        query=user_query,
        collection_name="workout",
        profile=profile,
    )

    return "💪 Workout Agent\n\n" + response