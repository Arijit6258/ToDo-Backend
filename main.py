from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4
from typing import Optional

app = FastAPI()

todo_list = []


class SingleTodo(BaseModel):
    title: str
    completed: bool
    order: int


@app.get("/")
def get_all():
    return todo_list


@app.post("/")
def post_todo(todo_item: SingleTodo):
    unique_id = str(uuid4())
    url = "http://127.0.0.1:8000/" + unique_id
    response_item = todo_item.dict()
    response_item["id"] = unique_id
    response_item["url"] = url
    # TODO: use database instead of array to save the data
    todo_list.append(response_item)
    return response_item
