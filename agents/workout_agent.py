from rag.rag_service import ask_rag


def workout_agent(user_query: str) -> str:
    """
    Handles workout and fitness-related questions
    using the Workout RAG knowledge base.
    """

    response = ask_rag(
        query=user_query,
        collection_name="workout"
    )

    return "💪 Workout Agent\n\n" + response