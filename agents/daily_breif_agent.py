from services.gemini_service import ask_gemini


def daily_brief_agent(profile: dict) -> str:
    """
    Generates a personalized daily health brief.
    """

    prompt = f"""
You are HealthHive AI.

Generate a personalized Daily Health Brief.

User Profile

Name: {profile["full_name"]}
Age: {profile["age"]}
Gender: {profile["gender"]}
Height: {profile["height"]} cm
Weight: {profile["weight"]} kg
Goal: {profile["goal"]}
Activity Level: {profile["activity"]}
Food Preference: {profile["food_preference"]}
Medical Conditions: {profile["medical_conditions"]}

Create today's plan in the following format:

🌞 Good Morning

🥗 Breakfast

🍛 Lunch

🍎 Snacks

🍽️ Dinner

💪 Workout

💧 Water Goal

😴 Sleep Goal

🌟 Motivation

Keep the response concise, practical, and motivating.
"""

    return ask_gemini(prompt)