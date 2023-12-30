import re

from .enums import ActivityLevel, BiologicalSex, Goal


async def str_to_int(raw_data: str) -> int:
    data = raw_data.strip().split(".")[0]
    return int("".join([i for i in data if i.isdigit()]))


def to_snake_case(str_value: str) -> str:
    str_value = str_value.lower()
    str_value = re.sub(r"\W+", "_", str_value)
    return str_value.strip("_")


def get_bmi(weight: int, height: int) -> float:
    return round((weight / (height**2)) * 10000, 1)


def convert_weight_to_metric(weight: int) -> int:
    return int(round(0.453592 * weight))


def convert_height_to_metric(height: int) -> int:
    return int(round(2.54 * height))


def convert_weight_to_imperial(weight: int) -> int:
    return int(round(2.20462 * weight))


def convert_height_to_imperial(height: int) -> int:
    return int(round(0.393701 * height))


def get_basal_metabolic_rate_harris_benedict(weight: int, height: int, age: int, sex: BiologicalSex) -> int:
    if sex == BiologicalSex.male.value:
        return int(round(66.5 + 13.75 * weight + 5.003 * height - 6.75 * age))
    else:
        return int(round(655.1 + 9.563 * weight + 1.85 * height - 4.676 * age))


def get_basal_metabolic_rate_mifflin_st_jeor(weight: int, height: int, age: int, sex: str) -> int:
    if sex == BiologicalSex.male.value:
        return int(round(10 * weight + 6.25 * height - 5 * age + 5))
    else:
        return int(round(10 * weight + 6.25 * height - 5 * age - 161))


def get_calories_goal_by_activity_level(bmr_value: int, activity_level: str) -> int:
    if activity_level == ActivityLevel.sedentary.value:
        return int(round(bmr_value * 1.2))
    elif activity_level == ActivityLevel.light.value:
        return int(round(bmr_value * 1.375))
    elif activity_level == ActivityLevel.moderate.value:
        return int(round(bmr_value * 1.55))
    elif activity_level == ActivityLevel.high.value:
        return int(round(bmr_value * 1.725))

    return int(round(bmr_value * 1.9))


def get_calories_goal_by_goal_type(bmr_value: int, goal_type: str) -> int:
    if goal_type == Goal.lose_weight.value:
        return int(round(bmr_value * 0.8))
    elif goal_type == Goal.build_muscle.value:
        return int(round(bmr_value * 1.1))

    return int(round(bmr_value))


def round_calories_goal_to_nearest_100(calories_goal: int) -> int:
    return int(round(calories_goal / 100.0)) * 100
