import asyncio
import logging
import os

from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
from bot.handlers import start, callback_tasks, creation



load_dotenv()
logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=os.getenv("token"))
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(start.router, callback_tasks.router, creation.router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

