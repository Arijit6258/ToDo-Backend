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


def delete_todo(todo_id: str, db: Session):
    db.query(models.TodoItem).filter(models.TodoItem.id == todo_id).delete()
    db.commit()


def update_todo_status(todo_id: str, completed: bool, db: Session):
    todo_to_update = db.query(models.TodoItem).filter(models.TodoItem.id == todo_id).first()
    todo_to_update.completed = completed
    db.commit()
    db.refresh(todo_to_update)
    return todo_to_update


