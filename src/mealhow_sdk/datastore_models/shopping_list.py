from google.cloud import ndb

from models.user import User


class ShoppingList(ndb.Model):
    user_key = ndb.KeyProperty(kind=User, indexed=True)
    details = ndb.JsonProperty()
    created_at = ndb.DateTimeProperty(auto_now_add=True)
    deleted_at = ndb.DateTimeProperty()
