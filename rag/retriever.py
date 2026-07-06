from rag.vector_store import get_collection
from rag.embedder import generate_embedding


def retrieve_context(
    query: str,
    collection_name: str,
    top_k: int = 5
):
    """
    Retrieves the most relevant chunks
    from ChromaDB.
    """

    collection = get_collection(collection_name)

    query_embedding = generate_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results["documents"][0]