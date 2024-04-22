from aiogram.types import Message, CallbackQuery
from sqlalchemy import select

from database.database import session
from database.models import Admins


async def get_data(message: Message):
    async with session.begin() as conn:
        query_db = (select(Admins).where(Admins.user_id == message.from_user.id))
        user = await conn.execute(query_db)
        result = user.scalar_one_or_none()
        if result:
            user_id = result.user_id
            name = result.name
            direction = result.direction
            return user_id, name, direction,
