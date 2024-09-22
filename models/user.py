from sqlalchemy import Table, Integer, String, Column, func, DateTime
from db import metadata


user = Table(
    'user', 
    metadata,
    Column('id', Integer, primary_key=True),
    Column('admin_tg_id', String, unique=True),
    Column('created_at', DateTime, server_default=func.now()),
)