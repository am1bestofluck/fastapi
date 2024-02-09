"""
Необходимо создать API для управления списком задач.
Каждая задача должна содержать заголовок и описание.                                +
Для каждой задачи должна быть возможность указать статус (выполнена/не выполнена).  +

API должен содержать следующие конечные точки:
— GET /tasks — возвращает список всех задач.                                        +
— GET /tasks/{id} — возвращает задачу с указанным идентификатором.
— POST /tasks — добавляет новую задачу.                                             +
— PUT /tasks/{id} — обновляет задачу с указанным идентификатором.                   ?
— DELETE /tasks/{id} — удаляет задачу с указанным идентификатором.                  +

Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа.   +
Для этого использовать библиотеку Pydantic.
"""
import pdb

from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse
from typing import Optional

app = FastAPI()


class Tasks:
    instance = None
    _all = dict()
    _index = 0

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    @classmethod
    def reveal(cls):
        return {i: cls._all[i] for i in cls._all if
                cls._all[i].get('active', True)}

    @classmethod
    def add(cls, task: "Task"):
        cls._all[cls._index] = dict(task)
        cls._index += 1

    @classmethod
    def pop(cls, task_index: int):
        cls._all[task_index]['active'] = False

    @classmethod
    def __getitem__(cls, index: int):
        try:
            return cls._all[index] if cls._all[index].get('active',
                                                          True) else None
        except KeyError:
            return None

    @classmethod
    def __setitem__(cls, key, value):
        cls._all[key] = dict(value)


class Task(BaseModel):
    title: str
    todo: Optional[str]
    status: Optional[bool]


SRC = Tasks()


@app.get("/tasks/")
async def select_all():
    return JSONResponse(content=Tasks.reveal(), status_code=200)


@app.get("/")
async def test():
    return RedirectResponse(url="/docs", status_code=307)


@app.get("/tasks/{task_id}")
async def select_one(task_id: int):
    out = SRC[task_id]
    if out:
        return JSONResponse(content=out, status_code=200)
    return JSONResponse(content="{'found':null}", status_code=404)


@app.post("/tasks/")
async def post_task(item: Task):
    SRC.add(item)
    return HTMLResponse("Added!")


@app.put("/tasks/{task_id}")
async def edit_task(task_id: int, item: "Task"):
    if not SRC[task_id]:
        return RedirectResponse(url=f"/items/{task_id}", status_code=404)
    # pdb.set_trace()
    SRC[task_id] = item
    # pdb.set_trace()
    return RedirectResponse(url=f"/tasks/{task_id}", status_code=308)


@app.delete("/tasks/{task_id}",response_class=HTMLResponse)
async def delete_task(task_id: int):
    SRC.pop(task_id)
    return HTMLResponse("Deleted ;|")


if __name__ == '__main__':
    a = Tasks()
    b = Tasks()
