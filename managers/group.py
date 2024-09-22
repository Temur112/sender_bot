from db import database as db
from models.group import group
from models.user import user
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, delete


class GroupManager:
    @staticmethod
    async def addnewGroup(user_id: str, group_id: str):
        # check user is exist or not
        user_ = await db.fetch_one(user.select().where(user.c.admin_tg_id == user_id))
        if user_ is None:
            raise ValueError("user is not exist")
        
        try:
            group_ = await db.execute(group.insert().values(group_id=group_id, owner_id=user_id))
            return group_
        except Exception as e:
            print(e)
        
        

    @staticmethod
    async def get_group_ids(owner_id: str):
        query = select(group.c.group_id).where(group.c.owner_id == owner_id)

        res = await db.fetch_all(query)

        return [i['group_id'] for i in res]
    

    @staticmethod
    async def delete_group(user_id, group_id):
        query = delete(group).where((group.c.owner_id == user_id) & (group.c.group_id == group_id))

        try:
            await db.execute(query)
            return True
        except Exception:
            return False
        