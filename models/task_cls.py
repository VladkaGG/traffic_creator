from .base import Model
from enum import Enum


class TaskType(str, Enum):
    install: str = 'install'
    run: str = 'run'


class TaskClass(Model):
    name: str
    description: str
    type_name: TaskType
