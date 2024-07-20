from typing import Annotated

from fastapi import APIRouter, Depends

from src.schemas.tasks import STaskAdd, STask
from src.services.task import TaskService
from src.api.dependencies import task_service

router = APIRouter(
    prefix="/tasks"
)

@router.post("")
async def add_task(task: STaskAdd, task_service: Annotated[TaskService, Depends(task_service)]):
    task_id = await task_service.add_task(task)
    return {"task_id": task_id}

@router.get("")
async def get_tasks(task_service: Annotated[TaskService, Depends(task_service)]):
    res = await task_service.get_all_tasks()
    return res