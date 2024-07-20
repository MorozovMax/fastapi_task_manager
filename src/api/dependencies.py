from src.repositories.tasks import TaskRepository
from src.services.task import TaskService


def task_service():
    return TaskService(TaskRepository())