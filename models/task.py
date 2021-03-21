from .base import Model
from .app import App
from .task_cls import TaskClass


class Task(Model):
    status: str
    app_id: App
    cls_id: TaskClass
    cost: float
