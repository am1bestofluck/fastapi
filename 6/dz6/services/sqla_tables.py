from sqlalchemy import Table, Column, Integer, String, Text, Float, ForeignKey,Date

from .database_interface import metadata

# WARES = Table("WARES", metadata, Column("id", Integer, primary_key=True),
#               Column("title", String, unique=True, nullable=False),
#               Column("hint", Text),
#               Column("price", Float)
#               )
#
# CUSTOMERS = Table("CUSTOMERS", metadata, Column("id", Integer, primary_key=True),
#                   Column("first_name", String, nullable=False), Column("last_name", String),
#                   Column("mail", String, nullable=False),
#                   Column("password", String, nullable=False))
# ORDERS = Table("ORDERS", metadata, Column("id", Integer, primary_key=True),
#                Column("user_id", Integer, ForeignKey('CUSTOMERS.id')),
#                Column("ware_id", Integer, ForeignKey('WARES.id')), Column("date", Date),
#                Column("status", Integer, ForeignKey('ORDER_STATUS.id')))
# ORDER_STATUS = Table("ORDER_STATUS", metadata, Column("id", Integer, primary_key=True),
#                      Column("Title", String, unique=True))
