import pdb

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from .pydantics import Order, User, Ware

from sqlalchemy import select, delete
from .database_interface import engine, CUSTOMERS, ORDERS, WARES, db
from sqlalchemy.orm import Session

router = APIRouter()


@router.delete("/wares/{ware_id}", response_class=JSONResponse)
async def delete_ware(ware_id: int):
    query = WARES.delete().where(WARES.c.id == ware_id)
    await db.execute(query)
    return {"from now on": 404}


@router.delete("/users/{user_id}", response_class=JSONResponse)
async def delete_user(user_id: int):
    query = CUSTOMERS.delete().where(CUSTOMERS.c.id == user_id)
    await db.execute(query)
    return {"from now on": 404}


@router.delete("/orders/{order_id}", response_class=JSONResponse)
async def delete_order(order_id: int):
    query = ORDERS.delete().where(ORDERS.c.id == order_id)
    await db.execute(query)
    return {"from now on": 404}
