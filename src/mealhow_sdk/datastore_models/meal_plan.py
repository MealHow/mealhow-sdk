from google.cloud import ndb

from .user import User


class MealPlanItem(ndb.Model):
    id = ndb.StringProperty()
    meal_name = ndb.StringProperty()
    meal_time = ndb.StringProperty()
    day = ndb.IntegerProperty()
    preparation_time = ndb.StringProperty()
    calories = ndb.IntegerProperty()
    protein = ndb.IntegerProperty()
    carbs = ndb.IntegerProperty()
    fats = ndb.IntegerProperty()


class MealPlanDayTotalInfo(ndb.Model):
    calories = ndb.IntegerProperty()
    protein = ndb.IntegerProperty()
    carbs = ndb.IntegerProperty()
    fats = ndb.IntegerProperty()


class MealPlanDayItem(ndb.Model):
    meals = ndb.LocalStructuredProperty(MealPlanItem, repeated=True)
    total = ndb.LocalStructuredProperty(MealPlanDayTotalInfo)


class MealPlanDetails(ndb.Model):
    day_1 = ndb.LocalStructuredProperty(MealPlanDayItem)
    day_2 = ndb.LocalStructuredProperty(MealPlanDayItem)
    day_3 = ndb.LocalStructuredProperty(MealPlanDayItem)
    day_4 = ndb.LocalStructuredProperty(MealPlanDayItem)
    day_5 = ndb.LocalStructuredProperty(MealPlanDayItem)
    day_6 = ndb.LocalStructuredProperty(MealPlanDayItem)
    day_7 = ndb.LocalStructuredProperty(MealPlanDayItem)


class MealPlan(ndb.Model):
    active = ndb.BooleanProperty(default=True, indexed=True)
    user = ndb.KeyProperty(kind=User, indexed=True)
    details = ndb.StructuredProperty(MealPlanDetails)
    created_at = ndb.DateTimeProperty(auto_now_add=True)
    deleted_at = ndb.DateTimeProperty()
