from typing import Union

from aiogram.types import Message, CallbackQuery
from sqlalchemy import select

from database.database import session
from database.models import Admins, Tasks


async def get_data(message: Message):
    async with session.begin() as conn:
        query_db = (select(Admins).where(Admins.user_id == message.from_user.id))
        user = await conn.execute(query_db)
        result = user.scalar_one_or_none()
        if result:
            user_id = result.user_id
            name = result.name
            direction = result.direction
            manager = result.manager
            return user_id, name, direction, manager


async def get_tasks(query: CallbackQuery):
    async with session.begin() as conn:
        query_db = (select(Tasks.task).where(Tasks.user_id == query.from_user.id))
        user = await conn.execute(query_db)
        result = user.scalars().all()
        if result:
            return '\n'.join(result)


async def get_all_tasks(query: CallbackQuery):
    async with session.begin() as conn:
        query_db = (select(Tasks.task)).distinct()
        user = await conn.execute(query_db)
        result = [task for task in user.scalars().all() if task is not None]
        if result:
            return '\n'.join(result)


async def create_task(admin_id: int, task_description: str):
    async with session.begin() as conn:
        new_task = Tasks(user_id=admin_id, task=task_description)
        conn.add(new_task)
        await conn.commit()


async def get_admins(query: CallbackQuery):
    async with session.begin() as conn:
        query_db = (select(Admins.user_id, Admins.name).order_by(Admins.user_id))
        admins = await conn.execute(query_db)
        result = admins.scalars().all()
        admin_objects = []
        if isinstance(result, list) and all(isinstance(item, tuple) for item in result):
            admin_objects = [Admins(user_id=admin[0], name=admin[1]) for admin in result]
        return admin_objects

