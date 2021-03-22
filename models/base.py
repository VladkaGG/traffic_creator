from datetime import datetime
from bson.objectid import ObjectId
from pydantic import BaseModel, BaseConfig, Field, ValidationError


class ObjectIdStr(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, (str, ObjectId)):
            raise ValidationError('_id must be a string or ObjectId instance!')
        return ObjectId(str(v))


class Model(BaseModel):
    id: ObjectIdStr = Field(alias='_id')
    created_at: datetime = Field(datetime.now())
    updated_at: datetime = Field(datetime.now())

    class Config(BaseConfig):
        allow_population_by_field_name = True
        json_encoders = {
            datetime: lambda dt: dt.isoformat(),
            ObjectId: lambda oid: str(oid),
        }
