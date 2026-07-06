from services.gemini_service import ask_gemini
from rag.retriever import retrieve_context


def ask_rag(
    query: str,
    collection_name: str
) -> str:
    """
    Retrieves relevant context from ChromaDB and
    asks Gemini to answer using that context.
    """

    context = retrieve_context(
        query=query,
        collection_name=collection_name
    )

    context = "\n\n".join(context)

    prompt = f"""
You are HealthHive AI, an expert health assistant.

Below is information retrieved from a trusted health knowledge base.

Use the retrieved context as your PRIMARY source.

Rules:
1. If the context contains the answer, answer using it.
2. If the context only partially answers the question, combine it with your general health knowledge to give a complete and practical answer.
3. Never invent unsafe medical advice.
4. If the question is completely unrelated to the context, politely say that the knowledge base does not contain enough information.

Retrieved Context:
{context}

User Question:
{query}

Provide a clear, well-structured answer with bullet points whenever appropriate.
"""

    return ask_gemini(prompt)