from sqlalchemy import Column, Table, ForeignKey, Integer, String, func, DateTime, UniqueConstraint
from db import metadata


group = Table(
    'group',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('group_id', String),
    Column('owner_id', Integer, ForeignKey('user.id')),
    Column('created_at', DateTime, server_default=func.now()),
    UniqueConstraint('owner_id', 'group_id', name='unique_job_const')
)