
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.models.tasks import Model

engine = create_async_engine(
    "sqlite+aiosqlite:///tasks.db"
)

new_session = async_sessionmaker(engine, expire_on_commit=False)

async def get_async_session_maker():
    async with new_session() as session:
        yield session
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)