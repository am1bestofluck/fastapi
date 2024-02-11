import databases

from sqlalchemy import Table, MetaData, create_engine, Column, Integer, Float, String, Text, Date, ForeignKey

DB_URL = "sqlite:///store.db"


def main():
    db = databases.Database(DB_URL)
    engine = create_engine(DB_URL)

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
                   Column("ware_id", Integer, ForeignKey('WARES.id')), Column("date", Date),
                   Column("status", Integer, ForeignKey('ORDER_STATUS.id')))
    ORDER_STATUS = Table("ORDER_STATUS", metadata, Column("id", Integer, primary_key=True),
                         Column("Title", String, unique=True))

    metadata.create_all(engine)


if __name__ == '__main__':
    main()
