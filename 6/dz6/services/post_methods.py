import pdb

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .pydantics import Order, User, Ware
from .database_interface import CUSTOMERS, WARES, ORDERS, db
from .secrets_wrapper import hash_pwd
from datetime import datetime

router = APIRouter()


@router.post("/wares/", response_class=JSONResponse)
async def add_ware(new_ware: Ware):
    query = WARES.insert().values(title=new_ware.title, hint=new_ware.hint, price=new_ware.price)
    id_ = await db.execute(query)
    out = dict(new_ware)
    out.update({"new_id": id_})
    return JSONResponse(status_code=200, content=out)


@router.post("/users/", response_class=JSONResponse)
async def add_user(new_user: User):
    query = CUSTOMERS.insert().values(first_name=new_user.first_name, last_name=new_user.last_name,
                                      mail=new_user.mail, password=hash_pwd(new_user.password))
    id_ = await db.execute(query)
    return JSONResponse(status_code=200, content={"added": f"{new_user.first_name} {new_user.last_name}", "uid": id_})


@router.post("/orders/", response_class=JSONResponse)
async def add_order(new_order: Order):
    # pdb.set_trace()
    query = ORDERS.insert().values(user_id=new_order.user_id, ware_id=new_order.ware_id, status=new_order.status,
                                   date=new_order.request_date)
    id_ = await db.execute(query)
    # pdb.set_trace()
    out = dict(new_order)
    out['request_date'] = str(out['request_date'])
    out.update({"new_id": id_})
    return JSONResponse(status_code=200, content=out)
