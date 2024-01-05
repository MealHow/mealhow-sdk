MEAL_PLAN_PREVIEW_BASE_PROMPT = """[Writing style guideline: return only meal plan in CSV format (semicolon separated): day(number); meal time; meal name; preparation time; calories; protein; carbs; fats]
Please make me a meal plan for a single day. I must hit a {calories_goal}-calorie{protein_goal_prompt} goal. """

MEAL_PLAN_BASE_PROMPT = """[Writing style guideline: return only meal plan in CSV format (semicolon separated): day(number); meal time; meal name; preparation time; calories; protein; carbs; fats]
Please make me a meal plan for a week's worth of meals. I must hit a {calories_goal}-calorie{protein_goal_prompt} goal for each day. """

MEAL_PLAN_CUISINE_PREFERENCES = """The {cuisines} cuisine"""
CUISINE_SINGULAR = """ is preferred. """
CUISINES_LIST_PLURAL = """s are preferred. """
MEAL_PLAN_INGREDIENTS_TO_AVOID = """Avoid the following ingredients: {ingredients}. """
MEAL_PLAN_HEALTH_ISSUES = """Also I have the following health issues: {health_issues}. """
MEAL_PLAN_PROTEIN_GOAL = """ and {protein} of protein"""
MEAL_PLAN_PREPARATION_TIME = """I want to spend {preparation_time} on meal preparation. """

SHOPPING_LIST_MEALS_REQUEST = """[Writing style guideline: return only meal plan in CSV format: product_name; product_category; quantity]
Available product categories: "fruits", "vegetables", "canned goods", "dairy", "meat", "fish & seafood", "deli", "condiments & spices", "snacks", "bread & bakery", "beverages", "pasta, rice & cereal", "baking", "frozen foods", "other".
Give me detailed shopping list for the following meal plan:
{meal_plan}
"""
SHOPPING_LIST_INGREDIENTS_REQUEST = """[Writing style guideline: return only meal plan in CSV format: product_name; product_category; quantity]
Available product categories: "fruits", "vegetables", "canned goods", "dairy", "meat", "fish & seafood", "deli", "condiments & spices", "snacks", "bread & bakery", "beverages", "pasta, rice & cereal", "baking", "frozen foods", "other".
Give me a detailed shopping list for the following ingredients:
{ingredients}
"""

MEAL_IMAGE_PROMPT = """Professional food picture of {meal_name} meal on the kitchen table"""
MEAL_RECIPE_REQUEST = """Tell me the ingredients and recipe for {meal}. Use markdown format and put the ingredients at the top of the response."""
