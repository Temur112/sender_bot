from aiogram import Dispatcher
from bot.handlers import router, bot
import asyncio


dp = Dispatcher()

dp.include_router(router)


async def main():
    await dp.start_polling(bot, allowed_updates=["message", "chat_member", "my_chat_member"])

if __name__ == "__main__":
    asyncio.run(main())


