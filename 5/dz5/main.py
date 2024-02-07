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
from fastapi import FastAPI
from fastapi.responses import JSONResponse,HTMLResponse
from typing import Optional

app = FastAPI()


class Task(BaseModel):
    __index = 0
    __all = dict()
    title: str
    todo: Optional[str]
    status: Optional[bool]

    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, sum_modifier):
        self.__index += sum_modifier

    @classmethod
    def gather(cls, item: "Task"):
        cls.__all[cls.__index] = item
        cls.__index = 1

    @classmethod
    def select(cls, index: int):
        return cls.__all.get(index, None)

    @classmethod
    def reveal(cls):
        return cls.__all


@app.get("/tasks/")
async def select_all():
    print(Task.reveal())
    return JSONResponse(content=Task.reveal(), status_code=200)

@app.get("/")
async def test():
    return HTMLResponse("Hi")
@app.get("/tasks/{task_id}")
async def select_one(task_id: int):
    return JSONResponse(content=Task.select(task_id), status_code=200)


@app.post("/tasks/")
async def post_task(new_task: Task):
    Task.gather(new_task)
    return new_task


@app.put("/tasks/{task_id}")
def edit_task(task_id: int):
    raise NotImplemented


@app.delete("/tasks/{task_id}")
def delete_task():
    raise NotImplemented
