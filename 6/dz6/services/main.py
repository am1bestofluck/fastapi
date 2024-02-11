import sqlalchemy
from fastapi import FastAPI
from databases import Database
from pathlib import Path
from fastapi.responses import HTMLResponse

from .read_methods import router as readers
# noinspection SpellCheckingInspection
from .delete_methods import router as razers
# noinspection SpellCheckingInspection
from .post_methods import router as ctors
from .put_methods import router as editors
from .database_interface import db

app = FastAPI()
app.include_router(readers)
app.include_router(razers)
app.include_router(ctors)
app.include_router(editors)


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


@app.get("/", response_class=HTMLResponse)
async def hellow():
    return HTMLResponse(
        content='<div style="display: flex; justify-content: center" id="rm"> <iframe width="560" height="315"' +
                ' src="https://www.youtube.com/embed/iAD6i2nYw8Q?si=KaQwxMSEnp9jDWO4" title="YouTube video player"' +
                ' frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope;' +
                ' picture-in-picture; web-share" allowfullscreen></iframe></div>',
        status_code=200)
