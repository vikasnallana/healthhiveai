def calculate_bmi(height_cm, weight_kg):
    """
    Calculate Body Mass Index (BMI).
    """
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)


def bmi_category(bmi):
    """
    Return BMI category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def daily_water(weight):
    """
    Daily water intake in liters.
    """
    return round(weight * 0.035, 1)


def daily_protein(weight, goal):
    """
    Protein recommendation.
    """
    if goal == "Muscle Gain":
        return round(weight * 1.8)

    if goal == "Weight Loss":
        return round(weight * 1.6)

    return round(weight * 1.2)


def daily_calories(weight, height, age, gender, activity):
    """
    Estimate maintenance calories using the Mifflin-St Jeor equation.
    """

    if gender == "Male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    activity_multiplier = {
        "Sedentary": 1.2,
        "Lightly Active": 1.375,
        "Moderately Active": 1.55,
        "Very Active": 1.725
    }

    calories = bmr * activity_multiplier.get(activity, 1.2)

    return round(calories)