from rag.retriever import retrieve_context

results = retrieve_context(
    query="basic workout for abs",
    collection_name="workout"
)

for i, chunk in enumerate(results, start=1):
    print("=" * 80)
    print(f"Chunk {i}")
    print("=" * 80)
    print(chunk)
    print()