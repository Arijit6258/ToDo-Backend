from fastapi import FastAPI, Depends
import models
import crud
import schemas
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from uuid import uuid4

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def get_all(db: Session = Depends(get_db)):
    return crud.fetch_all_todos(db)


@app.post("/", response_model=schemas.SingleTodo)
def post_todo(todo_item: schemas.SingleTodo, db: Session = Depends(get_db)):
    unique_id = str(uuid4())
    url = "http://127.0.0.1:8000/" + unique_id
    todo_item.id = unique_id
    todo_item.url = url
    return crud.create_todo(db, todo_item)
