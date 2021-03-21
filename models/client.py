from .base import Model


class Client(Model):
    login: str
    company_name: str
    photo: bytes
    balance: float
    email: str
    phone_number: str
