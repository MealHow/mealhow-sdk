from google.cloud import ndb

from .base import BaseModel
from .meal import Meal
from .user import User


class ShoppingListItem(BaseModel):
    name = ndb.StringProperty()
    quantity = ndb.StringProperty()


class ShoppingList(BaseModel):
    name = ndb.StringProperty(indexed=True)
    status = ndb.StringProperty(indexed=True)
    user = ndb.KeyProperty(kind=User, indexed=True)
    items = ndb.StructuredProperty(ShoppingListItem, repeated=True)
    linked_meals = ndb.KeyProperty(kind=Meal, repeated=True)
    created_at = ndb.DateTimeProperty(auto_now_add=True, indexed=True)
    deleted_at = ndb.DateTimeProperty(indexed=True)
