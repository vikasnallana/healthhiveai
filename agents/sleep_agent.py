from rag.rag_service import ask_rag


def sleep_agent(
    user_query: str,
    profile: dict | None = None,
) -> str:
    """
    Handles sleep and recovery-related questions
    using the Sleep RAG knowledge base.
    """

    response = ask_rag(
        query=user_query,
        collection_name="sleep",
        profile=profile,
    )

    return "😴 Sleep Agent\n\n" + response