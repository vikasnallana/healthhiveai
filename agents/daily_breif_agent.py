from services.gemini_service import ask_gemini


def daily_brief_agent(user: dict, profile: dict) -> str:
    """
    Generates a personalized daily health brief.
    """

    prompt = f"""
You are HealthHive AI.

Generate a personalized Daily Health Brief.

User Information

Name: {user["full_name"]}
Username: {user["username"]}

Health Profile

Age: {profile["age"]}
Gender: {profile["gender"]}
Height: {profile["height"]} cm
Weight: {profile["weight"]} kg
Goal: {profile["goal"]}
Activity Level: {profile["activity"]}
Food Preference: {profile["food_preference"]}
Medical Conditions: {profile["medical_conditions"]}

Create today's plan in this format:

🌞 Good Morning

🥗 Breakfast

🍛 Lunch

🍎 Snacks

🍽️ Dinner

💪 Workout

💧 Water Goal

😴 Sleep Goal

🌟 Motivation

Keep the response:
- Personalized
- Practical
- Motivating
- Easy to follow
- Under 400 words.
"""

    return ask_gemini(prompt)