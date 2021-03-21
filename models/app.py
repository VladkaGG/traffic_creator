from .base import Model


class App(Model):
    name: str
    description: str
    tasks: list[dict]
    uri: str
