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
    created_at: datetime
    updated_at: datetime


class User(Model):
    email: str
    login: str
    password: str
    monetary_info: dict
    tasks: list[dict]
    phone_number: str


class Task(Model):
    status: str
    app_id: str
    cls_id: str
    cost: float


class App(Model):
    name: str
    description: str
    tasks: list[dict]
    uri: str


class Client(Model):
    login: str
    company_name: str
    photo: bytes
    balance: float
    email: str
    phone_number: str


user = {
    "_id": ObjectId('60565f5c150820e17437f323'),
    "created_at": datetime.now(),
    "updated_at": datetime.now(),
    "email": "somemail@mail.ru",
    "login": "coolguy228",
    "password": "hash",
    "monetary_info": {
        "balance": 100,
        "credit_card": "alphabank"
    },
    "tasks": [{"blabla": "processing", "dada": "done"}],
    "phone_number": "+79142438227"
}

user_obj = User(**user)

print(user_obj.json(by_alias=True))
