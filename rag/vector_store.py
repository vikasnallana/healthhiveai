import chromadb

client = chromadb.PersistentClient(
    path="data/embeddings"
)


def get_collection(collection_name: str):
    """
    Returns a ChromaDB collection.
    """

    return client.get_collection(collection_name)