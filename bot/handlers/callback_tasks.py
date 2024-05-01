from aiogram import Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from bot.keyboards.complete_kb import completed_tasks_keyboard
from bot.keyboards.main_kb import create_task_keyboard
from database.ORM import get_data, get_tasks, create_task, get_all_tasks_with_users
from datetime import date

router = Router()


@router.callback_query(lambda callback_query: callback_query.data == 'задачи')
async def tasks_handler(query: CallbackQuery,):
    user_id, _, _, _ = await get_data(query)
    task = await get_tasks(query)
    if user_id == query.from_user.id:
        await query.message.answer(f'Ваши задачи на {date.today().strftime("%d-%m-%Y")}:\n\n{task}',
                                   reply_markup=completed_tasks_keyboard)


@router.callback_query(lambda c: c.data == 'all_tasks')
async def all_tasks_handler(query: CallbackQuery,):
    tasks = await get_all_tasks_with_users(query)
    await query.message.answer(f'Все задачи:\n\n{tasks}\n\nВыберите действие',
                               reply_markup=create_task_keyboard)
