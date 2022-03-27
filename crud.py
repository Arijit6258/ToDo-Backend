import models
import schemas
from sqlalchemy.orm import Session, query


def create_todo(db: Session, todo_item: schemas.SingleTodo):
    db_todo_item = models.TodoItem(**todo_item.dict())
    db.add(db_todo_item)
    db.commit()
    db.refresh(db_todo_item)
    return db_todo_item


def fetch_all_todos(db: Session):
    return db.query(models.TodoItem).all()
