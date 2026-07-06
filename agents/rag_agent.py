from rag.rag_service import ask_rag


def rag_agent(
    user_query: str,
    collection_name: str = "medical",
    profile: dict | None = None,
) -> str:
    """
    Handles medical and research-based health queries
    using the Medical RAG knowledge base.
    """

    response = ask_rag(
        query=user_query,
        collection_name=collection_name,
        profile=profile,
    )

    return "🩺 Medical Knowledge Agent\n\n" + response