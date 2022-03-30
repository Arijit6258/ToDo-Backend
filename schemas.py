from pydantic import BaseModel
from typing import Optional


class SingleTodo(BaseModel):
    title: str
    completed: bool
    order: int
    id: Optional[str] = None
    url: Optional[str] = None

    class Config:
        orm_mode = True


class CompletedStatus(BaseModel):
    completed: bool

    class Config:
        orm_mode = True
