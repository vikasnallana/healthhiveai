from services.gemini_service import ask_gemini

from agents.nutrition_agent import nutrition_agent
from agents.workout_agent import workout_agent
from agents.sleep_agent import sleep_agent
from agents.progress_agent import progress_agent
from agents.rag_agent import rag_agent
from agents.report_generator import generate_final_report


def manager_agent(user_query: str, profile: dict | None = None) -> str:
    """
    Routes the user's query to the appropriate AI agent.
    """

    query = user_query.lower()

    # ---------------- Nutrition Keywords ---------------- #

    nutrition_keywords = [
        "diet",
        "food",
        "meal",
        "protein",
        "nutrition",
        "calories",
        "breakfast",
        "lunch",
        "dinner",
        "weight gain",
        "weight loss",
    ]

    # ---------------- Workout Keywords ---------------- #

    workout_keywords = [
        "workout",
        "exercise",
        "gym",
        "push",
        "pull",
        "legs",
        "fitness",
        "training",
        "muscle",
        "cardio",
        "running",
        "walking",
    ]

    # ---------------- Sleep Keywords ---------------- #

    sleep_keywords = [
        "sleep",
        "insomnia",
        "recovery",
        "rest",
        "fatigue",
        "tired",
    ]

    # ---------------- Progress Keywords ---------------- #

    progress_keywords = [
        "progress",
        "goal",
        "routine",
        "habit",
        "improve",
        "track",
    ]

    # ---------------- Medical / Research Keywords ---------------- #

    rag_keywords = [
        "who",
        "icmr",
        "research",
        "study",
        "medical",
        "medicine",
        "disease",
        "guidelines",
        "evidence",
        "hypertension",
        "diabetes",
    ]

    # ---------------- Complex Health Goals ---------------- #

    complex_keywords = [
        "lose weight",
        "weight loss",
        "lose belly fat",
        "gain muscle",
        "muscle gain",
        "healthy lifestyle",
        "fitness plan",
        "overall health",
    ]

    # ======================================================
    # Multi-Agent Collaboration
    # ======================================================

    if any(keyword in query for keyword in complex_keywords):

        responses = [
            nutrition_agent(
                user_query=user_query,
                profile=profile,
            ),
            workout_agent(
                user_query=user_query,
                profile=profile,
            ),
            sleep_agent(
                user_query=user_query,
                profile=profile,
            ),
        ]

        return generate_final_report(
            user_query=user_query,
            agent_responses=responses,
        )

    # ======================================================
    # Individual Routing
    # ======================================================

    if any(keyword in query for keyword in nutrition_keywords):
        return nutrition_agent(
            user_query=user_query,
            profile=profile,
        )

    if any(keyword in query for keyword in workout_keywords):
        return workout_agent(
            user_query=user_query,
            profile=profile,
        )

    if any(keyword in query for keyword in sleep_keywords):
        return sleep_agent(
            user_query=user_query,
            profile=profile,
        )

    if any(keyword in query for keyword in progress_keywords):
        return progress_agent(
            user_query=user_query,
            profile=profile,
        )

    if any(keyword in query for keyword in rag_keywords):
        return rag_agent(
            user_query=user_query,
            collection_name="medical",
            profile=profile,
        )

    # ======================================================
    # Default AI Health Coach
    # ======================================================

    profile_context = ""

    if profile:
        profile_context = f"""
User Profile:

Name: {profile.get("full_name", "")}
Age: {profile.get("age", "")}
Gender: {profile.get("gender", "")}
Height: {profile.get("height", "")} cm
Weight: {profile.get("weight", "")} kg
Goal: {profile.get("goal", "")}
Activity Level: {profile.get("activity", "")}
Food Preference: {profile.get("food_preference", "")}
Medical Conditions: {profile.get("medical_conditions", "None")}
"""

    prompt = f"""
You are HealthHive AI.

You are an intelligent personal AI Health Coach.

Always personalize your response using the user's profile whenever it is available.

{profile_context}

User Question:
{user_query}

Provide a practical, professional, and motivating response.
"""

    return ask_gemini(prompt)