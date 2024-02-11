import datetime

from fastapi import APIRouter
from typing import List
from .database_interface import db, engine, WARES, CUSTOMERS, ORDERS
from .pydantics import Order, User, Ware, ModestUser

from sqlalchemy import select
from fastapi.responses import JSONResponse
import pdb

router = APIRouter()


@router.get("/users/", response_model=List[ModestUser])
async def fetch_users_all():
    with engine.connect() as session:
        all_ = session.execute(select(CUSTOMERS)).all()
    out = []
    for i in all_:
        out.append(User(
            first_name=i[1], last_name=i[2],
            mail=i[3], password=i[4]).keep_secrets())

    return out


@router.get("/wares/", response_model=List[Ware])
async def fetch_wares_all():
    with engine.connect() as session:
        all_ = session.execute(select(WARES)).all()

    return all_


@router.get("/orders/", response_model=List[Order])
async def fetch_orders_all():
    with engine.connect() as session:
        all_ = session.execute(select(ORDERS)).all()
    out = []
    for i in all_:
        out.append(Order(user_id=i[1], ware_id=i[2], request_date=i[3], status=i[4]))
    return out


@router.get("/users/{user_id}", response_model=ModestUser, response_class=JSONResponse)
async def fetch_users_filtered(user_id: int):
    with engine.connect() as session:
        usr = session.execute(select(CUSTOMERS).filter_by(id=user_id)).first()
    try:
        out = User(
            first_name=usr[1], last_name=usr[2],
            mail=usr[3], password=usr[4]).keep_secrets()
        return out
    except TypeError:
        return JSONResponse(content={"user": "not found"}, status_code=404)


@router.get("/wares/{ware_id}", response_model=Ware, response_class=JSONResponse)
async def fetch_wares_filtered(ware_id: int):
    with engine.connect() as session:
        itm = session.execute(select(WARES).filter_by(id=ware_id)).first()
    return itm if itm else JSONResponse(content={"item": "not found"}, status_code=404)


@router.get("/orders/{order_id}", response_model=Order, response_class=JSONResponse)
async def fetch_orders_filtered(order_id: int):
    with engine.connect() as session:
        i = session.execute(select(ORDERS).filter_by(id=order_id)).first()
    # pdb.set_trace()
    try:
        return Order(user_id=i[1], ware_id=i[2], request_date=i[3], status=i[4])
    except TypeError:
        return JSONResponse(content={"order": "not found"}, status_code=404)
