from db import database as db
from models.user import user


class UserManager:
    @staticmethod
    async def create_user(userid: str):
        ## check if user is already exists
        u = await db.fetch_one(user.select().where(user.c.id == userid))
        if u is not None:
            return u
        try:
            _id = await db.execute(user.insert().values(admin_tg_id=userid))
        except Exception as e:
            print(e)
            return None
        return await db.fetch_one(user.select().where(user.c.id == _id))
    
    