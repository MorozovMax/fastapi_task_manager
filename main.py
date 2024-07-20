from fastapi import FastAPI

from src.db.database import delete_tables, create_tables
from src.api.tasks import router

from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Tables was deleted")
    await create_tables()
    print("Tables was created")
    print("Start")
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(router)