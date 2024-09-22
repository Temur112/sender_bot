from aiogram import Router, F, Bot
from aiogram.filters import ChatMemberUpdatedFilter, PROMOTED_TRANSITION, ADMINISTRATOR, MEMBER, KICKED
from aiogram.types import ChatMemberUpdated, Message
from managers import user, group
from config import TOKEN

router = Router()
bot = Bot(token=TOKEN)

@router.my_chat_member(ChatMemberUpdatedFilter(PROMOTED_TRANSITION))
async def handle_promotion(event: ChatMemberUpdated):
    user_id = event.from_user.id
    user_ = await user.UserManager.create_user(user_id)
    if user_ is None:
        await bot.send_message(user_id, "Something went wrong try again") ## need to be changed later
    group_id = event.chat.id
    group_ = await group.GroupManager.addnewGroup(user_id=user_id, group_id=group_id)
    if group_ is None:
        await bot.send_message(user_id, "Something went wrong") ## need to be changed later
    
    await bot.send_message(user_id, "you promoted this bot to your channel/group and now bot send all messages which you send this bot to your groups")

@router.message(F.text)
async def handle_messages(message: Message):
    # print(message)
    if message.chat.type == 'private':

        a = (await group.GroupManager.get_group_ids(message.from_user.id))
        # print(a[0])
        if len(a) != 0:
            for i in a:
                await bot.send_message(i, message.text)
        else:
            await bot.send_message(message.chat.id, "you have not promoted me to your group as admin yet")


@router.my_chat_member(ChatMemberUpdatedFilter(ADMINISTRATOR >> (MEMBER | KICKED)))
async def handle_promotion(event: ChatMemberUpdated):
    # print(event)
    user_id = event.from_user.id
    chat_id = event.chat.id
    res = await group.GroupManager.delete_group(user_id=user_id, group_id = chat_id)
    if res:
       await bot.send_message(user_id, f"you demoted me from {event.chat.title}")
    

'''
event.from_user.id
event.chat.id

'''