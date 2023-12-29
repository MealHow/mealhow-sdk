from google.cloud import ndb

from .user import User


class MealImageThumbnail(ndb.Model):
    size = ndb.IntegerProperty()
    url = ndb.StringProperty()


class MealImage(ndb.Model):
    images = ndb.StructuredProperty(MealImageThumbnail, repeated=True)
    artifact_reported = ndb.BooleanProperty(default=False)
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
    image = ndb.KeyProperty(kind=MealImage)
    recipe = ndb.KeyProperty(kind=MealRecipe, indexed=True)
    preparation_time = ndb.IntegerProperty()
    created_at = ndb.DateTimeProperty(auto_now_add=True)


class FavoriteMeal(ndb.Model):
    meal = ndb.KeyProperty(kind=Meal, indexed=True)
    user = ndb.KeyProperty(kind=User, indexed=True)
    created_at = ndb.DateTimeProperty(auto_now_add=True)
    deleted_at = ndb.DateTimeProperty()
