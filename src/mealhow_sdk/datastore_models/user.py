from google.cloud import ndb


class WeightRecord(ndb.Model):
    weight_lbs = ndb.IntegerProperty()
    weight_kg = ndb.IntegerProperty()
    bmi = ndb.FloatProperty()
    created_at = ndb.DateTimeProperty(auto_now_add=True)


class User(ndb.Model):
    email = ndb.StringProperty(indexed=True)
    age = ndb.DateProperty()
    biological_sex = ndb.StringProperty()
    meal_prep_time = ndb.StringProperty()
    activity_level = ndb.StringProperty()
    measurement_system = ndb.StringProperty()
    height_inches = ndb.IntegerProperty()
    height_cm = ndb.IntegerProperty()
    goal = ndb.StringProperty()
    current_weight = ndb.StructuredProperty(WeightRecord, repeated=True)
    weight_goal = ndb.StructuredProperty(WeightRecord, repeated=True)
    bmr = ndb.IntegerProperty()
    calories_goal = ndb.IntegerProperty()
    protein_goal = ndb.StringProperty()
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
    country = ndb.StringProperty(indexed=True)
    country_subdivision = ndb.StringProperty(indexed=True)
    client_protocol = ndb.StringProperty()
    platform = ndb.StringProperty()
    timezone = ndb.StringProperty()
