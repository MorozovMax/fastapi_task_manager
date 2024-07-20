from src.schemas.tasks import STaskAdd
from src.utils.repository import AbstractRepository


class TaskService():
    def __init__(self, task_repo: AbstractRepository):
        self.task_repo: AbstractRepository = task_repo

    async def add_task(self, task: STaskAdd):
        tasks_dict = task.model_dump()
        task_id = await self.task_repo.add_one(tasks_dict)
        return task_id

    async def get_all_tasks(self):
        res = await self.task_repo.find_all()
        return res
