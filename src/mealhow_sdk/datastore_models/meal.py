from google.cloud import ndb

from .user import User


class MealImage(ndb.Model):
    images = ndb.JsonProperty()
    created_at = ndb.DateTimeProperty(auto_now_add=True)


class MealRecipe(ndb.Model):
    recipe = ndb.TextProperty()
    created_at = ndb.DateTimeProperty(auto_now_add=True)


class Meal(ndb.Model):
    full_name = ndb.StringProperty(indexed=True)
    calories = ndb.IntegerProperty()
    protein = ndb.IntegerProperty()
    carbs = ndb.IntegerProperty()
    fats = ndb.IntegerProperty()
    image_key = ndb.KeyProperty(kind=MealImage)
    recipe_key = ndb.KeyProperty(kind=MealRecipe, indexed=True)
    created_at = ndb.DateTimeProperty(auto_now_add=True)


class FavoriteMeal(ndb.Model):
    meal_key = ndb.KeyProperty(kind=Meal, indexed=True)
    user_key = ndb.KeyProperty(kind=User, indexed=True)
    created_at = ndb.DateTimeProperty(auto_now_add=True)
    deleted_at = ndb.DateTimeProperty()
