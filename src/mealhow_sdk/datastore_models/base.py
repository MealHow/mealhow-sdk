from google.cloud import ndb


class BaseModel(ndb.Model):
    def to_dict(self):
        result = super(BaseModel, self).to_dict()
        result['key'] = self.key.id()
        return result
