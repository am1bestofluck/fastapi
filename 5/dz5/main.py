"""
Необходимо создать API для управления списком задач.
Каждая задача должна содержать заголовок и описание.
Для каждой задачи должна быть возможность указать статус (выполнена/не выполнена).

API должен содержать следующие конечные точки:
— GET /tasks — возвращает список всех задач.
— GET /tasks/{id} — возвращает задачу с указанным идентификатором.
— POST /tasks — добавляет новую задачу.
— PUT /tasks/{id} — обновляет задачу с указанным идентификатором.
— DELETE /tasks/{id} — удаляет задачу с указанным идентификатором.

Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа.
Для этого использовать библиотеку Pydantic.
"""
from pydantic import BaseModel
from fastapi import FastAPI, Response
from typing import Optional

app = FastAPI()


class Task(BaseModel):
    title: str
    todo: Optional[str]
    status: Optional[bool]


class Base_of_sorts(dict):
    def put(self):

@app.get("/tasks/")
async def select_all():
    raise NotImplemented


@app.get("/tasks/{task_id}")
async def select_one():
    raise NotImplemented


@app.post("/tasks/")
async def post_task():
    raise NotImplemented


@app.put("/tasks/{task_id}")
def edit_task():
    raise NotImplemented


@app.delete("/tasks/{task_id}")
def delete_task():
    raise NotImplemented
