from aiogram import Router, Bot
from aiogram.types import CallbackQuery, Message
from sqlalchemy import select
from bot.keyboards.complete_kb import completed_tasks_keyboard
from database.ORM import get_data
from datetime import date
from database.database import session
from database.models import Admins

router = Router()


@router.callback_query(lambda callback_query: callback_query.data == 'задачи')
async def tasks_handler(query: CallbackQuery,):
    user_id, _, _, = await get_data(query)
    if user_id == query.from_user.id:
        await query.message.answer(f'Ваши задачи на {date.today().strftime("%d-%m-%Y")}:\n\n{tasks}',
                                   reply_markup=completed_tasks_keyboard)


@router.callback_query(lambda c: c.data == 'completed_tasks')
async def completed_tasks_handler(query: CallbackQuery, bot: Bot, message: Message):
    user = await session.execute(select(Admins).where(Admins.user_id == message.from_user.id))
    result = user.scalar_one_or_none()
    if result:
        user_id = result.user_id
        if user_id == message.from_user.id:
            tasks = result.tasks
            await query.message.answer(f'Ваши задачи\n{tasks}', reply_markup=completed_tasks_keyboard)
