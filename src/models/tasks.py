from typing import Optional

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from src.schemas.tasks import STask


class Model(DeclarativeBase):
    pass

class TaskOrm(Model):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]

    def to_read_model(self) -> STask:
        return STask(
            id = self.id,
            name = self.name,
            description = self.description
        )