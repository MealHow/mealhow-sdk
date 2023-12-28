from google.cloud import ndb


class User(ndb.Model):
    email = ndb.StringProperty(indexed=True)
    birth_date = ndb.DateProperty()
    biological_sex = ndb.StringProperty()
    measurement_system = ndb.StringProperty()
    height_inches = ndb.IntegerProperty()
    height_cm = ndb.IntegerProperty()
    current_weight_lbs = ndb.IntegerProperty()
    current_weight_kg = ndb.IntegerProperty()
    weight_goal_lbs = ndb.IntegerProperty()
    weight_goal_kg = ndb.IntegerProperty()
    calories_goal = ndb.IntegerProperty()
    meal_prep_time = ndb.StringProperty()
    activity_level = ndb.StringProperty()
    avoid_foods = ndb.StringProperty(repeated=True)
    preferred_cuisines = ndb.StringProperty(repeated=True)
    health_conditions = ndb.StringProperty(repeated=True)

    stripe_customer_id = ndb.StringProperty()
    subscription_id = ndb.StringProperty()
    subscription_type = ndb.StringProperty()
    subscribed_at = ndb.DateTimeProperty()
    subscription_active_until = ndb.DateTimeProperty()
    subscription_status = ndb.StringProperty()

    created_at = ndb.DateProperty(auto_now_add=True)
    cdn_cache_id = ndb.StringProperty(indexed=True)
    country_code = ndb.StringProperty(indexed=True)
    client_protocol = ndb.StringProperty()
