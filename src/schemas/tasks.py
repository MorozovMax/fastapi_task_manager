from typing import Optional

from pydantic import BaseModel

class STaskAdd(BaseModel):
    name: str
    description: Optional[str]

class STask(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

    class Config:
        from_attributes = True