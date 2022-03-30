from fastapi import FastAPI, Depends
import models
import crud
import schemas
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from uuid import uuid4
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


# CORS
origins = ["https://www.todobackend.com"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_model=list[schemas.SingleTodo])
def get_all(db: Session = Depends(get_db)):
    return crud.fetch_all_todos(db)


@app.post("/", response_model=schemas.SingleTodo)
def post_todo(todo_item: schemas.SingleTodo, db: Session = Depends(get_db)):
    unique_id = str(uuid4())
    url = "http://127.0.0.1:8000/" + unique_id
    todo_item.id = unique_id
    todo_item.url = url
    return crud.create_todo(db, todo_item)


@app.delete("/{todo_id}")
def delete_single_todo(todo_id: str, db: Session = Depends(get_db)):
    crud.delete_todo(todo_id, db)


@app.patch("/{todo_id}", response_model=schemas.SingleTodo)
def update_todo(todo_id: str, completed_status: schemas.CompletedStatus, db: Session = Depends(get_db)):
    return crud.update_todo_status(todo_id, completed_status.completed, db)


@app.put("/{todo_id}")
def update_todo_with_put(todo_id: str, updated_todo: schemas.SingleTodo, db: Session = Depends(get_db)):
    return crud.update_todo_status(todo_id, updated_todo.completed, db)

