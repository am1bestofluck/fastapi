from .sqla import DB_URL
from databases import Database
from datetime import date, timedelta
import asyncio
from random import choice

from .secrets_wrapper import hash_pwd

"""1) это не ответ в зачёт; просто мне проще было отрабатывать crud на не пустой таблице; сначала rd, потом cu 
2)первая страничка документации databases даёт очень наглядный образец заполнения таблиц;
считаю что подключать flask - избыточно"""

DB = Database(DB_URL)
UNITS_QUANTITY = 10


async def build_status_table():
    query = "INSERT INTO ORDER_STATUS(Title) VALUES (:title)"
    values = [
        {"title": "Accepted"},
        {"title": "Rejected"},
        {"title": "Delivery in progress"},
        {"title": "packaging"},
        {"title": "Complete"}
    ]
    await DB.execute_many(query=query, values=values)


async def build_users_table():
    query = ("INSERT INTO CUSTOMERS(first_name ,last_name, mail, password) VALUES" +
             " (:first_name ,:last_name, :mail, :password)")
    values = [{"first_name": f"U_f_name_{i}", "last_name": f"U_l_name_{i}", "mail": f"U{i}@person.edu",
               "password": hash_pwd(str(i) * UNITS_QUANTITY)} for i in range(UNITS_QUANTITY)]
    await DB.execute_many(query=query, values=values)


async def build_wares_table():
    query = ("INSERT INTO WARES(title,hint,price)" +
             " VALUES(:title, :hint, :price)")
    values = [{"title": f"ware_{i}", "hint": f"hint on #{i}", "price": round(12.34 + i, 2)} for i in
              range(UNITS_QUANTITY)]
    await DB.execute_many(query=query, values=values)


async def build_orders_table():
    query = ("INSERT INTO ORDERS(user_id,ware_id,status,date)" +
             " VALUES(:user_id, :ware_id, :status,:date)")
    values = [{'user_id': choice(range(UNITS_QUANTITY)), 'ware_id': choice(range(UNITS_QUANTITY)),
               'status': choice(range(1, 5 + 1)), 'date': date.today() - timedelta(days=i)} for i in
              range(UNITS_QUANTITY * 2)]
    await DB.execute_many(query=query, values=values)


async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(build_status_table())
        task2 = tg.create_task(build_users_table())
        task3 = tg.create_task(build_wares_table())
        task4 = tg.create_task(build_orders_table())


if __name__ == '__main__':
    asyncio.run(main())
