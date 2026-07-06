from services.gemini_service import ask_gemini


def progress_agent(user_query: str) -> str:
    """
    Tracks and analyzes user progress.
    """

    prompt = f"""
You are a Health Progress Coach.

Rules:
- Encourage consistency.
- Motivate the user.
- Suggest improvements.
- Give progress-based recommendations.

User Question:
{user_query}
"""

    return ask_gemini(prompt)