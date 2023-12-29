from google.cloud import ndb

from .user import User


class ShoppingListItem(ndb.Model):
    name = ndb.StringProperty()
    quantity = ndb.StringProperty()


class ShoppingList(ndb.Model):
    name = ndb.StringProperty(indexed=True)
    user = ndb.KeyProperty(kind=User, indexed=True)
    items = ndb.StructuredProperty(ShoppingListItem, repeated=True)
    created_at = ndb.DateTimeProperty(auto_now_add=True)
    deleted_at = ndb.DateTimeProperty()
