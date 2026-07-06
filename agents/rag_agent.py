from rag.rag_service import ask_rag


def rag_agent(
    user_query: str,
    collection_name: str = "medical"
) -> str:
    """
    RAG-powered medical knowledge agent.
    """

    return ask_rag(
        query=user_query,
        collection_name=collection_name
    )