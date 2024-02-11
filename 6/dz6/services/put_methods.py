from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .pydantics import Order, User, Ware
from .database_interface import WARES, CUSTOMERS, ORDERS, db

router = APIRouter()


@router.put("/wares/{ware_id}", response_model=Ware)
async def update_ware(ware_id: int, new_ware: Ware):
    query = WARES.update().where(WARES.c.id == ware_id).values(**new_ware.dict())
    await db.execute(query)
    return new_ware.dict()


@router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: User):
    query = CUSTOMERS.update().where(CUSTOMERS.c.id == user_id).values(**new_user.dict())
    await db.execute(query)
    return new_user.dict()


@router.put("/orders/{order_id}", response_model=Order)
async def update_order(order_id: int, new_order: Order):
    query = ORDERS.update().where(ORDERS.c.id == order_id).values(user_id=new_order.user_id, ware_id=new_order.ware_id,
                                                                  date=new_order.request_date, status=new_order.status)
    await db.execute(query)
    return new_order.dict()
