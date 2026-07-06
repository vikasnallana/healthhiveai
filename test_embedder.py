from utils.health_calculator import *

print(calculate_bmi(170, 74))
print(bmi_category(calculate_bmi(170, 74)))
print(daily_water(74))
print(daily_protein(74, "Muscle Gain"))
print(daily_calories(
    74,
    170,
    22,
    "Male",
    "Lightly Active"
))