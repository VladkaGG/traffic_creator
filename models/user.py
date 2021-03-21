from .base import Model
from fastapi import Query


class User(Model):
    email: str = Query(..., regex=r"^([a-zA-Z0-9 \-\.]+)@([a-zA-Z0-9 \-\.]+)\.([a-zA-Z]{2,5})$")
    login: str
    password: str
    monetary_info: dict
    tasks: list[dict]
    phone_number: str
