from datetime import datetime
from bson.objectid import ObjectId
from pydantic import BaseModel, Field, ValidationError


class ObjectIdStr(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, (str, ObjectId)):
            raise ValidationError('_id must be a string or ObjectId instance!')
        return str(v)


class Model(BaseModel):
    id: ObjectIdStr = Field(alias='_id')
    created_at: datetime = Field(datetime.now())
    updated_at: datetime = Field(datetime.now())
