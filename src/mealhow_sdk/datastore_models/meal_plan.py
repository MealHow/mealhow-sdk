from google.cloud import ndb

from .base import BaseModel
from .user import User


class MealPlanItem(BaseModel):
    id = ndb.StringProperty()
    meal_name = ndb.StringProperty()
    meal_time = ndb.StringProperty()
    day = ndb.IntegerProperty()
    preparation_time = ndb.IntegerProperty()
    calories = ndb.IntegerProperty()
    protein = ndb.IntegerProperty()
    carbs = ndb.IntegerProperty()
    fats = ndb.IntegerProperty()


class MealPlanDayTotalInfo(BaseModel):
    calories = ndb.IntegerProperty()
    protein = ndb.IntegerProperty()
    carbs = ndb.IntegerProperty()
    fats = ndb.IntegerProperty()


class MealPlanDayItem(BaseModel):
    meals = ndb.LocalStructuredProperty(MealPlanItem, repeated=True)
    total = ndb.LocalStructuredProperty(MealPlanDayTotalInfo)


class MealPlanDetails(BaseModel):
    day_1 = ndb.LocalStructuredProperty(MealPlanDayItem)
    day_2 = ndb.LocalStructuredProperty(MealPlanDayItem)
    day_3 = ndb.LocalStructuredProperty(MealPlanDayItem)
    day_4 = ndb.LocalStructuredProperty(MealPlanDayItem)
    day_5 = ndb.LocalStructuredProperty(MealPlanDayItem)
    day_6 = ndb.LocalStructuredProperty(MealPlanDayItem)
    day_7 = ndb.LocalStructuredProperty(MealPlanDayItem)


class MealPlan(BaseModel):
    status = ndb.StringProperty(indexed=True)
    user = ndb.KeyProperty(kind=User, indexed=True)
    meal_swaps = ndb.IntegerProperty(default=0)
    details = ndb.StructuredProperty(MealPlanDetails)
    created_at = ndb.DateTimeProperty(auto_now_add=True, indexed=True)
