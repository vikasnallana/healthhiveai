from services.gemini_service import ask_gemini


def generate_final_report(user_query: str, agent_responses: list[str]) -> str:
    """
    Combines multiple agent responses into one final response.
    """

    combined_response = "\n\n".join(agent_responses)

    prompt = f"""
You are HealthHive AI.

The user asked:

{user_query}

Below are responses from different AI specialists.

{combined_response}

Combine them into ONE final response.

Rules:
- Remove duplicate information.
- Keep it well structured.
- Use headings.
- Keep the answer motivating.
- Give a final summary.
"""

    return ask_gemini(prompt)