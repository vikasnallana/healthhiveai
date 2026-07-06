from rag.rag_service import ask_rag


def nutrition_agent(user_query: str) -> str:
    """
    Handles nutrition and diet-related questions
    using the Nutrition RAG knowledge base.
    """

    response = ask_rag(
        query=user_query,
        collection_name="nutrition"
    )

    return "🥗 Nutrition Agent\n\n" + response