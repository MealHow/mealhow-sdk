import asyncio
from dataclasses import dataclass, field
from typing import Any

from . import external_api, parsers, prompt_templates
from .helpers import to_snake_case


@dataclass
class MealPlanPromptInputData:
    calories_goal: int
    protein_goal: int | None = None
    preparation_time: int | None = None
    preferred_cuisines: list[str] = field(default_factory=lambda: [])
    ingredients_to_avoid: list[str] = field(default_factory=lambda: [])
    health_issues: list[str] = field(default_factory=lambda: [])


async def get_openai_meal_plan_prompt(data: MealPlanPromptInputData) -> str:
    prompt = prompt_templates.MEAL_PLAN_BASE_PROMPT

    if data.protein_goal:
        prompt = prompt.format(
            protein_goal_prompt=prompt_templates.MEAL_PLAN_PROTEIN_GOAL.format(protein=data.protein_goal),
            calories_goal=data.calories_goal,
        )
    else:
        prompt = prompt.format(
            protein_goal_prompt="",
            calories_goal=data.calories_goal,
        )

    if data.preferred_cuisines:
        prompt += prompt_templates.MEAL_PLAN_CUISINE_PREFERENCES.format(
            cuisines=", ".join(data.preferred_cuisines).lower()
        )
        prompt += (
            prompt_templates.CUISINE_SINGULAR
            if len(data.preferred_cuisines) == 1
            else prompt_templates.CUISINES_LIST_PLURAL
        )

    if data.preparation_time:
        prompt += prompt_templates.MEAL_PLAN_PREPARATION_TIME.format(preparation_time=data.preparation_time)

    if data.ingredients_to_avoid:
        prompt += prompt_templates.MEAL_PLAN_INGREDIENTS_TO_AVOID.format(
            ingredients=", ".join(data.ingredients_to_avoid).lower()
        )

    if data.health_issues:
        prompt += prompt_templates.MEAL_PLAN_HEALTH_ISSUES.format(health_issues=", ".join(data.health_issues).lower())

    return prompt


async def calculate_total_daily_micronutrients(
    parsed_diet_plan: list[dict],
) -> dict[int, dict[str, int]]:
    total_daily_micronutrients = {}
    micronutrients = (
        "protein",
        "carbs",
        "fats",
        "calories",
    )

    for i in range(len(parsed_diet_plan)):
        if parsed_diet_plan[i]["day"] not in total_daily_micronutrients:
            total_daily_micronutrients[parsed_diet_plan[i]["day"]] = {name: 0 for name in micronutrients}

        for name in micronutrients:
            total_daily_micronutrients[parsed_diet_plan[i]["day"]][name] += parsed_diet_plan[i][name]

    return total_daily_micronutrients


async def request_meal_plans(request_body: str, gpt_model: str, meal_plans: int = 3) -> list[list[dict]]:
    requests = []
    parsed_meal_plans: list[Any] = []

    async with asyncio.TaskGroup() as tg:
        for _ in range(meal_plans):
            requests.append(tg.create_task(external_api.openai_get_gpt_response(request_body, gpt_model)))

    async with asyncio.TaskGroup() as tg:
        for req in requests:
            parsed_meal_plans.append(tg.create_task(parsers.parse_diet_plan(req.result())))

    for i in range(len(parsed_meal_plans)):
        parsed_meal_plans[i] = parsed_meal_plans[i].result()

    return parsed_meal_plans


async def compound_most_optimal_meal_plan(
    diet_plan_variations: list[list[dict]], daily_calories_goal: int, plan_length: int = 7
) -> dict[int, dict[str, Any]]:
    daily_micronutrients = []
    optimal_meal_plan: dict[int, dict] = {}
    meal_plan_variations_structured: list[dict[int, dict]] = []

    async with asyncio.TaskGroup() as tg:
        for plan in diet_plan_variations:
            daily_micronutrients.append(tg.create_task(calculate_total_daily_micronutrients(plan)))

    for i in range(len(diet_plan_variations)):
        meal_plan: dict[int, dict[str, Any]] = {}
        for meal in diet_plan_variations[i]:
            if (day := meal["day"]) not in meal_plan:
                meal_plan[day] = {
                    "meals": [],
                    "total": daily_micronutrients[i].result()[day],
                }

            meal_plan[day]["meals"].append(meal)

        meal_plan_variations_structured.append(meal_plan)

    daily_calories_goal_diff: dict[int, int] = {k: 9999 for k in range(1, plan_length + 1)}
    for i in range(len(meal_plan_variations_structured)):
        for day in meal_plan_variations_structured[i]:
            day = int(day)
            diff = abs(meal_plan_variations_structured[i][day]["total"]["calories"] - daily_calories_goal)
            if diff < daily_calories_goal_diff[day]:
                optimal_meal_plan[day] = meal_plan_variations_structured[i][day]
                daily_calories_goal_diff[day] = diff

    for day in optimal_meal_plan:
        meals = optimal_meal_plan[day]["meals"]
        for i in range(len(meals)):
            optimal_meal_plan[day]["meals"][i]["id"] = f"{to_snake_case(meals[i]['meal_name'])}-{meals[i]['calories']}"

    return optimal_meal_plan
