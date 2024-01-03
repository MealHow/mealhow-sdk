from enum import Enum


class BiologicalSex(str, Enum):
    male = "male"
    female = "female"


class MeasurementSystem(str, Enum):
    imperial = "imperial"
    metric = "metric"


class Goal(str, Enum):
    build_muscles = "build muscles"
    lose_weight = "lose weight"
    eat_healthy = "eat healthy"


class ActivityLevel(str, Enum):
    sedentary = "Sedentary (little or no exercise)"
    light = "Lightly active (light exercise/sports 1-3 days/week)"
    moderate = "Moderately active (moderate exercise/sports 3-5 days/week)"
    high = "Very active (hard exercise/sports 6-7 days a week)"
    extra = "Extra active (very hard exercise/sports and a physical job)"


class MealPrepTime(str, Enum):
    up_to_30_min = "up to 30 minutes"
    up_to_60_min = "up to 60 minutes"


class Cuisine(str, Enum):
    mediterranean = "mediterranean"
    asian = "asian"
    mexican = "mexican"
    italian = "italian"
    middle_eastern = "middle_eastern"
    indian = "indian"
    eastern_european = "eastern european"


class IngredientsToAvoid(str, Enum):
    beef = "beef"
    fish = "fish"
    pork = "pork"
    shellfish = "shellfish"
    lamb = "lamb"
    poultry = "poultry"
    dairy = "dairy"
    eggs = "eggs"
    nuts = "nuts"
    gluten = "gluten"


class HealthIssue(str, Enum):
    type_1_diabetes = "type 1 diabetes"
    type_2_diabetes = "type 2 diabetes"
    high_blood_pressure = "high blood pressure"


class ProteinGoal(str, Enum):
    moderate = "90 to 120 grams"
    high = "more than 120 grams"


class Platform(str, Enum):
    web = "web"
    ios = "ios"
    android = "android"


class MealPlanStatus(str, Enum):
    in_progress = "in_progress"
    failed = "failed"
    active = "active"
    archived = "archived"


class JobStatus(str, Enum):
    in_progress = "in_progress"
    failed = "failed"
    active = "active"
