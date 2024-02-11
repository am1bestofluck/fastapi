from datetime import date,datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictFloat, NaiveDatetime
from sqlalchemy import DateTime
from decimal import getcontext, Decimal

# noinspection SpellCheckingInspection
getcontext().prec = 2


class User(BaseModel):
    first_name: str = Field(
        title="Имя", description="req.", examples=['User0', 'Anton'], max_length=30)
    last_name: Optional[str] = Field(
        title="Имя", description="opt.", examples=['Surname0', 'Corei'], max_length=30)
    mail: str = Field(
        title="мыло", description="req.", examples=['Surname0.User0@mai.l', 'Corei123@q.w'],
        max_length=50)
    password: str = Field(
        title="pw", description="req.", examples=['yeah, how about no'], max_length=50)

    def keep_secrets(self):
        return ModestUser(first_name=self.first_name, last_name=self.last_name, mail=self.mail)


class ModestUser(BaseModel):
    first_name: str = Field(
        title="Имя", description="req.", examples=['User0', 'Anton'], max_length=30)
    last_name: Optional[str] = Field(
        title="Имя", description="opt.", examples=['Surname0', 'Corei'], max_length=30)
    mail: str = Field(
        title="мыло", description="req.", examples=['Surname0.User0@mai.l', 'Corei123@q.w'],
        max_length=50)


class Ware(BaseModel):
    title: str = Field(title="Название товара", description="req.", max_length=100)
    hint: str = Field(title="Описание товара", description="opt.", max_length=200)
    price: StrictFloat = Field(title="Цена товара", description="req.", gt=0, le=10 ** 6)


class Order(BaseModel):
    user_id: int = Field(title="внешний ключ", description="req.", examples=[1, 2])
    ware_id: int = Field(title="внешний ключ", description="req.", examples=[1, 2])
    request_date: datetime = Field(title="дата", description="тяжело :')",examples=[datetime.today(),datetime.now()])
    status: int = Field()
