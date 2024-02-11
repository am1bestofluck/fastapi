import asyncio
from pathlib import Path
from databases import Database
from sqlalchemy import MetaData, create_engine
from sqlalchemy import Table, Column, String, Text, Float, Integer, ForeignKey,DateTime
# from sqla_tables import WARES, ORDERS, ORDER_STATUS, CUSTOMERS

DB_URL = f"sqlite:///{'' if Path('store.db').exists() else '../'}store.db"
db = Database(DB_URL)

engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
metadata = MetaData()

WARES = Table("WARES", metadata, Column("id", Integer, primary_key=True),
              Column("title", String, unique=True, nullable=False),
              Column("hint", Text),
              Column("price", Float)
              )

CUSTOMERS = Table("CUSTOMERS", metadata, Column("id", Integer, primary_key=True),
                  Column("first_name", String, nullable=False), Column("last_name", String),
                  Column("mail", String, nullable=False),
                  Column("password", String, nullable=False))
ORDERS = Table("ORDERS", metadata, Column("id", Integer, primary_key=True),
               Column("user_id", Integer, ForeignKey('CUSTOMERS.id')),
               Column("ware_id", Integer, ForeignKey('WARES.id')),
               Column("date", DateTime),
               Column("status", Integer, ForeignKey('ORDER_STATUS.id')))
ORDER_STATUS = Table("ORDER_STATUS", metadata, Column("id", Integer, primary_key=True),
                     Column("Title", String, unique=True))

DB_URL = f"sqlite:///store.db"


async def main():
    metadata.create_all(engine)


if __name__ == '__main__':
    asyncio.run(main())
