from database import Base
from sqlalchemy import Boolean, String, Integer, Column


class TodoItem(Base):
    __tablename__ = "todos"

    id = Column(String, primary_key=True)
    url = Column(String)
    completed = Column(Boolean)
    title = Column(String)
    order = Column(Integer)
