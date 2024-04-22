import asyncio
import logging
import os

from aiogram import Dispatcher, Bot
from dotenv import load_dotenv
from bot.handlers import start

load_dotenv()
logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=os.getenv("token"))
    dp = Dispatcher()
    dp.include_router(start.router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

