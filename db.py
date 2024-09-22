from databases import Database
from sqlalchemy import MetaData
from config import TOKEN

DATABASE_URL = f'sqlite:///./database.db'

database = Database(DATABASE_URL)

metadata = MetaData()

