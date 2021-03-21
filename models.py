from datetime import datetime
from pydantic import BaseModel


class Model(BaseModel):
    id: str
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
    "id": '60565f5c150820e17437f323',
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

print(user_obj.json())
