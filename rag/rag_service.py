from services.gemini_service import ask_gemini
from rag.retriever import retrieve_context


def ask_rag(
    query: str,
    collection_name: str,
    profile: dict | None = None,
) -> str:
    """
    Retrieves relevant context from ChromaDB and
    generates a personalized response using
    the user's profile and retrieved knowledge.
    """

    # Retrieve relevant chunks
    context = retrieve_context(
        query=query,
        collection_name=collection_name,
    )

    context = "\n\n".join(context)

    # ---------------- Profile Context ---------------- #

    profile_context = ""

    if profile:

        profile_context = f"""
User Profile

Name: {profile.get("full_name", "")}
Age: {profile.get("age", "")}
Gender: {profile.get("gender", "")}
Height: {profile.get("height", "")} cm
Weight: {profile.get("weight", "")} kg
Goal: {profile.get("goal", "")}
Activity Level: {profile.get("activity", "")}
Food Preference: {profile.get("food_preference", "")}
Medical Conditions: {profile.get("medical_conditions") or "None"}
"""

    # ---------------- Prompt ---------------- #

    prompt = f"""
You are HealthHive AI, an expert AI Health Coach.

You have access to:

1. The user's health profile.
2. A trusted health knowledge base.

Instructions:

- Always personalize your answer using the user's profile whenever it is available.
- Use the retrieved context as your PRIMARY source of information.
- If the context partially answers the question, combine it with your general health knowledge.
- Never generate unsafe medical advice.
- If the context does not fully answer the question, provide safe general guidance while clearly prioritizing the retrieved information.
- Keep the answer practical, structured, and easy to understand.
- Use bullet points whenever appropriate.

{profile_context}

==========================
Retrieved Knowledge
==========================

{context}

==========================
User Question
==========================

{query}

Answer:
"""

    return ask_gemini(prompt)